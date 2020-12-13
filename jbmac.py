#!/usr/bin/env python

import subprocess
from optparse import OptionParser
import re
import random
import sys

class mac_Changer():

    def __init__(self):
    	self.description=""
    	self.usage=""
    	if sys.version_info[0] >= 3:
    		self.description = "Need sudo perm. jbMac is Mac Changer. Version 1.0 // 12.13.2020"
    		self.usage = "Usage: sudo python3 ./jbMac.py -i [interface] { -m [mac address] }"
    	else:
    		self.description = unicode("Need sudo perm. jbMac is Mac Changer. Version 1.0 // 12.13.2020")
    		self.usage = unicode("Usage: sudo ./jbMac.py -i wlan0 \n & python3 jbMac.py -i wlan0")

    def getArg(self):
        argv=OptionParser(description=self.description, prog="jbMac -i [interface] ..", epilog="example: ./jbmac.py -i eth0 [-m ??:??:??:??:??:??]")
        argv.add_option("-i",dest="interface",help="\tSelect the interface to change")
        argv.add_option("-m",dest="mac",help="\tSet mac address")
        (options,arguments)= argv.parse_args()

        if not options.interface:
            argv.error("[-] Please select interface.")
        else:
            return options

    def macGenerator(self):
        tempArray=[]
        for x in range(6):
            tempArray.append(random.randint(16,255))
        mac_address=self.encryptor(tempArray)
        mac_address=':'.join(mac_address)
        return mac_address

    def encryptor(self,mac):
        encrypted = []
        for x in mac:
            encrypted.append(hex(x)[2:])
        return encrypted

    def changeMac(self,interface,mac):
        try:
            if options.mac:
                print(mac)
                subprocess.call(["ifconfig",interface, "down"])
                subprocess.call(["ifconfig",interface,"hw","ether",mac])
                subprocess.call(["ifconfig",interface, "up"])
            else:
                subprocess.call(["ifconfig",interface, "down"])
                subprocess.call(["ifconfig",interface,"hw","ether",self.macGenerator()])
                subprocess.call(["ifconfig",interface, "up"])

            self.checkMac(interface)
        except:
            print("ERROR!")



    def checkMac(self,interface):
        ifconfig=str(subprocess.check_output(["ifconfig",interface]))

        print("[+] Done. Current mac: "+re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig).group())


mac_changer=mac_Changer()
options=mac_changer.getArg()
if not options.mac:
    mac_changer.changeMac(options.interface,options.mac)
else:
    mac_changer.changeMac(options.interface,options.mac)
