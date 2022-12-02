import os
import sys
import time
from termcolor import colored

def mix():
#	ques = input('Would YOu Like To Perform A [simp]le Or [comp]lex Test:  ')
	win = 'gnome-terminal'
	tor = 'tor'
	print(colored('PLEASE MINIMIZE SCREEN ONCE TOR IS AT 100%', 'green'))
	time.sleep(2)
	os.system(win)
	os.system(tor)

	Loop = ''
	while Loop != 'q':
		if ques == 'comp':
			target = input('What Is The Targets URL: ')
			ltests = input('Level Of Tests To Perform (1-3)')
			cmx = 'commix -v --url="' + target + '" --random-agent --tor --tor-port="9050" --all --level="' + ltests + '" --dependencies'
			os.system(cmx)

		elif ques == 'simp':
			target = input('What Is The Targets URL: ')
			cmxx = 'commix -v --url="' + target + '" --tor --wizard'
			os.system(cmxx)

		else:
			print(colored('Invalid Input', 'red'))

		Loop = input('Press Any Key To Test A New URL, Press "q" To Quit:  ')

