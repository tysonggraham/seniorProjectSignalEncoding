import math
import wave
import struct
import pyaudio
import sys


fname = "WaveTest.wav"; # Filename
frate = 5000.0; # framerate as a float (also referred to as frequency rate or sample rate)
data_size = int(frate); # integer of frate data_size and fequency are the same so duration of each char rep is 1 second
amp = 20000.0;     # multiplier for amplitude
userInput = sys.argv[1] if (len(sys.argv) > 1) else input('Please enter your message: \n');
CHUNK = 32; #this is calculated by frate/desired step_size or difference in hz from each character representation.
step_size = frate/CHUNK;
#uppercase characters array
cap = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '{', '}', '|', ':', '"', '<', '>', '?'];
#lowercase characters array
low = ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', '[', ']', '\\', ';', '\'', ',','.', '/'];

# Each character is assigned a frequency in hz here.
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

sine_list_x = []
durationStart = 0;

for letter in userInput:
	if letter.isupper(): #if it is an uppercase letter
		duration = 3;    #set char reps duration to 3 secs

		# Lowercase the letter
		letter = letter.lower() 
	elif (letter in cap):	#or if it is in the caps array
		duration = 3;    #set char reps duration to 3 secs

		# Find where letter is in cap
		# Set letter to that location in lower
		letter = low[cap.index(letter)];
	else:
		duration = 1;    #set char reps duration to 1 sec
		
	#This is to test what frequency we assigned for each character. The default case is 4500 which is for the space
	#print (freq.get(letter, 4500))
	durationEnd = durationStart + duration
	#print ('duration End = ' + str(durationEnd))
	#This is where we add each frequency to the list to be emitted
	print ((enum.get(letter, 46) + 1) * step_size)
	for x in range(durationStart * data_size, durationEnd * data_size):
		sine_list_x.append(math.sin(2*math.pi*((enum.get(letter, 46) + 1) * step_size)*(x/frate)))
	durationStart = durationEnd;

#############################################################################
# This is where we write to the file.
#############################################################################
wav_file = wave.open(fname, 'w')
#This should make it mono
nchannels = 1
sampwidth = 2 #width of each sample in bytes.
framerate = int(frate) #TODO think about deleting and replacing with data_width or frate. They all share same value
nframes = data_size #TODO think about replacing with data_size. May keep for clarity.
comptype = "NONE"
compname = "not compressed"

wav_file.setparams((nchannels, sampwidth, framerate, nframes,
    comptype, compname))

for s in sine_list_x:
    # write the audio frames to file
    wav_file.writeframes(struct.pack('h', int(s*amp/2)))

wav_file.close()


#############################################################################
# This is where we play the file we just wrote.
#############################################################################
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
