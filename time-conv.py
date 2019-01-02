#!/usr/bin/python

import time

unix_timestamp  = int("1545901895")
utc_time = time.gmtime(unix_timestamp)
#local_time = time.localtime(unix_timestamp)
#print(time.strftime("%Y-%m-%d %H:%M:%S", local_time)) 

print(time.strftime("%Y-%m-%dT%H:%M:%S", utc_time))  



print time.strftime("%Y-%m-%dT%H:%M:%S",  time.gmtime(1545901895))
