from urllib.request import Request,urlopen
from urllib.error import URLError,HTTPError

def evaluate_headers(url,headers):
 h={str(k).lower():str(v).strip() for k,v in headers.items()};https=url.lower().startswith('https://');checks=[]
 def add(name,ok,severity,detail):checks.append({"name":name,"ok":bool(ok),"severity":severity,"detail":detail})
 csp=h.get('content-security-policy','');add('Content-Security-Policy',bool(csp),'high','Define a restrictive source policy; avoid unsafe-inline where possible.' if not csp else 'Policy is present; review allowed sources and directives.')
 hsts=h.get('strict-transport-security','');add('Strict-Transport-Security',bool(hsts) if https else True,'high' if https else 'info','Enable HSTS for HTTPS sites after confirming all subdomains support HTTPS.' if https and not hsts else ('Not applicable to an HTTP URL.' if not https else 'HSTS is present; review max-age and includeSubDomains.'))
 add('X-Content-Type-Options',h.get('x-content-type-options','').lower()=='nosniff','medium','Set X-Content-Type-Options: nosniff.')
 add('Referrer-Policy',bool(h.get('referrer-policy')),'low','Set a policy such as strict-origin-when-cross-origin.')
 add('Permissions-Policy',bool(h.get('permissions-policy')),'low','Disable browser features the site does not need.')
 frame_ok='frame-ancestors' in csp.lower() or h.get('x-frame-options','').lower() in ('deny','sameorigin')
 add('Clickjacking protection',frame_ok,'medium','Use CSP frame-ancestors or X-Frame-Options.')
 failed=[x for x in checks if not x['ok'] and x['severity']!='info'];weights={'high':25,'medium':15,'low':5}
 score=max(0,100-sum(weights.get(x['severity'],0) for x in failed))
 return {"url":url,"score":score,"checks":checks}

def fetch_headers(url,timeout=8):
 if not url.startswith(('http://','https://')):raise ValueError('URL must start with http:// or https://')
 request=Request(url,method='HEAD',headers={'User-Agent':'SecurityHeaderAuditor/1.0'})
 try:
  with urlopen(request,timeout=timeout) as response:return response.geturl(),dict(response.headers.items()),response.status
 except HTTPError as exc:return exc.geturl(),dict(exc.headers.items()),exc.code
 except URLError as exc:raise RuntimeError(f'Could not reach target: {exc.reason}') from exc
