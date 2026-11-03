from machine import ADC, Pin
from time import sleep
from logic import decide_pump,adc_to_percent
sensor=ADC(Pin(34));sensor.atten(ADC.ATTN_11DB);relay=Pin(5,Pin.OUT);relay.value(0)
pump_on=False
while True:
    try:
        raw=sensor.read();moisture=adc_to_percent(raw)
        state=decide_pump(moisture,pump_on);pump_on=state['pump_on'];relay.value(1 if pump_on else 0)
        print('moisture={:.1f}% pump={} safe={}'.format(moisture,pump_on,state['safe']))
    except Exception as exc:
        pump_on=False;relay.value(0);print('sensor/control error; pump OFF:',exc)
    sleep(5)
