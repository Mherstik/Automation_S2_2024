#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 14:27:29 2024

@author: marcus
"""
import time
from urllib import request

import uuid
import re
# joins elements of getnode() after each 2 digits.
# using regex expression
print ("The MAC address in formatted and less complex way is : ", end="")
mac_add =  ':'.join(re.findall('..', '%012x' % uuid.getnode()))


## Create a Speedtester
def speedtester():
   
    ## start a timer / get current time
    dl_start = time.time()
    #print(dl_start)
    
    ### Download a file
    dl_file = "https://github.com/Mherstik/Automation_Trainee_Nov2024/raw/refs/heads/main/20MB.zip"
    
    ## download the file
    ## using a WITH to have it not stored permanently.
    with request.urlopen(dl_file) as response:
        response.read()
    
    ## stop the timer
    dl_stop = time.time() # dt.datetime.now(tz=None)
    #print(dl_stop)
    
    # Calculate time to download.
    dl_delta = dl_stop - dl_start
    #print(dl_delta)
    
    ## Convert the time to Mbps
    # speed = filesize / downloadtime
    speed = (20 * 8 ) / dl_delta
    return speed

speed = speedtester()
print(f"Your internet is running at {speed:.2f}Mbps")
### check if file exists.
## if file DOES NOT exist... write the headers
## if file exists... move to adding speed to file
## else add speed to file


filename = "tester.csv"
f = open(filename, "a")

f.write("Time/Date, Speed\n")  ## make this optional

f.write(f"{time.ctime()},")
f.write(str(speed) + "," + mac_add + "\n")
f.close()

### Read the file
with open(filename, "r") as f:
    print(f.read())