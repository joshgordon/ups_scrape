#!/usr/bin/env python
import subprocess
import os

# Wattage rating of the UPS. Since the UPS daemon returns load in percent,
# you have to specify the wattage rating to get it back into watts. 
# You can either do some math with the front panel to figure this out,
# read the specs on your UPS, or use 'pwrstat -status' from somewhere with
# the cyberpower software installed and look for "Rating Power."
RATING_W = 900

# device name of the UPS. This is the name that you specified in
# /etc/nut/ups.conf
DEVNAME = 'test'

DEVNULL = open(os.devnull, 'w')

load = subprocess.check_output(['upsc',  DEVNAME, 'ups.load'], stderr=DEVNULL).strip()
voltage = subprocess.check_output(['upsc', DEVNAME, 'input.voltage'], stderr=DEVNULL).strip()
battery = subprocess.check_output(['upsc', DEVNAME, 'battery.charge'], stderr=DEVNULL).strip()
battery_v = subprocess.check_output(['upsc', DEVNAME, 'battery.voltage'], stderr=DEVNULL).strip()

load_w = int(load) / 100.0 * RATING_W


print("Load: %s, Voltage: %s, battery percent: %s, battery voltage: %s" % (load_w, voltage, battery, battery_v))
