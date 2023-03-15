# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()
# boot.py -- run on boot-up

import network
import esp
esp.osdebug(None)
import gc
gc.collect()
import time


ssid = 'Controller-AP'
password = 'kutbilim'

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=ssid,authmode=network.AUTH_WPA_WPA2_PSK, password=password)

while ap.active() == False:
  pass

print('Connection successful: AP Wifi:')
print(ap.ifconfig()[0])


sta_if_ssid='wifiSSID'
sta_if_password='wifiPassword'
sta_if=network.WLAN(network.STA_IF)
count=3

while not sta_if.isconnected():
    sta_if.active(True)
    try:
        sta_if.connect(sta_if_ssid,sta_if_password)
    except Exception as e:
        print("Exception: ",e)
        break

    while not sta_if.isconnected() and count>0:
        print("connecting to STA WiFi!")
        time.sleep(0.2)
        count=count-1

 
print("STA Wifi: ",sta_if.ifconfig()[0])
