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

try:
	clear()
	print('CACHERIPPER for The Beginner\'s Guide - by GamingWithEvets\n')

	if not os.path.exists('filecache.bin'):
			print('Please place filecache.bin in the same directory as this script!\nOr you can do the other way around.')
			print("\nPress Enter to exit.")
			input()
			clear()
			exit()


	print('---------------------------------------------------------\nStealing Davey\'s The Beginner\'s Guide development work...\n---------------------------------------------------------')

	cache = open('filecache.bin', 'rb')
	cache.seek(4,0)
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
	file_to_write = mkdir_and_open(filename, 'wb')
	file_to_write.write(filedata)
	while cache:
		filenamelen_b = cache.read(4)
		if not filenamelen_b:
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
		file_to_write = mkdir_and_open(filename, 'wb')
		file_to_write.write(filedata)
	print('\nFinished! Now you don\'t need a hex editor to view the files.\nYou can view them right from your file explorer!\n\nPress Enter to exit.')
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