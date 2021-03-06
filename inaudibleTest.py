import math
import wave
import struct
import pyaudio
import sys

##################################################################
# RATE / CHUNK * Record_seconds = number of seconds in recording?
##################################################################

# Filename
fname = "WaveTest.wav";
# framerate as a float (also referred to as frequency rate or sample rate)
frate = 48000.0;
# integer of frate data_size and fequency are the same so duration of each char rep is 1 second
data_size = int(frate*1.003);
amp = 40000.0;     # multiplier for amplitude (Is any of this lost when transfering through FFT?)
userInput = sys.argv[1] if (len(sys.argv) > 1) else input('Please enter your message: \n');
#this is calculated by frate/desired step_size or difference in hz from each character representation.
#this should be a power of 2 close to it
CHUNK = 32 	# Is this a correct assumption? Should we modify the chunk size?
step_size = 202
#uppercase characters array
cap = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '{', '}', '|', ':', '"', '<', '>', '?'];
#lowercase characters array
low = ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', '[', ']', '\\', ';', '\'', ',','.', '/'];

# Each character is assigned a frequency in hz here.
enum = {
	'0' : 0,
	'1' : 1,
	'2' : 2,
	'3' : 3,
	'4' : 4,
	'5' : 5,
	'6' : 6,
	'7' : 7,
	'8' : 8,
	'9' : 9
}

sine_list_x = [];
durationStart = 0;

for letter in userInput:
	if letter.isupper(): #if it is an uppercase letter
		duration = 4;    #set char reps duration to 3 secs

		# Lowercase the letter
		letter = letter.lower() 
	elif (letter in cap):	#or if it is in the caps array
		duration = 4;    #set char reps duration to 3 secs
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
	print (((enum.get(letter, 10) + 1) * step_size) + 18000)
	for x in range(durationStart * data_size, durationEnd * data_size):
		sine_list_x.append(math.sin(2*math.pi*(((enum.get(letter, 10) + 1) * step_size)+18000)*(x/frate))) ####
	durationStart = durationEnd;

#############################################################################
# This is where we write to the file.
#############################################################################
wav_file = wave.open(fname, 'w')
'''WAVE FILE PARAMETERS'''
#This should make it mono
nchannels = 1
sampwidth = 2 #width of each sample in bytes. # How is this different from CHUNK?
				# Python and Matlab seem to call this CHUNK, why is wav calling it sample width?
framerate = int(frate) #TODO think about deleting and replacing with data_width or frate. They all share same value
nframes = data_size #TODO think about replacing with data_size. May keep for clarity.
comptype = "NONE"
compname = "not compressed"

wav_file.setparams((nchannels, sampwidth, framerate, nframes,
    comptype, compname))

for s in sine_list_x:
    # write the audio frames to file

    wav_file.writeframes(struct.pack('h', int(s*amp/2)))	# Why is amplitude divided by 2?

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

data = wf.readframes(CHUNK)	# Is there a specific reason we are reading the file in CHUNKs? Could this be anything?

while data != '':
    stream.write(data)
    data = wf.readframes(CHUNK)

stream.stop_stream()
stream.close()

p.terminate()