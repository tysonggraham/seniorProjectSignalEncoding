import math
import wave
import struct
import pyaudio
import sys

#This has something to do with the duration of each character we express in the signal.
data_size = 11400 # duration each freqency is emitted for each character
fname = "WaveTest.wav" # Filename
frate = 11025.0  # framerate as a float
amp = 20000.0     # multiplier for amplitude
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
	enum = { 
		'a' : 0,
		'b' : 1,
		'c' : 2,
		'd' : 3,
		'e' : 4,
		'f' : 5,
		'g' : 6,
		'h' : 7,
		'i' : 8,
		'j' : 9,
		'k' : 10,
		'l' : 11,
		'm' : 12,
		'n' : 13,
		'o' : 14,
		'p' : 15,
		'q' : 16,
		'r' : 17,
		's' : 18,
		't' : 19,
		'u' : 20,
		'v' : 21,
		'w' : 22,
		'x' : 23,
		'y' : 24,
		'z' : 25,
		'1' : 26,
		'2' : 27,
		'3' : 28,
		'4' : 29,
		'5' : 30,
		'6' : 31,
		'7' : 32,
		'8' : 33,
		'9' : 34,
		'0' : 35,
		'-' : 36,
		'=' : 37,
		'[' : 38,
		']' : 39,
		'\\' : 40,
		';' : 41,
		'\'' : 42,
		',' : 43,
		'.' : 44,
		'/' : 45,
	}
	#This is to test what frequency we assigned for each character. The default case is 4500 which is for the space
	#print (freq.get(letter, 4500))
	durationEnd = durationStart + duration
	#print ('duration End = ' + str(durationEnd))
	#This is where we add each frequency to the list to be emitted
	print (enum.get(letter) * 50 + 300)
	for x in range(durationStart, durationEnd):
		sine_list_x.append(math.sin(2*math.pi*(enum.get(letter, 46) * 50 + 300)*(x/frate)))

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
