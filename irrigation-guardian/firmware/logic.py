def decide_pump(moisture_pct, pump_on, dry_threshold=30.0, wet_threshold=45.0, sensor_ok=True):
    if not (0 <= dry_threshold < wet_threshold <= 100): raise ValueError('thresholds must satisfy 0 <= dry < wet <= 100')
    if not sensor_ok or not isinstance(moisture_pct,(int,float)) or not 0 <= moisture_pct <= 100:
        return {"pump_on":False,"safe":True,"reason":"invalid sensor reading"}
    next_state = moisture_pct < wet_threshold if pump_on else moisture_pct <= dry_threshold
    reason = 'watering until wet threshold' if next_state else 'moisture is adequate'
    return {"pump_on":next_state,"safe":False,"reason":reason}

def adc_to_percent(raw,dry_raw=3200,wet_raw=1400):
    if not 0 <= raw <= 4095 or dry_raw<=wet_raw: raise ValueError('invalid ADC calibration or reading')
    return max(0.0,min(100.0,(dry_raw-raw)*100/(dry_raw-wet_raw)))
