from appJar import gui
import os
import sys
abspath = os.getcwd()
path = os.path.join(abspath,"info","about_project.txt")
with open(path) as f:
    information = f.read()


app = gui("Project Documentation","720x520")
app.setIcon('logo.gif')
app.setBg('light cyan')
app.startScrollPane("s1")
app.addMessage("m1",information)
app.stopScrollPane()
app.go()
