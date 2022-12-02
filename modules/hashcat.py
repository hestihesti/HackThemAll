import os
import sys
import time
from termcolor import colored
import hashlib

def hashkitty():
	list = '''
	CHOOSE ONE OF THE OPTIONS

[a] bruteforce hashes and save the result to a file
[b] generate a hash

	'''
	print(list)
	select = input('> ')
	if select == 'a':
		hashes = input('Provide/Path/To/Your/Collection/Of/Hashes.txt: ')
		wl = input('Provide/Path/To/Your/Wordlist.txt: ')
		kitty = 'hashcat -m 500 -a 0 Done.txt ' + hashes + wl
		os.system(kitty)

	if select == 'b':
		word = input('Hash A Phrase Or A Word: ')
		hashobj1 = hashlib.md5()
		hashobj1.update(word.encode())
		print(colored(hashobj1.hexdigest(), 'cyan'))
		Save = input('Would You Like To Save The Output <y/n>:  ')
		if Save == 'y':
			with open('Results/Hashes.txt', 'a') as f:
				f.write(hashobj1.hexdigest())



