import sys
import os
import traceback
import binascii
import msvcrt
import math
import decimal
from datetime import datetime

def clear():
	if os.name == 'nt':
		 _ = os.system('cls')
	else:
		_ = os.system('clear')

def mkdir_and_open(path, opentype):
	if not os.path.exists('cacheripper_ripped/' + exportdir):
		os.makedirs('cacheripper_ripped/' + exportdir)
	if not os.path.exists('cacheripper_ripped/' + exportdir + '/' + os.path.dirname(path)):
		os.makedirs('cacheripper_ripped/' + exportdir + '/' + os.path.dirname(path), exist_ok = True)
	return open('cacheripper_ripped/' + exportdir + '/' + path, 'wb')

def draw_screen(draw_verify = True, draw_steal = True, draw_status = True):
	clear()
	print('CACHERIPPER for The Beginner\'s Guide v1.1.0 - by GamingWithEvets\n')
	if draw_verify:
		print('Verifying number of files... OK\nVerifying file size... OK\n')
	if draw_steal:
		print('---------------------------------------------------------\nStealing Davey\'s The Beginner\'s Guide development work...\n---------------------------------------------------------')
		if draw_status:
			print('\nExtracted {0}/{1} file(s) - {2}%\n\nSTATUS:'.format(extracted, numfiles, round(extracted / numfiles * 100)))
			if not done:
				print('Extracting {0} - {1} ({2} bytes)...'.format(filename, convert_size(filedatalen), filedatalen))
			else:
				print('Done!')

