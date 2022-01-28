from mpy_bme280_esp8266 import bme280
from machine import Pin, I2C

i2c = I2C(scl=Pin(4), sda=Pin(5))
bme = bme280.BME280(i2c=i2c)

print(bme.values)