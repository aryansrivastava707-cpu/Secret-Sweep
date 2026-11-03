import argparse,json
from pathlib import Path
from scanner import scan_tree

def main():
 p=argparse.ArgumentParser(description="Scan a local tree for common secret patterns")
 p.add_argument('root');p.add_argument('--out',default='secret-findings.json');p.add_argument('--allowlist',default='.secret-sweep-allow.json');a=p.parse_args()
 allow=[]
 try:allow=json.loads(Path(a.allowlist).read_text(encoding='utf8')).get('fingerprints',[])
 except FileNotFoundError:pass
 findings=scan_tree(a.root,allow);Path(a.out).write_text(json.dumps({"count":len(findings),"findings":findings},indent=2),encoding='utf8')
 print(f"{len(findings)} possible findings; values redacted; report: {a.out}")
 if findings:raise SystemExit(1)
if __name__=='__main__':main()
