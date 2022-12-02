import os
import sys
from termcolor import colored
import time
from modules import nmap
from modules import nikto
from modules import ncrack1
from modules import searchsploit
from modules import xsstrike
from modules import sqlmap
from modules import commix
from modules import wpscan
from modules import aircrack
from modules import wifite
from modules import airgeddon
from modules import fern
from modules import bettercap
from modules import setoolkit
from modules import hashcat
from modules import wifi_honey




def hta():

	clear = 'clear'
	os.system(clear)

	logo = '''
			     x
                             x x			Hack Them All
	                   x xx x		     *******************
	                  x xxxx x               __   __  _____________     /\ 
	                 x xxxxxx x		|  | |  | |____    ____|   /  \ 
	                x xxxxxxxx x		|  | |  |      |  |       /    \ 
	               x xxxxxxxxxx x		|  |_|  |      |  |      /  /\  \ 
	              x xxxxxxxxxxxx x		|   _   |      |  |     /   __   \ 
	             x xx          xx x		|  | |  |      |  |    /   /  \   \ 
	            x   xxx    xxx   x x	|__| |__|      |__|   /___/    \___\ 
	           x  xxxx      xxxxx   x
	          x xx  xxx    xxxx  xxx x
	         x xxxxxx         xxxxxxx x
	        x xxxxxxxxxxxxxxxxxxxxxxxx x
	       x xxxxxxxxxxxxxxxxxxxxxxxxxx x
	      x xxxxxxxxxxxxxxxxxxxxxxxxxxxx x
	     x xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx x         ..created by..
	    x xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx x         {hestihesti}
	   x xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx x
	  x xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx x
	 x xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx x
	x                                          x
          xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
	'''

	logo2 = '''


     *  * * * * * * * * * * * * * * * * * * * * * * * *
          xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
       x x                                         x x
        x x                                       x x
	 x x                                     x x
	  x x                                   x x
	   x x                                 x x
	    x x                               x x
	     x x                             x x
	      x x                           x x
	       x x                         x x        Thank You For
		x x                       x x       Using HackThemAll
		 x x                     x x
		  x x                   x x
		   x x                 x x
		    x x               x x
		     x x             x x
		      x x           x x
		       x x         x x
        	        x x       x x
	                 x x     x x
		          x x   x x
			   x xxx x
                            x xx
                              x
	'''
	print(colored(logo, 'green'))
	time.sleep(3)

	print(colored('Create A New Tab And Type "tor"', 'cyan'))
	time.sleep(5)

	print(colored('\nWhat Kind Of Attack Would You Like To Perform? \n \n', 'yellow'))
	banner = '''
			[1] Exploit A Machine
			[2] Exploit A Website
			[3] WIFI Network
			[4] Man In The Middle
			[5] Forensics
			[6] Social-Engineering
			[7] Crack Passwords

	'''

	print(colored(banner, 'cyan'))
	user = input('> ')

#	EXPLOIT A MACHINE
	if user == '1':
		oS = '''
	[a] nmap
	[b] nikto

'''
		print(oS)
		slt = input('Which Program Would You Like To Use:\n > ')
		if slt == 'a':
			q5 = ''
			while q5 != 'q':
				nmap.nm()
				q7 = input('Is Port 21 Open <y/n>:  ')
				if q7 == 'y':
					ncrack1.nc1()
				if q7 == 'n':
					pass
				q3 = input('Were There Any Versions Listed <y/n>:  ')
				if q3 == 'y':
					searchsploit.ss()
				elif q3 == 'n':
					q5 = input('[c]ontinue scanning OR [q]uit: ')
					if q5 == 'c':
						continue
					elif q5 == 'q':
						break
				else:
					print(colored('Invalid Input', 'red'))

		if slt == 'b':
			nikto.NIK()


#	EXPLOIT A WEBSITE
	elif user == '2':
		optns = '''

[a] XSStrike
[b] SqlMap
[c] Commix
[d] Wpscan

		'''
		print(optns)
		Ur = input('> ')
		if Ur == 'a':
			xsstrike.xss()
		elif Ur == 'b':
			sqlmap.sql()
		elif Ur == 'c':
			commix.mix()
		elif Ur == 'd':
			wpscan.wps()
		else:
			print(colored('Invalid Input', 'red'))




#	ATTACK WIFI NETWORK
	elif user == '3':
		option1 = '''
[a] Aircrack-ng
[b] Wifite
[c] Airgeddon
[d] Fern Wifi Cracker
[e] Wifi-Honey
		'''
		print(colored(options1, 'cyan'))
		user1 = input('> ')
		if user1 == 'a':
			aircrack.ac()
		elif user1 == 'b':
			wifite.fite()
		elif user1 == 'c':
			airgeddon.geddy()
		elif user1 == 'd':
			fern.fern_wifi()
		elif user1 == 'e':
			wifi_honey.honey()
		else:
			print(colored('Invalid Input', 'red'))


#	MAN IN THE MIDDLE
	elif user == '4':
		print(colored('Man In The Middle', 'red'))
		bettercap.better()


#	FORENSICS
	elif user == '5':
		print(colored('Forensics', 'red'))


#	Social-Engineering-Toolkit
	elif user == '6':
		setoolkit.SET()

#	Crack Passwords
	elif user == '7':
		optns2 = '''

[a] ncrack
[b] ophcrack
[c] hashcat
[d] wordlists

		'''
		print(optns2)
		usrIn = input('> ')
		if usrIn == 'a':
			print('')
		elif usrIn == 'b':
			print('')
		elif usrIn == 'c':
			hashcat.hashkitty()

		elif usrIn == 'd':
			print('')
		else:
			print(colored('Invalid Input', 'red'))


	print(colored(logo2, 'yellow'))


hta()
