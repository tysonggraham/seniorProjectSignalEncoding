import math
import wave
import struct
import pyaudio

#This has something to do with the duration of each character we express in the signal.
data_size = 11400 # duration each freqency is emitted for each character
fname = "WaveTest.wav" # Filename
frate = 11025.0  # framerate as a float
amp = 8000.0     # multiplier for amplitude
#TODO: Make this a prompt for input
userInput = 'Hello, World!'
# userInput = input('Please enter your message: \n')

sine_list_x = []
durationStart = 0;

for letter in userInput:

	cap = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '{', '}', '|', ':', '"', '<', '>', '?']
	low = ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', '[', ']', '\', ';', '/'', ',','.', '/']

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
		'a' : 16000,
		'b' : 15750,
		'c' : 15500,
		'd' : 15250,
		'e' : 15000,
		'f' : 14750,
		'g' : 14500,
		'h' : 14250,
		'i' : 14000,
		'j' : 13750,
		'k' : 13500,
		'l' : 13250,
		'm' : 13000,
		'n' : 12750,
		'o' : 12500,
		'p' : 12250,
		'q' : 12000,
		'r' : 11750,
		's' : 11500,
		't' : 11250,
		'u' : 11000,
		'v' : 10750,
		'w' : 10500,
		'x' : 10250,
		'y' : 10000,
		'z' : 9750,
		'1' : 9500,
		'2' : 9250,
		'3' : 9000,
		'4' : 8750,
		'5' : 8500,
		'6' : 8250,
		'7' : 8000,
		'8' : 7750,
		'9' : 7500,
		'0' : 7250,
		'-' : 7000,
		'=' : 6750,
		'[' : 6500,
		']' : 6250,
		'\\' : 6000,
		';' : 5750,
		'\'' : 5500,
		',' : 5250,
		'.' : 5000,
		'/' : 4750,
	}
	#This is to test what frequency we assigned for each character. The default case is 4500 which is for the space
	#print (freq.get(letter, 4500))
	durationEnd = durationStart + duration
	#print ('duration End = ' + str(durationEnd))
	#This is where we add each frequency to the list to be emitted
	for x in range(durationStart, durationEnd):
		sine_list_x.append(math.sin(2*math.pi*freq.get(letter, 4500)*(x/frate)))
	durationStart = durationEnd;
print (sine_list_x)
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
