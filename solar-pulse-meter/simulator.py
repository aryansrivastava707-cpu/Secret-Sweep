from firmware.logic import PulseMeter
m=PulseMeter(1000);[m.pulse(t) for t in (0,1000,2000,2010,3000)]
print({'pulses':m.count,'energy_kwh':m.energy_kwh(),'power_w':m.power_w(3000)})
