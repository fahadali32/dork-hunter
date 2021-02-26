#!/usr/bin/python
import os
import sys
import time
from base64 import b16decode 
from base64 import b16encode 
from os import linesep as endl

banner = ("""
    #  ▓█████▄  ▒█████   ██▀███   ██ ▄█▀    ██░ ██  █    ██  ███▄    █ ▄▄▄█████▓▓█████  ██▀███
    #  ▒██▀ ██▌▒██▒  ██▒▓██ ▒ ██▒ ██▄█▒    ▓██░ ██▒ ██  ▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒
    #  ░██   █▌▒██░  ██▒▓██ ░▄█ ▒▓███▄░    ▒██▀▀██░▓██  ▒██░▓██  ▀█ ██▒▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒
    #  ░▓█▄   ▌▒██   ██░▒██▀▀█▄  ▓██ █▄    ░▓█ ░██ ▓▓█  ░██░▓██▒  ▐▌██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄
    #  ░▒████▓ ░ ████▓▒░░██▓ ▒██▒▒██▒ █▄   ░▓█▒░██▓▒▒█████▓ ▒██░   ▓██░  ▒██▒ ░ ░▒████▒░██▓ ▒██▒
    #   ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░▒ ▒▒ ▓▒    ▒ ░░▒░▒░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒   ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░
    #   ░ ▒  ▒   ░ ▒ ▒░   ░▒ ░ ▒░░ ░▒ ▒░    ▒ ░▒░ ░░░▒░ ░ ░ ░ ░░   ░ ▒░    ░     ░ ░  ░  ░▒ ░ ▒░
    #   ░ ░  ░ ░ ░ ░ ▒    ░░   ░ ░ ░░ ░     ░  ░░ ░ ░░░ ░ ░    ░   ░ ░   ░         ░     ░░   ░
    #     ░        ░ ░     ░     ░  ░       ░  ░  ░   ░              ░             ░  ░   ░
    #   ░
    version 1.0
""")
for ban in banner:
     print("\033[1;34;40m"+ban,end="")

print("\033[0;37;40m",end="")

#author
author = ("""
        Author:Fahad Ali
        Github:https://github.com/fahadali32
        Facebook:https://www.facebook.com/i.me.fahad.ali
        Email:fahad288ali@gmail.com
        
""")

for show in author:
    print("\033[1;32;40m"+show,end="")
    sys.stdout.flush()
    time.sleep(0.025)     
print("\033[0;37;40m",endl)

#working code
try:
    from googlesearch import search 
except ImportError: 
    print("Module is not installed") 
    os.system('pip install googlesearch && python scan.py')
query = input("type here query: ")
how_many = int(input("How many u wants to see: "))
i = 0
last = []
for j in search(query, tld="com", lang="en", num=int(how_many), start=0, stop=int(how_many), pause=2): 
    i += 1
    last.append(j)
    print(str(i)+":"+j+"\n\n")

# taking answer
ans = str(input("Do you wana save that data into text file:(ex:y/n) "))
take = ans.lower()
if take == "y":
    file_name = input("File Name(Ex:Data): ")
    for i in last:
        f = open(file_name+".txt","a")
        f.write(i+"\n")
        f.close()
    else:
        exit();
