import time
import datetime
import Adafruit_DHT
import sys
import requests
import psutil
from system_info import get_temperature
def runController():
    dt = datetime.datetime.now()
    print(dt)
    print('Temperature: {0:0.1f} C'.format(tmp))
    print('Cpu Usage:    {0:0.1f} %'.format(Cpu))
    setDtState(dt)
    setTmpState(tmp)
    setCpuState(Cpu)
def setDtState(val):
    values = {'name': val}
    r = requests.put('http://127.0.0.1:8000/dt/1/', data=values, auth=('hello', 'nishil123'))
def setTmpState(val):
    values = {'name': val}
    r = requests.put('http://127.0.0.1:8000/tmp/1/', data=values, auth=('hello', 'nishil123'))
def setCpuState(val):
    values = {'name': val}
    r = requests.put('http://127.0.0.1:8000/Cpu/1/', data=values, auth=('hello', 'nishil123'))
while True:
    try:
        Cpu = psutil.cpu_percent()
        tmp = get_temperature()

        if Cpu is None or tmp is None:
            time.sleep(2)
            continue
        runController()
        time.sleep(10)
    except KeyboardInterrupt:
        exit()
