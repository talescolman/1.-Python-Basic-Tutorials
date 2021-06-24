# how to shutdown your computer using python

import os 
  
shutdown = input("Do you wish to shutdown your computer ? (yes / no): ") 
  
if shutdown == 'no': 
    exit() 
else: 
    os.system("shutdown /s /t 1") # /t set the waiting time to turn off the computer in 1 second
