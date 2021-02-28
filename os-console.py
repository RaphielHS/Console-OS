import os
import time
try:
	import platform
	import wget
	import datetime
	import clipboard
	import psutil
	import shutil
	from path import Path
	from subprocess import PIPE, run
	from colorama import init, Fore
except ImportError:
	print("Updating Packages...")
	time.sleep(3)
	os.system("pip install --upgrade colorama psutil datetime wget path clipboard -q -U")
	import platform
	import wget
	import datetime
	import clipboard
	import psutil
	import shutil
	from path import Path
	from subprocess import PIPE, run
	from colorama import init, Fore

from modules import misc

init()

pl = platform.system()
if pl == "Windows":
	os.system("cls")
else:
	os.system("clear")

class Misc:
	def ls():
		file = ''
		file += f'{"File name".ljust(12)} {"<-<->->".ljust(12)} Size (Bytes)\n'
		for root, dirs, files, in os.walk(".", topdown=False):
			for name in files:
				file += f'{os.path.join(root, name).ljust(12)} {"<-<->->".ljust(12)} {os.path.getsize(os.path.join(root, name))} Bytes\n'
			for name in dirs:
				file += f'{os.path.join(root, name).ljust(22)} {"<-<->->".ljust(12)} {os.path.getsize(os.path.join(root, name))} Bytes\n'
		return file

	def echo(*, text):
		a = print(text)
		print()
		return a

	def out(command):
		result = run(command, universal_newlines=True, shell=True)
		return result.stdout

directory = os.getcwd()

print(f"""
    {Fore.CYAN}<-{Fore.RESET}{Fore.RED}<->{Fore.RESET}{Fore.CYAN}->{Fore.RESET}LISENCE{Fore.CYAN}<-{Fore.RESET}{Fore.RED}<->{Fore.RESET}{Fore.CYAN}->{Fore.RESET}
 {Fore.CYAN}<-{Fore.RESET}{Fore.RED}<->{Fore.RESET}{Fore.CYAN}->{Fore.RESET} MIT License {Fore.CYAN}<-{Fore.RESET}{Fore.RED}<->{Fore.RESET}{Fore.CYAN}->{Fore.RESET}

 Copyright (c) 2021 RaphielHS

 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in all
 copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 SOFTWARE.""")
input()

