import sys
import os
import traceback
import binascii

def clear():
	if os.name == 'nt':
		 _ = os.system('cls')
	else:
		_ = os.system('clear')

def mkdir_and_open(path, opentype):
	if not os.path.exists('cacheripper_ripped'):
		os.mkdir('cacheripper_ripped')
	if not os.path.exists(path):
		os.makedirs('cacheripper_ripped/' + os.path.dirname(path), exist_ok = True)
	return open('cacheripper_ripped/' + path, 'wb')

def draw_screen():
	clear()
	print('CACHERIPPER for The Beginner\'s Guide v1.0.1 - by GamingWithEvets\n')
	print('---------------------------------------------------------\nStealing Davey\'s The Beginner\'s Guide development work...\n---------------------------------------------------------')
	print('\nExtracted {0} file(s)\n\nSTATUS:'.format(extracted))
	if not done:
		print('Extracting {0} ({1} bytes)...'.format(filename, filedatalen))
	else:
		print('Done!')

try:
	clear()
	print('CACHERIPPER for The Beginner\'s Guide - by GamingWithEvets\n')

	if len(sys.argv) == 1:
		print('You must specify the path to filecache.bin in game-path/beginnersguide/!')
		print("\nPress Enter to exit.")
		input()
		clear()
		exit()
	else:
		i = 1
		file = ''

		while i < len(sys.argv):
			fn = sys.argv[i]
			if fn:
				if not os.path.exists(fn):
					i += 1
					
				else:
					file = fn
					break
			else:
				print('You must specify the path to filecache.bin in game-path/beginnersguide/!')
				print("\nPress Enter to exit.")
				input()
				clear()
				exit()

		if not file:
			print('I can\'t find the file(s) in your specified path(s)! Please double-check it/them.')
			print("\nPress Enter to exit.")
			input()
			clear()
			exit()

	cache = open(file, 'rb')
	header = cache.read(4)
	if not header == b'\x01\x01\x00\x00':
		print('Invalid filecache.bin! Please specify another one.')
		print("\nPress Enter to exit.")
		input()
		clear()
		exit()


	print('---------------------------------------------------------\nStealing Davey\'s The Beginner\'s Guide development work...\n---------------------------------------------------------')
	extracted = 0
	done = False

	filenamelen_b = cache.read(4)
	filenamelen_h = bytearray(filenamelen_b)
	filenamelen_h.reverse()
	filenamelen = int.from_bytes(filenamelen_h, "big")
	filename_b = cache.read(filenamelen)
	filename = binascii.b2a_qp(filename_b).decode('utf-8')
	filedatalen_b = cache.read(4)
	filedatalen_h = bytearray(filedatalen_b)
	filedatalen_h.reverse()
	filedatalen = int.from_bytes(filedatalen_h, "big")
	filedata = cache.read(filedatalen)
	draw_screen()
	file_to_write = mkdir_and_open(filename, 'wb')
	file_to_write.write(filedata)
	extracted += 1
	while not done:
		filenamelen_b = cache.read(4)
		if not filenamelen_b:
			done = True
			draw_screen()
			break
		filenamelen_h = bytearray(filenamelen_b)
		filenamelen_h.reverse()
		filenamelen = int.from_bytes(filenamelen_h, "big")
		filename_b = cache.read(filenamelen)
		filename = binascii.b2a_qp(filename_b).decode('utf-8')
		filedatalen_b = cache.read(4)
		filedatalen_h = bytearray(filedatalen_b)
		filedatalen_h.reverse()
		filedatalen = int.from_bytes(filedatalen_h, "big")
		filedata = cache.read(filedatalen)
		draw_screen()
		file_to_write = mkdir_and_open(filename, 'wb')
		file_to_write.write(filedata)
		extracted += 1
	print('\nFinished! You can look at the files in the newly-created cacheripper_ripped/ folder.\nI hope you enjoy looking at the files!\n\nPress Enter to exit.')
	input()
	clear()
	exit()

except Exception:
	print("\nMy my! An error occured!\n")
	print(traceback.format_exc())
	print("If possible, please report it to https://github.com/gamingwithevets/tbg-cacheripper/issues")
	print("\nPress Enter to exit.")
	input()
	clear()
	exit()