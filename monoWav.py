import math
import wave
import struct
import sys

# Filename
fname = "WaveTest.wav";
# framerate as a float (also referred to as frequency rate or sample rate)
frame_rate = 48000.0; 
# integer of int(frame_rate) int(frame_rate) and fequency are the same so duration of each char rep is 1 second
#int(frame_rate) = int(int(frame_rate)); 
amp = 10000.0;     # multiplier for amplitude (Is any of this lost when transfering through FFT?)
userInput = sys.argv[1] if (len(sys.argv) > 1) else input('Please enter your message: \n');
#this is calculated by int(frame_rate)/desired step_size or difference in hz from each character representation.
#this should be a power of 2 close to it
step_size = 100;
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
	'`' : 26,
	'1' : 27,
	'2' : 28,
	'3' : 29,
	'4' : 30,
	'5' : 31,
	'6' : 32,
	'7' : 33,
	'8' : 34,
	'9' : 35,
	'0' : 36,
	'-' : 37,
	'=' : 38,
	'[' : 39,
	']' : 40,
	'\\' : 41,
	';' : 42,
	'\'' : 43,
	',' : 44,
	'.' : 45,
	'/' : 46,
}

sine_list_x = []
duration_start = 0;

for letter in userInput:
	if letter.isupper():
		duration = 4;
		letter = letter.lower() 
	elif (letter in cap):
		duration = 4;
		letter = low[cap.index(letter)];
	else:
		duration = 1;
	duration_end = duration_start + duration
	#This is where we add each frequency to the list to be emitted
	print ((enum.get(letter, 47) + 1) * step_size)
	for x in range(duration_start * int(frame_rate), duration_end * int(frame_rate)):
		sine_list_x.append(math.sin(2*math.pi*((enum.get(letter, 47) + 1) * step_size + 22000)*(x/int(frame_rate)))) ####
	duration_start = duration_end;

#############################################################################
# This is where we write to the file.
#############################################################################
wav_file = wave.open(fname, 'w')
#This should make it mono
nchannels = 1
sampwidth = 2   #width of each sample in bytes.
nframes = int(frame_rate) * duration_end#TODO think about replacing with int(frame_rate). May keep for clarity.
comptype = "NONE"
compname = "not compressed"
wav_file.setparams((nchannels, sampwidth, int(frame_rate), nframes, comptype, compname))

for s in sine_list_x:
    # write the audio frames to file
    wav_file.writeframes(struct.pack('h', int(s*amp/2)))
wav_file.close()