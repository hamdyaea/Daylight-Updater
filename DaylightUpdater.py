# Developer : Hamdy Abou El Anein

from easygui import *
import sys
import os


def su():
    os.popen("sudo -S %s" % (su), 'w').write('fieldValues\n')

def clean():
    os.system("apt-get -y clean")
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
    msg = "This software only work as root or with a sudoer user. \n\nWhat do you want to do ?"
    choices = ["1 Update", "2 Upgrade", "3 Dist-upgrade", "4 Autoclean", "5 Clean", "6 Exit"]
    reply = buttonbox(msg, choices=choices)
    if reply == "1 Update":
        update()
    elif reply == "2 Upgrade":

        upgrade()
    elif reply == "3 Dist-upgrade":
        distUpgrade()
    elif reply == "4 Autoclean":
        autoclean()
    elif reply == "5 Clean":
        clean()
    elif reply == "6 Exit":
        sys.exit(0)
    else:
        sys.exit(0)




startUpdate()
#msg = "Enter the root password"
#title = "Root Password"
#fieldValues = passwordbox(msg, title)

#startUpdate()

#if not fieldValues:
#    sys.exit(0)