import math
import wave
import struct
import pyaudio

freq = 16000.0
freq2 = freq-1000
data_size = 40000
fname = "WaveTest.wav"
frate = 11025.0  # framerate as a float
amp = 8000.0     # multiplier for amplitude

cap = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '{', '}', '|', ':', '"', '<', '>', '?']
low = ['1', '2', '3', '4'] #TODO: FINISH

if x.isupper()
	duration = 2;

	# Lowercase the letter
	x = x.lower();
elif (x in cap)
	duration = 2;

	# Find where x is in cap
	# Set x to that location in lower
	x = low[cap.index(x)]
else
	duration = 1;

frequencies = { 
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

sine_list_x = []
for x in range(int(data_size/2)):
    sine_list_x.append(math.sin(2*math.pi*freq*(x/frate)))

for x in range(int(data_size/2), data_size):
    sine_list_x.append(math.sin(2*math.pi*freq2*(x/frate)))

wav_file = wave.open(fname, 'w')

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