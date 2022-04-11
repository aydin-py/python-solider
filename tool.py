#from colorama import Fore, init
from dataclasses import replace
from colorama import *
from tkinter import *
import time
import socket
import sys
import requests
import os

init()

print("\n")
print(Style.BRIGHT+ Fore.GREEN+"    [!] Wellcome to the Cyber1400 first Python tool. [!]")
print(Fore.WHITE + "\n""                  \32",Fore.CYAN+"Cyber1400.epyzi.com",Fore.WHITE+"\33")
print("\n")
adminpanel = print(Fore.YELLOW + "   [1] Find the websites admin panel.")
wordtext = print(Fore.YELLOW + "   [2] Find the words in long texts.")
csddos = print(Fore.YELLOW + "   [3] Find sites IP.")
IRclock = print(Fore.YELLOW + "   [4] Display world clock graphically.")



YELLOW = "\x1b[1;33;40m" 
RED = "\x1b[1;31;40m"


print("\n")
print("\n")
print(f"{RED}   [+] Enter your tool number : ")
tournament = input()
# -------------------------------------------------------------------------------

            #tool 1 (graphically clock)

if tournament == "1":

    print("\n")
    print(Fore.LIGHTRED_EX+"          [!]--Find Admin Panel--[!]")
    print("\n")
    mylist = ["admin123","admin","wp-admin"]
    sitename = input("   [+] Enter your site URL : ")
    
    if "www" in sitename :
            x = sitename.replace("www.","https://")
             #print(sitename.replace("www.","https://"),http = requests.get(sitename+"/"+ i ).status_code+print(i+" : "+str(http)))
            for i in mylist:
                http = requests.get(x + "/"+i).status_code
                print(i+" : "+str(http))
               
    for i in mylist :
            http = requests.get(sitename+"/"+ i).status_code
            print("\n"+"   "+i + " : "+str(http))
            
# -------------------------------------------------------------------------------

            # tool 2
            
if tournament == "2" :
    print("\n")
    print(Fore.MAGENTA + "          [!]--Text finding--[!]")
    print("\n")
    text = input("  [+] Enter your text: ")
    word = input("  [+] Enter your word for finding :")
    print("\n")
    if word in text:
        print(Fore.GREEN+"   ["+"\1"+"]"+"\7"" in kalame "+ "[" +word + "]"+" vojood darad :)")
        #print(text.count(word))

    if word not in text:
        print(Fore.RED+"   [!]"+"\7\7"" sharmande.in kalame vojood nadarad :(")

# -------------------------------------------------------------------------------

            # tool 3
            
if tournament == "3":
    print("\n")
    print(Fore.LIGHTBLUE_EX+"          [!]--Find sites IP--[!]")
    print("\n")
    site = input("   [+] Enter site URL : ")
    print("\n")
    ip = socket.gethostbyname(site)
    print(Fore.LIGHTBLUE_EX+"   [!]"+Fore.LIGHTCYAN_EX+" This site IP : "+Fore.LIGHTWHITE_EX+ip)
    
# -------------------------------------------------------------------------------

            # tool 4
if tournament == "4" :
    # def myclock():


        root = Tk()
        root.title("Clock")
        width = 510
        height = 270
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width/3)- (width/2)
        y = (screen_height/2)- (height/2)
        root.geometry("%dx%d+%d+%d" % (width, height, x, y))
#root.resizable(0, 0)
        root.config(bg="black")
        def tick():

            setTime=time.strftime('%I: %M: %S')
            clock.config(text=setTime)
            clock.after(200,tick)
        Top = Frame(root, width=1000, bd=1, relief=SOLID)
        Top.pack(side=TOP)
        Mid = Frame(root, width=1000)
        Mid.pack(side=TOP, expand=1)
        lbl_title = Label(Top, text="Cyber1400", width=1000, font=("Arial Black", 20))

        lbl_title.pack(fill=X)


        clock= Label(Mid, font=('BAUHS93.TTF', 65 , 'bold'), fg="red", bg="black")
        clock.pack()
        if __name__=='__main__':
            tick()
            root.mainloop()

    

# while True :
#     pass
