import argparse,json
from pathlib import Path
from auditor import evaluate_headers,fetch_headers

def main():
 p=argparse.ArgumentParser(description='Check browser security headers for an authorized URL');p.add_argument('url');p.add_argument('--json');a=p.parse_args()
 final,headers,status=fetch_headers(a.url);result=evaluate_headers(final,headers);result['http_status']=status
 print(f"HTTP {status} · header score {result['score']}/100")
 for check in result['checks']:print(('OK  ' if check['ok'] else 'FIX ')+f"{check['name']}: {check['detail']}")
 if a.json:Path(a.json).write_text(json.dumps(result,indent=2),encoding='utf8')
if __name__=='__main__':main()
