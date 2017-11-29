# Developer : Hamdy Abou El Anein

from easygui import *
import sys
import os




def su():
    os.popen("sudo -S %s" % (su), 'w').write('fieldValues\n')



def update():
    os.system("apt-get -y update")

def upgrade():
    os.system("apt-get -y upgrade")

def distUpgrade():
    os.system("apt-get -y dist-upgrade")

def startUpdate():
    msg = "What do you want to do ?"
    choices = ["1 Update", "2 Upgrade", "3 Dist-upgrade"]
    reply = buttonbox(msg, choices=choices)
    if reply == "1 Update":
        update()
    elif reply == "2 Upgrade":

        upgrade()
    elif reply == "3 Dist-upgrade":
        distUpgrade()
    else:
        sys.exit(0)




startUpdate()
#msg = "Enter the root password"
#title = "Root Password"
#fieldValues = passwordbox(msg, title)

#startUpdate()

#if not fieldValues:
#    sys.exit(0)