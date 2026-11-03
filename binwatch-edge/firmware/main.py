from machine import Pin
from time import sleep_us,sleep
from logic import assess
trigger=Pin(5,Pin.OUT);echo=Pin(18,Pin.IN)
def read_distance():
    trigger.value(0);sleep_us(3);trigger.value(1);sleep_us(10);trigger.value(0)
    duration=machine_time_pulse_us(echo,1,30000)
    return None if duration<0 else duration*0.0343/2
# Import lazily because not all MicroPython builds expose this helper globally.
try:from machine import time_pulse_us as machine_time_pulse_us
except ImportError:machine_time_pulse_us=lambda pin,level,timeout:-1
while True:
    samples=[read_distance() for _ in range(5)];result=assess(samples)
    print(result);sleep(60)