helpc = {
	"ls": "Get all files in the current directory",
	"cwd": "Get current working directory",
	"exit()": "Exit",
	"quit()": "Exit",
	"wget": "download stuff via the web (url)",
	"cat": "Print a file content's into console.",
	"cp": "Copy This Executeable File Location."
}
info = {
	"version": "InDev 1.1.2",
	"developer": "Raphiel#4045",
	"language": "Python"
}
dc = {
	"discord_tag": "Raphiel#4045",
	"discord_server": "None"
}
while True:
	try:
		command = input(f"{Fore.RED}[IN DEV] <Raphiel OS>{Fore.RESET} > ")
		if command == "ls":
			print(misc.ls())
			continue

		elif 'echo' in command:
			arg = command.replace("echo", '')
			Misc.echo(text=arg)
			continue

		elif 'info' in command:
			m = f''
			for cate, detail in info.items():
				m += f" {Fore.CYAN}<-{Fore.RESET}{Fore.RED}<->{Fore.RESET}{Fore.CYAN}->{Fore.RESET} {cate.ljust(15)} : {detail}\n"
			print(m)
			continue

		elif 'intro' in command:
			print(f"""
      {Fore.CYAN}<-{Fore.RESET}{Fore.RED}<->{Fore.RESET}{Fore.CYAN}->{Fore.RESET}LISENCE{Fore.CYAN}<-{Fore.RESET}{Fore.RED}<->{Fore.RESET}{Fore.CYAN}->{Fore.RESET}
 {Fore.CYAN}<-{Fore.RESET}{Fore.RED}<->{Fore.RESET}{Fore.CYAN}->{Fore.RESET} MIT License {Fore.CYAN}<-{Fore.RESET}{Fore.RED}<->{Fore.RESET}{Fore.CYAN}->{Fore.RESET}

 Copyright (c) 2021 RaphielHS

 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in all
 copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 SOFTWARE.""")
			input()
			continue

		elif 'lisence' in command:
			print(f"""
      {Fore.CYAN}<-{Fore.RESET}{Fore.RED}<->{Fore.RESET}{Fore.CYAN}->{Fore.RESET}LISENCE{Fore.CYAN}<-{Fore.RESET}{Fore.RED}<->{Fore.RESET}{Fore.CYAN}->{Fore.RESET}
 {Fore.CYAN}<-{Fore.RESET}{Fore.RED}<->{Fore.RESET}{Fore.CYAN}->{Fore.RESET} MIT License {Fore.CYAN}<-{Fore.RESET}{Fore.RED}<->{Fore.RESET}{Fore.CYAN}->{Fore.RESET}

 Copyright (c) 2021 RaphielHS

 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in all
 copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 SOFTWARE.""")
			input()
			continue

		elif 'discord' in command:
			m = f''
			for cate, asset in dc.items():
				m += f" {Fore.CYAN}<-{Fore.RESET}{Fore.RED}<->{Fore.RESET}{Fore.CYAN}->{Fore.RESET} {cate.ljust(15)} : {asset}"
			print(m)
			continue

		elif 'cd' in command:
			arg = command.replace("cd", '').replace(' ', '')
			with Path(str(arg)) as c:
				print(f"In      : {os.getcwd()}")
				print("ListDir : %s" % str(os.listdir()).replace("[", '').replace("]", '').replace('\'', ''))
				os.chdir(arg)
			continue

		elif 'about' in command:
			arg = command.replace("about ", '')
			if arg == "dev":
				print(f"""
 {Fore.CYAN}<-{Fore.RESET}{Fore.RED}<->{Fore.RESET}{Fore.CYAN}->{Fore.RESET} About Developer {Fore.CYAN}<-{Fore.RESET}{Fore.RED}<->{Fore.RESET}{Fore.CYAN}->{Fore.RESET}
 Created by {Fore.GREEN}Raphiel{Fore.RESET} as a project for improving his skill at {Fore.GREEN}Python{Fore.RESET}.
""")
			else:
				print(f"""
 {Fore.CYAN}<-{Fore.RESET}{Fore.RED}<->{Fore.RESET}{Fore.CYAN}->{Fore.RESET} About {Fore.CYAN}<-{Fore.RESET}{Fore.RED}<->{Fore.RESET}{Fore.CYAN}->{Fore.RESET}
 This code was created on {Fore.GREEN}25/02/2021{Fore.RESET} as a project just for fun, Coded by Raphiel as a project
 for improving his skill at {Fore.GREEN}Python{Fore.RESET}.
""")

		elif 'github' in command:
			print(Fore.GREEN + " [SUCESS] " + Fore.RESET + "{0} https://github.com/RaphielHS/Console-OS {1}".format(Fore.GREEN, Fore.RESET))

		elif 'exit()' in command:
			quit()

		elif 'quit()' in command:
			quit()

		elif command in ['cwd', 'pwd']:
			print("a " + os.getcwd())
			continue

		elif 'cat' in command:
			arg = command.replace("cat ", '')
			try:
				f = open(arg, 'r')
				print(f.read())
			except OSError:
				print(f"'{arg}' is not a valid filename.")
			continue

		elif 'wget' in command:
			arg = command.replace("wget ", '')
			try:
				print(f"{Fore.CYAN}<-{Fore.RESET}{Fore.RED}<->{Fore.RESET}{Fore.CYAN}->{Fore.RESET} WGET {Fore.CYAN}<-{Fore.RESET}{Fore.RED}<->{Fore.RESET}{Fore.CYAN}->{Fore.RESET} {Fore.CYAN}<RUNNING>{Fore.RESET} Getting info from {arg}.")
				s = wget.download(arg)
				print(f"'{s}' has been downloaded.")
			except Exception as e:
				print("Error : " + str(e))
			continue

		elif 'help' in command:
			m = f''
			for cmd, desc in helpc.items():
				m += f" {Fore.CYAN}<-{Fore.RESET}{Fore.RED}<->{Fore.RESET}{Fore.CYAN}->{Fore.RESET} {cmd.ljust(20)} - {desc}\n"
			print(m)
			continue

		elif command == 'cp':
			try:
				clipboard.copy(__file__)
				print(f"Copied '{__file__}' to clipboard")
			except Exception as e:
				print(e)
				raise e
			continue
		else:
			try:
				arg = command.replace(command, '')
				r = Misc.out(command)
				if "internal or external" in str(r):
					print(f"'{command}' is not a internal nor a external command...")
				else:
					if r == None:
						print()
					else:
						print(r)
				continue
			except Exception as e:
				print(e)
				raise e
	except KeyboardInterrupt:
		exit()
