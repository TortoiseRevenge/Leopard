import time
import os
from ChangeDetector import *
starttime = time.time()
name = os.getcwd()
name = "C:\Code Stuff"
print(name)
cd = ChangeDetector(name)
while True:
    cd.check()
    time.sleep(1.0 - ((time.time() - starttime) % 1.0))
