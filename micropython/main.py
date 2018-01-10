from machine import Pin
from neopixel import NeoPixel
from time import sleep

pin = Pin(0, Pin.OUT)   # set GPIO0 to output to drive NeoPixels
np = NeoPixel(pin, 1)   # create NeoPixel driver on GPIO0 for 8 pixels
while True:
	np[0] = (255, 0, 0) # set the first pixel to white
	np.write()              # write data to all pixels
	sleep(0.2)
	np[0] = (0, 255, 0) # set the first pixel to white
	np.write()              # write data to all pixels
	sleep(0.2)
	np[0] = (0, 0, 255) # set the first pixel to white
	np.write()              # write data to all pixels
	sleep(0.2)
