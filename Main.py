import sys
import time
from private_data import data

from structures.Hal9000 import Hal9000

TOKEN = sys.argv[1]
ids = data.ids
bot = Hal9000(TOKEN, ids)

print ('Running ...')

while 1:
    time.sleep(10)