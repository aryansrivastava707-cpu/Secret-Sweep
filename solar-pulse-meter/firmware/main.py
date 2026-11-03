from machine import Pin
from time import ticks_ms,sleep
from logic import PulseMeter
PULSES_PER_KWH=1000
meter=PulseMeter(PULSES_PER_KWH,debounce_ms=30)
input_pin=Pin(27,Pin.IN,Pin.PULL_UP)
def on_pulse(pin):meter.pulse(ticks_ms())
input_pin.irq(trigger=Pin.IRQ_FALLING,handler=on_pulse)
while True:
 now=ticks_ms();print('pulses={} energy={:.5f} kWh power={:.1f} W'.format(meter.count,meter.energy_kwh(),meter.power_w(now)))
 sleep(5)
