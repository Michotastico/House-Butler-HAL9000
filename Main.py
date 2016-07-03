#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import subprocess
import time
from private_data import data
from structures.Weather import Weather
'''
weather = Weather(data.city, data.pid)
weather.update()
weather.show()
'''

from structures.Hal9000 import Hal9000

print "Starting HAL-9000"
TOKEN = sys.argv[1]
ids = data.ids
bot = Hal9000(TOKEN, ids)

bot.send_master_message("HAL-9000 fully operational")

print ('Running ...')

while bot.running:
    time.sleep(10)
git_result = os.popen("git pull").read()
bot.send_master_message(git_result)
subprocess.Popen(["python", "Main.py", data.telegram_id])
bot.send_master_message("Finishing execution")
sys.exit()
'''
from structures.Database import EventDatabase

print "creating db"
db = EventDatabase('events.db')
print "inserting events"
db.add_event('Evento 1', 'Descripcion evento 1', 2016, 07, 03, 18, 00)
db.add_event('Evento 2', 'Descripcion evento 2', 2017, 07, 03, 18, 00)
print "request testing"
print "request all"
request = db.get_all_events()
for e in request:
    print e
print "request empty day"
request = db.get_events_from_day(2016, 07, 04)
for e in request:
    print e
print "request event 1 day"
request = db.get_events_from_day(2016, 07, 03)
for e in request:
    print e
print "request event 2 day"
request = db.get_events_from_day(2017, 07, 03)
for e in request:
    print e

'''