import numpy as np
import librosa as lb
import os
import wave
import struct
import pyaudio
import User as nu
from scipy.stats import linregress

compareroot = 'VoiceSamples'

Output = ""

def compare_samples():
    global Output
    try:
        Output = ""
        a = nu.user()
        a.record_sample("temp",0)
        cost = 80
        flag=""
        MFCCout = np.loadtxt("temp0.txt")
        for folder in os.listdir(compareroot):
            for file in os.listdir(compareroot+"/"+folder):
                MFCCin = np.loadtxt(compareroot+"/"+folder+"/" +file)
                if (len(MFCCout[0])>len(MFCCin[0])):
                    inp1 = MFCCin
                    inp2 = MFCCout
                else:
                    inp1 = MFCCout
                    inp2 = MFCCin
                D,wp = lb.sequence.dtw(inp1,inp2,subseq = True)
                bestcost = D[wp[-1,0],wp[-1,-1]]
                slope = linregress(wp[:,1],wp[:,0])
                if slope[0]>0.75 and slope[0]<1.25:
                    if bestcost<cost:
                        cost = bestcost
                        slope1 = slope[0]
                        flag=folder
        if cost == 80:
            print("sorry,no user matched")
            Output = "No one"
        else:
            Output = flag
            print("The voice matched to {}".format(flag))
            print("bestcost={}".format(cost))
            print("slope={}".format(slope1))
            print(Output)
    except FileNotFoundError:
        print("file not found")
    if os.path.exists('temp0.txt'):
        os.remove('temp0.txt')
