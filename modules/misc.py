import platform
import wget
import datetime
import os
import clipboard
import psutil
import shutil
from path import Path
from subprocess import PIPE, run
from colorama import init, Fore

init()

def ls():
	file = ''
	file += f'{"		File name".ljust(32)} Size (Bytes)\n'
	for root, dirs, files, in os.walk(".", topdown=False):
		for name in files:
			file += f'{os.path.join(root, name).ljust(12)} {os.path.getsize(os.path.join(root, name))} Bytes\n'
		for name in dirs:
			file += f'{os.path.join(root, name).ljust(22)} {os.path.getsize(os.path.join(root, name))} Bytes\n'
	return file

def echo(*, text):
	a = print(text)
	print()
	return a

def out(command):
	result = run(command, universal_newlines=True, shell=True)
	return result.stdout