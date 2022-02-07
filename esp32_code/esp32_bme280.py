from mpy_bme280_esp8266 import bme280
from machine import Pin, I2C
from time import sleep

i2c = I2C(scl=Pin(4), sda=Pin(5))

while True:
    bme = bme280.BME280(i2c=i2c)
    print(bme.values[0], bme.values[1], bme.values[2])
    sleep(1.0)