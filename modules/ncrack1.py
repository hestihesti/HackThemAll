import os
import sys
import time
from termcolor import colored

def nc1():
	adr = input('Whats The IP Address That Has This Port Open: ')
	crk = 'ncrack ftp://' + adr
	os.system(crk)


