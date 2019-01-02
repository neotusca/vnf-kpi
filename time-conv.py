#!/usr/bin/python

import time
import datetime

unix_timestamp  = int("1545901895")
utc_time = time.gmtime(unix_timestamp)
#local_time = time.localtime(unix_timestamp)
#print(time.strftime("%Y-%m-%d %H:%M:%S", local_time)) 

print(time.strftime("%Y-%m-%dT%H:%M:%S", utc_time))  
print time.strftime("%Y-%m-%dT%H:%M:%S",  time.gmtime(1545901895))



now = datetime.datetime.now()
print now,type(now)

print now.strftime('%Y.%m.%d')

print datetime.datetime.now().strftime('%Y.%m.%d'), type( datetime.datetime.now().strftime('%Y.%m.%d') )




print datetime.datetime.utcnow()