def convert_size(size_bytes):
	if size_bytes == 0:
		return "0 bytes"
	size_name = ("bytes", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
	i = int(math.floor(math.log(size_bytes, 1024)))
	p = math.pow(1024, i)
	s = round(size_bytes / p)

	if i != 0:
		digits = 0
		while(s > 0):
			digits += 1
			s //= 10
		if digits == 1:
			s = round(size_bytes / p, 2)
			if str(s).endswith('.0') or str(s).endswith('.1') or str(s).endswith('.2') or str(s).endswith('.3') or str(s).endswith('.4') or str(s).endswith('.5') or str(s).endswith('.6') or str(s).endswith('.7') or str(s).endswith('.8') or str(s).endswith('.9'):
				return "%s0 %s" % (s, size_name[i])
		elif digits == 2:
			s = round(size_bytes / p, 1)
		elif digits == 3:
			s = round(size_bytes / p)

	return "%s %s" % (s, size_name[i])

def newexportdir(old_dir, set_dir = False):
	newexport = ''
	typedonce = False
	success = False
	while not success:
		draw_screen(draw_steal = False)
		if not typedonce:
			if not set_dir:
				if args.newexport:
					print('Directory {0} exists in cacheripper_ripped/.'.format(exportdir))
				print('Please specify a new export directory: ', end = '')
			else:
				print('Directory {0} also exists in cacheripper_ripped/.\nPlease type another export directory: '.format(exportdir), end = '')
		else:
			print('You cannot leave the export directory blank or type the old export directory.\nPlease type another export directory: ', end = '')
		newexport = input()
		if not newexport or newexport == old_dir:
			if not typedonce:
				typedonce = True
		else:
			draw_screen(draw_steal = False)
			print('New export directory: {0}\n\nIs this correct? [Y/N] '.format(newexport), end = '')
			final_choice = msvcrt.getche()
			draw_screen(draw_steal = False)
			if not final_choice.lower() == b'n':
				success = True
				return newexport
			else:
				newexport = ''
				typedonce = False


def get_data(set_global = False):
	if set_global:
		global filename, filedatalen
	filenamelen_b = cache.read(4)
	if not filenamelen_b:
		return True
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
	return False

def validate():
	filenamelen_b = cache.read(4)
	if not filenamelen_b:
		return 0, 0, True
	filenamelen_h = bytearray(filenamelen_b)
	filenamelen_h.reverse()
	filenamelen = int.from_bytes(filenamelen_h, "big")
	cache.seek(filenamelen, 1)
	filedatalen_b = cache.read(4)
	if not filedatalen_b:
		return filenamelen, 0, False
	filedatalen_h = bytearray(filedatalen_b)
	filedatalen_h.reverse()
	filedatalen = int.from_bytes(filedatalen_h, "big")
	cache.seek(filedatalen, 1)
	return filenamelen, filedatalen, False

import argparse
parser = argparse.ArgumentParser(description = 'Extracts the contents of filecache.bin, found in the files of the game The Beginner\'s Guide.', epilog = 'Please, DO NOT make the program scan a fake file cache! That makes me not happy.\n\n(c) 2022 GamingWithEvets Inc. All rights reserved.', formatter_class=argparse.RawTextHelpFormatter, allow_abbrev = False)
parser.add_argument('filecache_path', help = 'path to the file cache you want to extract')
parser.add_argument('-e', '--export', metavar = 'DIRECTORY', nargs = '?', default = 'filecache.bin', help = 'export directory in cacheripper_ripped/')
parser.add_argument('-d', '--disablelog', action = 'store_true', help = 'disable logging')
parser.add_argument('-o', '--overwrite', action = 'store_true', help = 'suppresses the export directory overwrite prompt')
parser.add_argument('-n', '--newexport', action = 'store_true', help = 'prompts you to enter a new export directory name if the old one is taken')
args = parser.parse_args()
if args.overwrite and args.newexport:
	parser.error('cannot combine -o/--overwrite with -n/--newexport')

try:
	clear()
	draw_screen(False, False)

	file = args.filecache_path
	exportdir = args.export

	cache = open(file, 'rb')
	
	numfiles_b = cache.read(4)
	numfiles_h = bytearray(numfiles_b)
	numfiles_h.reverse()
	numfiles = int.from_bytes(numfiles_h, "big")

	print('Verifying number of files... ', end = '')
	get_sizes = False
	filesize =  os.path.getsize(file)
	filelens = []
	filenamelens = []
	i = 0
	val0 = 0
	val1 = 0
	while not get_sizes:
		val0, val1, get_sizes = validate()
		if not get_sizes:
			if val0 != 0:
				filelens.append(val0)
				filenamelens.append(val0)
			if val1 != 0:
				filelens.append(val1)
	filesize_calc = 4
	for x in filelens:
		filesize_calc += 4
		filesize_calc += x
	if numfiles != len(filenamelens):
		print('file counts does not match\n\nFILE COUNT DOES NOT MATCH REPORTED FILE COUNT\nActual: {0} file(s) - Reported: {1} file(s)\n'.format(len(filenamelens), numfiles))
		print('Invalid file cache!\nPlease specify the right file, or double-check your specified file path.')
		print("\nPress Enter twice to exit.")
		input()
		print('Press Enter again to exit!')
		input()
		clear()
		exit()
	else:
		print('OK')

	print('Verifying file size... ', end = '')
	if filesize_calc != filesize:
		print('file sizes do not match\n\nFILE SIZE DOES NOT MATCH CALCULATED FILE SIZE\nActual: {0} ({1} bytes) - Calculated: {2} ({3} bytes)\n'.format(convert_size(filesize), filesize, convert_size(filesize_calc), filesize_calc))
		print('Invalid file cache!\nPlease specify the right file, or double-check your specified file path.')
		print("\nPress Enter twice to exit.")
		input()
		print('Press Enter again to exit!')
		input()
		clear()
		exit()
	else:
		print('OK\n')

	exportdircheck = False
	set_dir = False
	old_export = exportdir
	while not exportdircheck:
		if os.path.exists('cacheripper_ripped/' + exportdir):
			if args.newexport:
				exportdir = newexportdir(exportdir, set_dir)
				if not set_dir:
					set_dir = True
			elif args.overwrite:
				exportdircheck = True
			else:
				print('Directory "{0}" in cacheripper_ripped/ exists! Do you want to change the export directory name?\n[Y: Yes (Default) / N: No] '.format(exportdir), end = '')
				newexport_choice = msvcrt.getche()
				if not newexport_choice.lower() == b'n':
					exportdir = newexportdir(exportdir)
				else:
					exportdircheck = True
		else:
			exportdircheck = True
			
	draw_screen(draw_steal = False)
	extracted = 0
	done = False
	cache.seek(4, 0)
	get_data(True)
	if not args.disablelog:
		logfile = open('cacheripper_ripped/' + exportdir + '/cacheripper.log', 'w')
		logfile.write('CACHERIPPER RIP LOG - Auto-generated - DO NOT EDIT!\nTime of ripping: ' + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + '\nRipped file name/path: ' + file)
		logfile.write('\n\nFiles (sorted by file cache order):\n{0} - {1} ({2} bytes)'.format(filename, convert_size(filedatalen), filedatalen))
	extracted += 1
	while not done:
		done = get_data()
		if not done:
			if not args.disablelog:
				logfile.write('\n{0} - {1} ({2} bytes)'.format(filename, convert_size(filedatalen), filedatalen))
			extracted += 1
	draw_screen()
	print('\nFinished! You can look at the files in the cacheripper_ripped/{0} folder.\nI hope you enjoy looking at the files!\n\nPress Enter twice to exit.'.format(exportdir))
	input()
	print('Press Enter again to exit!')
	input()
	clear()
	exit()

except KeyboardInterrupt:
	print("\nScript exited with a KeyboardInterrupt!\n")
	print(traceback.format_exc())
	print("noice")
	exit()
except Exception:
	print("\nMy my! An error occured!\n")
	print(traceback.format_exc())
	print("If possible, please report it to https://github.com/gamingwithevets/tbg-cacheripper/issues")
	print("\nPress Enter twice to exit.")
	input()
	print('Press Enter again to exit!')
	input()
	clear()
	exit()