from firmware.logic import decide_pump
samples=[68,49,44,31,29,35,46,52]
pump=False
for value in samples:
 state=decide_pump(value,pump);pump=state['pump_on'];print('{:>5.1f}% moisture -> pump {}'.format(value,'ON' if pump else 'OFF'))
