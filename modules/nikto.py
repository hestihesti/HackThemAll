import os
import sys
import time
from termcolor import colored
import socket

def NIK():
	url = input('What Is The URL: ')
	IP_address = socket.gethostbyname(url)
	print(IP_address)
	calc = 'ipcalc ' + IP_address
	os.system(calc)
	print(colored('\n \nCOPY THE NETWORK IP', 'yellow'))
	time.sleep(2)
	print('\n \n')
	paayste = input('And Paste It Here: ')
	netmap = 'nmap -v ' + paayste + ' -oG temp.txt'
	os.system(netmap)
	readable = 'cat temp.txt | awk "/Up$/{print $2}" | cat >> targetIP.txt'
	os.system(readable)
	nkto = 'nikto -v -h targetIP.txt >> ' + url + '.txt'
	os.system(nkto)
	lay = 'Results Were Saved As... ' + url + '.txt'
	print(colored(lay, 'green'))
