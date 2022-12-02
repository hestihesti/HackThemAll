import os
import sys
import time
from termcolor import colored

def wps():
	site = input('Paste URL Thats A Wordpress Site: ')

	qtn = input('Did You Want To Save Your Results <y/n>:  ')
	if qtn == 'y':
		name = input('What Would You Like The File To Be Named: ')
		wscan = 'wpscan -v --url ' + site + ' --random-user-agent -t 10 -e ap --ignore-main-redirect > ' + name + '.txt'
		os.system(wscan)
		print(colored('Your Results Have Been Saved', 'green'))

	if qtn == 'n':
		wscan = 'wpscan -v --url ' + site + ' --random-user-agent -t 10 -e ap --ignore-main-redirect'
		os.system(wscan)

