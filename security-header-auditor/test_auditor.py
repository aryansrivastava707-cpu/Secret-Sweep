import unittest
from auditor import evaluate_headers,fetch_headers
class HeaderTests(unittest.TestCase):
 def test_secure_header_set_scores_well(self):
  headers={'Content-Security-Policy':"default-src 'self'; frame-ancestors 'none'",'Strict-Transport-Security':'max-age=31536000','X-Content-Type-Options':'nosniff','Referrer-Policy':'strict-origin-when-cross-origin','Permissions-Policy':'camera=()'}
  result=evaluate_headers('https://example.test',headers);self.assertEqual(result['score'],100);self.assertTrue(all(c['ok'] for c in result['checks']))
 def test_missing_headers_are_prioritized(self):
  result=evaluate_headers('https://example.test',{});self.assertLess(result['score'],50);self.assertFalse(result['checks'][0]['ok'])
 def test_http_does_not_require_hsts(self):
  result=evaluate_headers('http://example.test',{});hsts=next(c for c in result['checks'] if c['name']=='Strict-Transport-Security');self.assertTrue(hsts['ok'])
 def test_rejects_non_http_url_before_request(self):
  with self.assertRaises(ValueError):fetch_headers('file:///etc/passwd')
if __name__=='__main__':unittest.main()
