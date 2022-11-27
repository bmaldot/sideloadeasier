#hi
import os
from os import system
from colorama import Fore

wc=os.getcwd()

def clc():
    os.system("clear")

def check():
    initchec=system('which adb')
    clc()
    if initchec != 0: 
        print(f'install adb first!\n{Fore.LIGHTBLACK_EX}archlinux: pacman -S android-tools\ndebian: apt-get install android-tools{Fore.RESET}')
        exit()
    return initchec

def check2():
    if len(url) == 0:
        print(f"{Fore.RED}please input a url!{Fore.RESET}")
        exit()

def __init__():
    print('put the url of the download')
    inp=input('here: ')
    return inp

url=__init__()

def install():
    print('obtaining the archive...')
    system('wget '+url)
    directorios=os.listdir(wc)
    fileext1= r".zip"
    directiosbuenos = [_ for _ in directorios if _.endswith(fileext1)]
    print(f'{directiosbuenos}')
    if len(directiosbuenos) != 0:
        update=directiosbuenos[0]
        print('installing it')
        os.system('adb sideload '+update)
        print('cleaning...')
        os.system('rm '+update)
    else:
        print(f'{Fore.RED}Put a valid url!\n{Fore.LIGHTBLACK_EX}your actual url was {url}{Fore.RESET}')

##execution of the code

check()
check2()
install()
print(Fore.GREEN+'updated!'+Fore.RESET)





