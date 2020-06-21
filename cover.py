#!/usr/bin/env python3

from appJar import gui
#from UserVoice import newuser as nu
import os
def none():
    pass

def newUserWindow():
    app.hide()
    os.system("python3 newuserpage.py")
    app.show()

def aboutproject():
    app.hide()
    os.system("python3 abouttheproject.py")
    app.show()

def aboutus():
    app.hide()
    os.system("python3 aboutus.py")
    app.show()

def comparepage():
    app.hide()
    os.system("python3 comparepage.py")
    app.show()



def quit():
    if os.path.exists("temp.txt"):
        os.remove("temp.txt")
    if os.path.exists("temp0.txt"):
        os.remove("temp0.txt")
    app.stop()

text="TEXT BASED SPEAKER RECOGNITION USING MFCC"
app = gui("Text based Speaker Recognition","720x520")
app.setIcon('logo.gif')
app.setBgImage("Bg.gif")
app.setResizable(canResize=False)
tools=["About the project","About us"]
app.addToolbarButton(tools[0],aboutproject,findIcon=False)
app.addToolbarButton(tools[1],aboutus,findIcon=False)
app.setToolbarBg("RoyalBlue1")
app.addButton("New User",newUserWindow)
app.setButtonBg('New User','lawn green')
app.setButtonFg('New User','orange red')
app.addButton("Recognize Speaker",comparepage)
app.setButtonBg('Recognize Speaker','lawn green')
app.setButtonFg('Recognize Speaker','orange red')
app.addButton("Quit",quit)
app.setButtonBg('Quit','lawn green')
app.setButtonFg('Quit','orange red')




app.go()
