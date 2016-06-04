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

print ('Running ...')

while bot.running:
    time.sleep(10)
git_result = os.popen("git pull").read()
bot.send_master_message(git_result)
subprocess.Popen(["python", "Main.py", data.telegram_id])
bot.send_master_message("Finishing execution")
sys.exit()
