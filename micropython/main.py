from machine import Pin, SPI, ADC
from neopixel import NeoPixel
from time import sleep
import thermistor
import urandom
import util


pixel = NeoPixel(Pin(5, Pin.OUT), 1)
spi = SPI(1, baudrate=1000000, polarity=0, phase=0)
cs=Pin(15, Pin.OUT)
thermistorAdc = ADC(0)
button = Pin(4, Pin.IN, Pin.PULL_UP)

def setPixel(r, g, b):
	pixel[0] = (r, g, b)
	pixel.write()         

def setLeds(b):
	cs.off();
	spi.write(bytearray([b]))
	cs.on();

def getTemperature():
	return thermistor.lsbToTemperature(thermistorAdc.read())



def wiggleFeet():
	for t in range(10):
		setLeds(0x55)
		sleep(0.07)
		setLeds(0xAA)
		sleep(0.07)
	setLeds(0)

def cycleFeet():
	for t in range(8):
		setLeds(1 << t)
		sleep(0.1)


def flash(color):
	if None == color:
		color = urandom.getrandbits(8)
	(r, g, b) = util.colorWheel(color)
	setPixel(r, g, b)
	while r > 0 or g > 0 or b > 0:
		if r > 0:
			r = r - 1
		if g > 0:
			g = g - 1
		if b > 0:
			b = b - 1
		setPixel(r, g, b)
		sleep(0.01)

# setPixel(0, 0, 0)
# wiggleFeet()
# flash(None)
# cycleFeet()
# cycleFeet()
# cycleFeet()


temp = getTemperature()
MODE1 = 1
MODE2 = 2

mode = MODE1

while True:
	print(getTemperature())

	if MODE1 == mode:
		if abs(getTemperature() - temp) > 2:
			temp = getTemperature()
			flash(int(util.translate(temp, 5, 30, 0, 255)))
			sleep(0.1)
		setLeds(urandom.getrandbits(8))
		sleep(0.01)
	elif MODE2 == mode:
		temp = getTemperature()
		(r,g,b) = util.colorWheel(int(util.translate(temp, 5, 30, 0, 255)))
		setPixel(r, g, b)
		cycleFeet()

	if 0 == button.value():
		setPixel(0,0,0)
		setLeds(0)
		if mode < MODE2:
			mode = mode + 1
		else:
			mode = MODE1
		while 0 == button.value():
			print(button.value())