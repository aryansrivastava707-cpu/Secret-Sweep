import math
FEATURES=("utilization","late_payments","debt_ratio","account_age")
def sigmoid(x):
    if x>=0:
        z=math.exp(-min(x,60)); return 1/(1+z)
    z=math.exp(max(x,-60)); return z/(1+z)
def fit(rows,epochs=4000,learning_rate=0.08,l2=0.01):
    if not rows: raise ValueError("training data is empty")
    if epochs<1: raise ValueError("epochs must be positive")
    means={k:sum(float(r[k]) for r in rows)/len(rows) for k in FEATURES}
    scales={k:max(1e-9,math.sqrt(sum((float(r[k])-means[k])**2 for r in rows)/len(rows))) for k in FEATURES}
    weights={k:0.0 for k in FEATURES}; bias=0.0
    for _ in range(epochs):
        grad={k:0.0 for k in FEATURES}; gb=0.0
        for row in rows:
            z=bias+sum(weights[k]*((float(row[k])-means[k])/scales[k]) for k in FEATURES)
            err=sigmoid(z)-int(row["label"]); gb+=err
            for k in FEATURES: grad[k]+=err*((float(row[k])-means[k])/scales[k])
        n=len(rows); bias-=learning_rate*gb/n
        for k in FEATURES: weights[k]-=learning_rate*(grad[k]/n+l2*weights[k])
    return {"features":list(FEATURES),"means":means,"scales":scales,"weights":weights,"bias":bias}
def explain(model,row):
    contributions={k:model["weights"][k]*((float(row[k])-model["means"][k])/model["scales"][k]) for k in FEATURES}
    logit=model["bias"]+sum(contributions.values())
    return {"probability":sigmoid(logit),"contributions":contributions,"base_logit":model["bias"]}
def predict(model,row,threshold=0.5): return int(explain(model,row)["probability"]>=threshold)
