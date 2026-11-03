from firmware.logic import evaluate
for reading in [(5,50,False),(9,52,False),(7.5,48,True),(None,None,False)]:
 result=evaluate(*reading);print(reading,'=>',result)
