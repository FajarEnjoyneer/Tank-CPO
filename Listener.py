import sys
sys.path.append('../')
import time
from tinydb import TinyDB, Query
from DFRobot_ADS1115 import ADS1115
import requests

db = TinyDB('db.json')
data = Query()
ADS1115_REG_CONFIG_PGA_6_144V        = 0x00 # 6.144V range = Gain 2/3
ADS1115_REG_CONFIG_PGA_4_096V        = 0x02 # 4.096V range = Gain 1
ADS1115_REG_CONFIG_PGA_2_048V        = 0x04 # 2.048V range = Gain 2 (default)
ADS1115_REG_CONFIG_PGA_1_024V        = 0x06 # 1.024V range = Gain 4
ADS1115_REG_CONFIG_PGA_0_512V        = 0x08 # 0.512V range = Gain 8
ADS1115_REG_CONFIG_PGA_0_256V        = 0x0A # 0.256V range = Gain 16
ads1115 = ADS1115()

def convert(x)->str:
    x = int(x)
    in_min = 0
    in_max = 26670
    out_min = 0
    out_max = 30
    return str(round((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min,2))

while True :
    #Set the IIC address
    ads1115.setAddr_ADS1115(0x48)
    #Sets the gain and input voltage range.
    ads1115.setGain(ADS1115_REG_CONFIG_PGA_6_144V)
    #Get the Digital Value of Analog of selected channel
    ads1115.setChannel(0)
    adc0 = ads1115.readValue()
    tinggi = adc0
    # adc0 = 12
    API = "https://neptune.crocodic.net/iot-kelapa-sawit/public/api/device/sensor"
    data1 = {
    "code": "MT1",
    "level":tinggi
    }
    d = requests.post(url=API_SENSOR, data=data1)
    text = d.text
    print(text)