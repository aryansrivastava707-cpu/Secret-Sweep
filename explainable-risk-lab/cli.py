import argparse,csv,json
from model import fit,explain,predict
from metrics import evaluate

def main():
    p=argparse.ArgumentParser(description="Fit and explain a synthetic binary risk model")
    p.add_argument("csv");p.add_argument("--epochs",type=int,default=4000);p.add_argument("--threshold",type=float,default=.5);args=p.parse_args()
    with open(args.csv,newline="",encoding="utf-8") as f: rows=list(csv.DictReader(f))
    if any(r.get("label") not in ("0","1") for r in rows): raise SystemExit("CSV label must be 0 or 1")
    split=max(1,int(len(rows)*.8));train,test=rows[:split],rows[split:]
    if not test: test=train
    model=fit(train,epochs=args.epochs);actual=[int(r["label"]) for r in test];pred=[predict(model,r,args.threshold) for r in test]
    print(json.dumps({"metrics":evaluate(actual,pred),"example":explain(model,test[0]),"threshold":args.threshold},indent=2))
if __name__=="__main__":main()
