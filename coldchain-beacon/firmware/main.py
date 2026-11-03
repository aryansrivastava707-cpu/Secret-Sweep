from machine import Pin
from dht import DHT22
from time import sleep,time
from logic import evaluate
sensor=DHT22(Pin(4));led=Pin(2,Pin.OUT);alarm=False
while True:
    try:
        sensor.measure();temp=sensor.temperature();humidity=sensor.humidity()
        result=evaluate(temp,humidity,alarm);alarm=result['alarm'];led.value(1 if alarm else 0)
        print('{},{:.1f},{:.1f},{}'.format(int(time()),temp,humidity,result['status']))
    except Exception as exc:
        alarm=True;led.value(1);print('{},{},{},sensor_error'.format(int(time()),'', ''))
    sleep(30)
