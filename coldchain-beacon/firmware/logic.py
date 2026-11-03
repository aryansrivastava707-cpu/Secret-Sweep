def evaluate(temp_c,humidity_pct,alarm_on=False,sensor_ok=True,low=2.0,high=8.0,clear_low=2.5,clear_high=7.0,humidity_low=20.0,humidity_high=90.0,humidity_clear_low=25.0,humidity_clear_high=85.0):
    if not sensor_ok or temp_c is None or humidity_pct is None:
        return {"alarm":True,"status":"sensor_error","reason":"reading unavailable"}
    if not (-40<=temp_c<=85 and 0<=humidity_pct<=100):
        return {"alarm":True,"status":"invalid_reading","reason":"outside sensor range"}
    temp_out = temp_c<low or temp_c>high
    humidity_out = humidity_pct<humidity_low or humidity_pct>humidity_high
    if alarm_on:
        active = temp_c<clear_low or temp_c>clear_high or humidity_pct<humidity_clear_low or humidity_pct>humidity_clear_high
    else:
        active = temp_out or humidity_out
    reason = 'temperature outside band' if temp_out else ('humidity outside band' if humidity_out else 'readings within bands')
    return {"alarm":active,"status":"alert" if active else "normal","reason":reason}
