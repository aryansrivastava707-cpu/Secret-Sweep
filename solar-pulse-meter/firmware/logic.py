class PulseMeter:
    def __init__(self,pulses_per_kwh,debounce_ms=30):
        if pulses_per_kwh<=0 or debounce_ms<0:raise ValueError('pulse constant must be positive and debounce non-negative')
        self.pulses_per_kwh=float(pulses_per_kwh);self.debounce_ms=debounce_ms;self.count=0;self.last_ms=None;self.window=[]
    def pulse(self,now_ms):
        if self.last_ms is not None and now_ms-self.last_ms<self.debounce_ms:return False
        self.last_ms=now_ms;self.count+=1;self.window.append(now_ms);return True
    def energy_kwh(self):return self.count/self.pulses_per_kwh
    def power_w(self,now_ms,window_seconds=60):
        cutoff=now_ms-window_seconds*1000;self.window=[t for t in self.window if t>=cutoff]
        if len(self.window)<2:return 0.0
        elapsed=(self.window[-1]-self.window[0])/1000
        if elapsed<=0:return 0.0
        pulse_rate=(len(self.window)-1)/elapsed
        return pulse_rate*3600/self.pulses_per_kwh*1000
