import os
import sys
from termcolor import colored

def nm():
	q1 = input('[ip] Address Or [web]site:  ')
	if q1 == 'ip':
		q2 = input('Type In The IP Address You Would Like To Scan: ')
		nmap1 = 'nmap -v -O -D RND:5 ' + q2
		nmap2 = 'nmap -v -sV --version-intensity 9 -D RND:7 -p7,19,20,21,22,23,25,37,53,69,79,80,110,111,135,137,138,139,445,161,443,512,513,514,1433,1434,1723,3389,8080 ' + q2 + ' -oX ' + q2 + '.xml'
		os.system(nmap1)
		os.system(nmap2)
		print(colored('Results Were Saved As.. ' + q2 + '.xml', 'green'))

	elif q1 == 'web':
		q4 = input('What Is The Website URL: ')
		nmap3 = 'nmap -v -O -D RND:5 ' + q4
		nmap4 = 'nmap -v -sV --version-intensity 9 -D RND:7 -p7,19,20,21,22,23,25,37,53,69,79,80,110,111,135,137,138,139,445,161,443,512,513,514,1433,1434,1723,3389,8080 ' + q4 + ' -oX ' + q4 + '.xml'
		os.system(nmap3)
		os.system(nmap4)
		print(colored('Results Were Saved As.. ' + q4 + '.xml', 'green'))
	else:
		print(colored('Invalid Input', 'red'))

