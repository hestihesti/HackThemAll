import os
import sys
from termcolor import colored
import time

def xss():
	win = 'gnome-terminal'
	dwnld = input('Do You Have XSStrike Downloaded <y/n>:  ')
	placed = input('Is XSStrike Already In The Collabs Directory <y/n>:  ')
	if dwnld == 'y':
		if placed == 'n':
			locate = 'locate XSStrike'
			os.system(locate)
			print(colored('Copy The Path To The XSStrike Directory', 'yellow'))
			paste = input('Paste The Path Here:  ')
			copy = 'cp -r ' + paste + ' collabs/'
			os.system(copy)
			target = input('Put In URL You Are Targeting: ')
			post = input('Put In Post Data (Inspect Website(Right-Click On Website, Select Inspect, Select Network, Refresh Page, And Find \nAnything That Says "POST", Copy Labeled "Cooke": ')
			save = input('Did You Want To Save Your Results <y/n>:  ')
			if save == 'n':
				py = 'python3 collabs/XSStrike/xsstrike.py -u ' + target + 'data="' + post + '" --crawl --level 3 --blind'
				os.system(py)
			if save == 'y':
				name = input('What Would You Like The File Name To Be:  ')
				py = 'python3 collabs/XSStrike/xsstrike.py -u ' + target + 'data="' + post + '" --crawl --level 3 --blind -o ' + name
				os.system(py)

		elif placed == 'y':
			target = input('Put In URL You Are Targeting: ')
			post = input('Put In Post Data (Inspect Website(Right-Click On Website, Select Inspect, Select Network, Refresh Page, And Find \nAnything That Says "POST", Copy Labeled "Cooke": ')
			save = input('Would You Want To Save Your Results <y/n>:  ')
			if save == 'y':
				name = input('What Would You Like The Name Of The File To Be:  ')
				py = 'python3 collabs/XSStrike/xsstrike.py -u ' + target + 'data="' + post + '" --crawl --level 3 --blind -o ' + name
				os.system(py)

			if save == 'n':
				py = 'python3 collabs/XSStrike/xsstrike.py -u ' + target + 'data="' + post + '" --crawl --level 3 --blind'
				os.system(py)

		else:
			print(colored('Invalid Input', 'red'))

	elif dwnld == 'n':
		path = 'collabs/'
		mv = 'mv XSStrike collabs/'
#		os.system(win)
#		cd = 'cd ' + path
#		os.system(cd)
		github = 'git clone https://github.com/s0md3v/XSStrike.git'
		os.system(github)
		time.sleep(2)
		os.system(mv)
		time.sleep(1)
		pip = 'pip3 install -r collabs/XSStrike/requirements.txt'
		chmod = 'chmod +x collabs/XSStrike/xsstrike.py'
		os.system(pip)
		os.system(chmod)
		exit = 'exit'
		os.system(exit)
		print(colored('Program Is Now Installed, Please Re-Run Program', 'green'))
