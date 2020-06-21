# importing required libraries
from User import user
import os

count = 0

class NewUser(user):
    def __init__(self,name):
        self.name=name


    def saveMFCC(self):
        global count
        count=0
        if os.getcwd().endswith("PeaktoPeak"):
            if not os.path.exists("VoiceSamples"):
                os.mkdir("VoiceSamples")
            os.chdir("VoiceSamples")
            if not os.path.exists(self.name):
                os.mkdir(self.name)
            for file in os.listdir(self.name):
                if file.endswith('.txt'):
                    count+=1
            os.chdir(self.name)
            self.record_sample(self.name,count+1)
            os.chdir("..")
            os.chdir("..")
        else:
            print("Folder not found.\n")
