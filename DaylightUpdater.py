# Developer : Hamdy Abou El Anein

from easygui import *
import sys
import os

image = "./images/update.gif"

def su():
    startUpdate()
    os.system("sudo su")

def everything():
    os.system("apt-get -y update && sudo apt-get -y upgrade && sudo apt-get -y dist-upgrade && sudo apt-get -y autoremove ")
    startUpdate()

def autoremove():
    os.system("apt-get -y autoremove")
    startUpdate()

def autoclean():
    os.system("apt-get -y autoclean")
    startUpdate()

def update():
    os.system("apt-get -y update")
    startUpdate()

def upgrade():
    os.system("apt-get -y upgrade")
    startUpdate()

def distUpgrade():
    os.system("apt-get -y dist-upgrade")
    startUpdate()

def startUpdate():
    img= image
    title= "DaylightUpdater"
    msg = "This software only work as root or with a sudoer user.\n\nClick on Become Root and enter the Root password in the terminal if asked.\n\nWhat do you want to do ?"
    choices = ["Become Root","Everything in one time","1 Update", "2 Upgrade", "3 Dist-upgrade", "4 Autoclean", "5 Autoremove", "6 Exit"]
    reply = buttonbox(msg,image=img,choices=choices)
    if reply == "1 Update":
        update()
    elif reply == "2 Upgrade":

        upgrade()
    elif reply == "3 Dist-upgrade":
        distUpgrade()
    elif reply == "4 Autoclean":
        autoclean()
    elif reply == "5 Autoremove":
        autoremove()
    elif reply == "6 Exit":
        sys.exit(0)
    elif reply == "Everything in one time":
        everything()
    elif reply == "Become Root":
        su()
    else:
        sys.exit(0)


startUpdate()

