# Developer : Hamdy Abou El Anein

from easygui import *
import sys
import os

image = "./images/update.gif"

#def su():
#    os.system("sudo -S su root | echo Password")
#    startUpdate()

def everything():
    os.system("sudo -i apt-get -y update && sudo -i apt-get -y upgrade && sudo -i apt-get -y dist-upgrade && sudo -i apt-get -y autoremove ")
    startUpdate()

def autoremove():
    os.system("sudo -i apt-get -y autoremove")
    startUpdate()

def autoclean():
    os.system("sudo -i apt-get -y autoclean")
    startUpdate()

def update():
    os.system("sudo -i apt-get -y update")
    startUpdate()

def upgrade():
    os.system("sudo -i apt-get -y upgrade")
    startUpdate()

def distUpgrade():
    os.system("sudo -i apt-get -y dist-upgrade")
    startUpdate()

def startUpdate():
    img= image
    title= "DaylightUpdater"
    msg = "This software only work as root or with a sudoer user.\n\n\n\nWhat do you want to do ?"
    choices = ["Everything in one time","1 Update", "2 Upgrade", "3 Dist-upgrade", "4 Autoclean", "5 Autoremove", "6 Exit"]
    reply = buttonbox(msg,image=img,choices=choices,title=title)
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
 #   elif reply == "Become Root":
  #       su()
    else:
        sys.exit(0)


startUpdate()

