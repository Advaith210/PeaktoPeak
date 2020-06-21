from appJar import gui
from time import sleep
import numpy as np
import sys
import os
abspath = os.getcwd()
sys.path.insert(1,os.path.join(abspath,'Backend'))
import compare as cm
import User as u
count=0

def rowfill(i,j,n):
    global count
    app.addEmptyLabel(str(count),row=i,column=j,colspan=n)
    count+=1

def none():
    pass

def status():
	sleep(0.2)
	app.setLabel("RecordStatus","Loading...")
	sleep(2)
	app.setLabel("RecordStatus","recording")
	sleep(2)
	app.setLabel("RecordStatus","Finished recording")
	sleep(1)

def compare():
    cm.compare_samples()

def voicestatupdate():
    sleep(6)
    if u.flag == 0:
        app.setLabel("RecordStatus","Voice collected")
        if cm.Output == "No one":
            app.setLabel("output","Sorry, no user matched.")
        elif cm.Output == "":
            app.setLabel("output","No user registered.")
        else:
            app.setLabel("output","Voice matched with {}.".format(cm.Output))
        sleep(2)
        app.setLabel("output","")
    if u.flag == 1:
        app.setLabel("RecordStatus","Please record again")


def compare_button():
    app.thread(compare)
    app.thread(status)
    app.thread(voicestatupdate)
app = gui("Compare Voice","720x480")
app.setIcon("logo.gif")
app.setBg("light green")
rowfill(0,0,0)
app.addLabel("info","Press Record to recognize speaker.",row=0,column=1,colspan=4)
app.setLabelFont(weight="bold")
rowfill(0,5,0)
rowfill(1,0,2)
app.addLabel("RecordStatus","",row=1,column=2,colspan=2)
app.setLabelBg("RecordStatus","cyan")
app.setLabelFg("RecordStatus","orange")
rowfill(1,4,2)
rowfill(2,0,2)
app.addButton("Record",compare_button,row=2,column=2,colspan=2)
app.setButtonWidth("Record",15)
app.setButtonHeight("Record",1)
rowfill(2,4,2)
rowfill(3,0,6)
rowfill(4,0,6)
app.addLabel("output","",row=5,column=0,colspan=6)
app.setLabelBg("output","light green")
rowfill(6,0,6)
app.go()
