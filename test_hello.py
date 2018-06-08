#!/usr/bin/env python3
from __future__ import print_function, unicode_literals
ip_addr = '192.168.10.101'
octets = ip_addr.split(".")
print ("Hello World")
print ("-" * 80)
print ("{:20}{:20}{:20}{:20}".format(octets[0], octets[1], octets[2], octets[3]))
#print (octets)
print ("-" * 80)
