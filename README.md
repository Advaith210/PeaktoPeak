# Speaker Recognition using MFCC and DTW
## PeaktoPeak


This project contains a speaker recognition system using MFCC and DTW.

## Dependencies
* Any Linux Distro
* Python3.6 or above
* Librosa
* Numpy
* Scipy
* Pyaudio
* Appjar

## Usage
### Method 1
1. Open the terminal in the PeaktoPeak folder.
2. Type the following command "chmod +x cover.py".
3. Now click the cover.py icon to start the program.

### Method 2
1. Open the terminal in the PeaktoPeak folder.
2. Type the following command "python3 cover.py".
3. The program starts running now.

# Precaution
A library called numba got a new update in this month. It deleted some of the files present in the previous version. This caused librosa to crash as it has dependencies on the files that got deleted. So for those who want to run it, we suggest you to install numba version 0.48 after insalling librosa so that the new version of numba will be replaced by the previous version.
