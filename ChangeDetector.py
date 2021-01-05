import os
import time
from SQLconnection import *
class ChangeDetector:
    loc = ""
    folders = []
    def __init__(self,address):
        self.loc = address
    
    def check(self):
        direc = os.listdir(self.loc)
        if(direc != self.folders):
            for x in direc:
                if x not in self.folders:
                    print(x)
            for x in self.folders:
                if x not in direc:
                    print(x + " deleted")
            self.folders = direc
