import math
import wave
import struct
import pyaudio
import sys

#This has something to do with the duration of each character we express in the signal.
data_size = 11400 # duration each freqency is emitted for each character
fname = "WaveTest.wav" # Filename
frate = 11025.0  # framerate as a float
amp = 10000.0     # multiplier for amplitude
#TODO: Make this a prompt for input
#userInput = 'Hello, World!'
userInput = sys.argv[1] if (len(sys.argv) > 1) else input('Please enter your message: \n')

#print (userInput)

sine_list_x = []
durationStart = 0;

for letter in userInput:

	cap = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '{', '}', '|', ':', '"', '<', '>', '?']
	low = ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', '[', ']', '\\', ';', '\'', ',','.', '/']

	if letter.isupper():
		duration = 2 * data_size

		# Lowercase the letter
		letter = letter.lower()
	elif (letter in cap):
		duration = 2 * data_size

		# Find where letter is in cap
		# Set letter to that location in lower
		letter = low[cap.index(letter)]
	else:
		duration = 1 * data_size
		
	# Each character is assigned a frequency here.
	freq = { 
		'a' : 350,
		'b' : 400,
		'c' : 450,
		'd' : 500,
		'e' : 550,
		'f' : 600,
		'g' : 650,
		'h' : 700,
		'i' : 750,
		'j' : 800,
		'k' : 850,
		'l' : 900,
		'm' : 950,
		'n' : 1000,
		'o' : 1050,
		'p' : 1100,
		'q' : 1150,
		'r' : 1200,
		's' : 1250,
		't' : 1300,
		'u' : 1350,
		'v' : 1400,
		'w' : 1450,
		'x' : 1500,
		'y' : 1550,
		'z' : 1600,
		'1' : 1650,
		'2' : 1700,
		'3' : 1750,
		'4' : 1800,
		'5' : 1850,
		'6' : 1900,
		'7' : 1950,
		'8' : 2000,
		'9' : 2050,
		'0' : 2100,
		'-' : 2150,
		'=' : 2200,
		'[' : 2250,
		']' : 2300,
		'\\' : 2350,
		';' : 2400,
		'\'' : 2450,
		',' : 2500,
		'.' : 2550,
		'/' : 2600,
	}
	#This is to test what frequency we assigned for each character. The default case is 4500 which is for the space
	#print (freq.get(letter, 4500))
	durationEnd = durationStart + duration
	#print ('duration End = ' + str(durationEnd))
	#This is where we add each frequency to the list to be emitted
	for x in range(durationStart, durationEnd):
		sine_list_x.append(math.sin(2*math.pi*freq.get(letter, 4500)*(x/frate)))
	durationStart = durationEnd;
#print (sine_list_x)
wav_file = wave.open(fname, 'w')
#This should make it mono
nchannels = 1
sampwidth = 2
framerate = int(frate)
nframes = data_size
comptype = "NONE"
compname = "not compressed"

wav_file.setparams((nchannels, sampwidth, framerate, nframes,
    comptype, compname))

for s in sine_list_x:
    # write the audio frames to file
    wav_file.writeframes(struct.pack('h', int(s*amp/2)))

wav_file.close()


CHUNK = 1024

wf = wave.open(fname, 'rb')

p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

data = wf.readframes(CHUNK)

while data != '':
    stream.write(data)
    data = wf.readframes(CHUNK)

stream.stop_stream()
stream.close()

p.terminate()
