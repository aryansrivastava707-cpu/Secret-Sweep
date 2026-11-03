def fill_percent(distance_cm,empty_cm=80.0,full_cm=12.0):
    if distance_cm is None or not isinstance(distance_cm,(int,float)):return None
    if empty_cm<=full_cm:raise ValueError('empty distance must exceed full distance')
    if distance_cm<0 or distance_cm>400:return None
    value=(empty_cm-distance_cm)*100/(empty_cm-full_cm)
    return round(max(0.0,min(100.0,value)),1)
def median(values):
    if not values:return None
    ordered=sorted(values);mid=len(ordered)//2
    return ordered[mid] if len(ordered)%2 else (ordered[mid-1]+ordered[mid])/2
def assess(samples,threshold=80):
    valid=[x for x in samples if x is not None and 0<=x<=400]
    if not valid:return {"fill_percent":None,"pickup":False,"status":"sensor_error"}
    fill=fill_percent(median(valid))
    return {"fill_percent":fill,"pickup":fill>=threshold,"status":"pickup" if fill>=threshold else "normal"}
