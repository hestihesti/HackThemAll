import os
import sys
from termcolor import colored
import time
import socket

def honey():
	name = input('Name Of The Network You Want To Use (FreeWifi): ')
	ch = input('What Channel Do You Want To Be On (1-11): ')
	interf = input('What Interface Would You Like To Use (wlan0,eth0): ')
	s = ' '
	wifi = 'wifi-honey ' + name + s + ch + s + interf
	os.system(wifi)
