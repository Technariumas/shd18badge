# This file is executed on every boot (including wake-boot from deepsleep)
import esp
esp.osdebug(None)

import network
network.WLAN(network.AP_IF).active(False)

import gc
#import webrepl
#webrepl.start()
gc.collect()
