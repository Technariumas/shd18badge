from machine import Pin, SPI, ADC
from neopixel import NeoPixel
from time import sleep

pixel = NeoPixel(Pin(5, Pin.OUT), 1)
spi = SPI(1, baudrate=1000000, polarity=0, phase=0)
cs=Pin(15, Pin.OUT)
thermistor = ADC(0)

def setPixel(r, g, b):
	pixel[0] = (r, g, b)
	pixel.write()         

def setLeds(b):
	cs.off();
	spi.write(bytearray([b]))
	cs.on();

while True:
	# print(thermistor.read())
	setLeds(0x55)
	setPixel(4, 0, 0)
	sleep(0.2)
	setLeds(0xAA)
	setPixel(0, 4, 0)
	sleep(0.2)
	setLeds(0x00)
	setPixel(0, 0, 4)
	sleep(0.2)
