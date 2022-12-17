import pytube
import sys      
from time import sleep  

link = input('\033[33m' + "Paste Video Link here: " + '\033[0m').strip()
yt = pytube.YouTube(link)

if(yt.check_availability()):
    print('\033[31m' + "SORRY ! VIDEO NOT FOUND" + '\033[0m')
    sleep(8)
    exit()
else:
    print('\033[32m' + "VIDEO FOUND !")
    print('\033[0m' + yt.title)
    print('\033[36m' + str(yt.views) + " Views")
    if(input('\033[33m' + "Do you want to download : y/n : " + '\033[0m').strip().lower()=="y"):
        print('\033[32m' + "Downloading..." + '\033[0m')
        yt.streams.get_highest_resolution().download()
        print('\033[32m' + "Download Completed!" + '\033[0m')
    sleep(8)
    exit()
