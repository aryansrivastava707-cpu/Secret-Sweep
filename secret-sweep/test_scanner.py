import tempfile,unittest
from pathlib import Path
from scanner import fingerprint,scan_text,scan_tree
class ScannerTests(unittest.TestCase):
 def test_detects_and_redacts_cloud_key(self):
  findings=scan_text('KEY=AKIA1234567890ABCDEF','sample.env');self.assertEqual(len(findings),1);self.assertEqual(findings[0]['redacted'],'[REDACTED]');self.assertNotIn('AKIA',str(findings))
 def test_allowlist_and_inline_ignore(self):
  value='ghp_'+'A'*30;fp=fingerprint(value);self.assertEqual(scan_text('TOKEN='+value,allowlist=[fp]),[]);self.assertEqual(scan_text('TOKEN='+value+' # secret-sweep: ignore'),[])
 def test_tree_skips_vendor_and_reports_relative_path(self):
  with tempfile.TemporaryDirectory(dir=Path(__file__).parent) as t:
   root=Path(t);(root/'src').mkdir();(root/'src'/'a.txt').write_text('AKIA1234567890ABCDEF');(root/'node_modules').mkdir();(root/'node_modules'/'x.txt').write_text('AKIA1234567890ABCDEF')
   found=scan_tree(root);self.assertEqual(len(found),1);self.assertEqual(Path(found[0]['path']),Path('src')/'a.txt')
if __name__=='__main__':unittest.main()
