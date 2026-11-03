def evaluate(actual,predicted):
    if len(actual)!=len(predicted) or not actual: raise ValueError("labels and predictions must be non-empty and equal length")
    tp=sum(a==1 and p==1 for a,p in zip(actual,predicted)); tn=sum(a==0 and p==0 for a,p in zip(actual,predicted))
    fp=sum(a==0 and p==1 for a,p in zip(actual,predicted)); fn=sum(a==1 and p==0 for a,p in zip(actual,predicted))
    return {"accuracy":(tp+tn)/len(actual),"precision":tp/(tp+fp) if tp+fp else 0.0,"recall":tp/(tp+fn) if tp+fn else 0.0,"confusion":{"tn":tn,"fp":fp,"fn":fn,"tp":tp}}
