#Importing all required libraries
import numpy as np
import librosa as lb
import os
import wave
import struct
import pyaudio
#global variables used in this module
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 48000
CHUNK = 1024
RECORD_SECONDS = 2

flag = None

class user():
	def record(self,output_filename,delay=0):
		"""This function records the audio using the available ports and writes it to the output_filename.
		The delay is a parameter which delays the recording message and captures the surrounding amount of time.
		WARNING:- Give the filename without any extension like .wav or .mp3 as the function automatically assigns it as .wav file"""
		if not (output_filename.endswith(".wav")):
			output_filename = output_filename +".wav"
		audio = pyaudio.PyAudio()
		#start recording
		stream = audio.open(format = FORMAT, channels = CHANNELS,rate = RATE,input = True,frames_per_buffer=CHUNK)
		frames=[]
		value1 = int(RATE / CHUNK * (RECORD_SECONDS+delay))
		if delay == 0:
			value2 = 0
		else:
			value2 = int(RATE / CHUNK * delay)
		for i in range(0, value1):
			data = stream.read(CHUNK)
			frames.append(data)
			if i == value2:
				print("Recording")
		print("Finish Recording")
		# stop Recording
		stream.stop_stream()
		stream.close()
		audio.terminate()
		waveFile = wave.open(output_filename, 'wb')
		waveFile.setnchannels(CHANNELS)
		waveFile.setsampwidth(audio.get_sample_size(FORMAT))
		waveFile.setframerate(RATE)
		waveFile.writeframes(b''.join(frames))
		waveFile.close()

	def silent_noise_removal(self,input_array,framelength=15000,topdb=4):
		"""This function finds the end points of the isolated word and trims the remaining part."""
		Yt = lb.effects.trim(input_array,frame_length=framelength, top_db=topdb)
		return Yt[0]


	def record_sample(self,name,sample_number):
		"""This function records the voice sample and does the preprocessing work.
		It first removes all the trailing silences and detects the isolated word.
		Then it extracts the mfcc of the new array and saves it as a .txt file.
		Finally it deletes the .wav file from the folder."""
		global flag
		flag=0
		name1 = name + str(sample_number)
		self.record(name1,2)
		A,s = lb.core.load(name1+".wav")
		Yt = self.silent_noise_removal(A[10000:])
		#plot(A,Yt)
		if len(Yt) > (len(A)-s*2) :
			print("\nRecorded voice is not clear.\nPlease record it again.\n")
			flag=1
			
		else:
			MFCC = lb.feature.mfcc(Yt,n_mfcc=40)
			np.savetxt(name1+".txt",MFCC)
		os.remove(name1+".wav")
