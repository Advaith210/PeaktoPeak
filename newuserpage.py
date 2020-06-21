from appJar import gui
from time import sleep
import numpy as np
import sys
import os
abspath = os.getcwd()
sys.path.insert(1,os.path.join(abspath,'Backend'))
from NewUser import NewUser as nu
import User as u


count=0
sampcount = 0

def submitname():
	if app.getEntry("Name") != "":
		with open("temp.txt","w") as f:
			f.write(app.getEntry("Name"))
		app.showLabel('l1')
		app.showLabel('sampcount')
		app.showLabel('VoiceStat')
		app.showButton('record')
		app.disableButton('Submit')

def status():
	sleep(0.2)
	app.setLabel("l1","Loading...")
	sleep(2)
	app.setLabel("l1","recording")
	sleep(2)
	app.setLabel("l1","Finished recording")
	sleep(1)




def rowfill(i,j,n):
	global count
	app.addLabel(str(count),"",row=i,column=j,colspan=n)
	app.hideLabel(str(count))
	count+=1

def record1(name):
	A = nu(name)
	A.saveMFCC()
	del A

def sampnumber(name):
	global sampcount
	if not os.path.exists("VoiceSamples"):
		os.mkdir('VoiceSamples')
	os.chdir("VoiceSamples")
	sampcount=0
	if not os.path.exists(name):
		os.mkdir(name)
	for file in os.listdir(name):
		if file.endswith('.txt'):
			sampcount+=1
	os.chdir("..")
	app.setLabel("sampcount","Sample "+str(sampcount+1))

def voicestatupdate():
	sleep(6)
	if u.flag == 0:
		app.setLabel("VoiceStat","Voice collected")
	if u.flag == 1:
		app.setLabel("VoiceStat","Please record again")


def recordbutton():
	global i
	with open("temp.txt") as f:
		name = f.read()
	if name != "":
		sampnumber(name)
		app.thread(record1,name)
		app.thread(status)
		app.thread(voicestatupdate)

app = gui("NewUser","720x480")
app.setIcon('logo.gif')
app.setBg('aquamarine')
app.warningBox("warning","Please fill in the name in the entry widget in a single word.\n\nRecord atleast 5 samples for better accuracy.")
rowfill(1,0,2)
app.addLabelEntry("Name",row=1,column=2,colspan=2)
rowfill(1,4,2)
rowfill(2,0,2)
app.button("Submit",submitname,row=2,column=2,colspan=2)
rowfill(2,4,2)

rowfill(3,0,2)
app.addLabel("sampcount","",row=3,column=2,colspan=2)
app.setLabelBg("sampcount","spring green")
rowfill(3,4,2)

rowfill(4,0,2)
app.addLabel("l1","",row=4,column=2,colspan=2)
app.setLabelBg("l1","turquoise")
rowfill(4,4,2)
rowfill(5,0,2)
app.button("record",recordbutton,row=5,column=2,colspan=2)
rowfill(5,4,2)
rowfill(6,0,1)
app.addLabel("VoiceStat","",row=6,column=1,colspan=4)
app.setLabelBg("VoiceStat","aquamarine")
rowfill(6,5,1)
rowfill(7,0,6)
app.hideLabel('l1')
app.hideLabel('sampcount')
app.hideLabel('VoiceStat')
app.hideButton('record')
app.go()
