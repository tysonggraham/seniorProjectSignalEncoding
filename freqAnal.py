#Eng Eder de Souza 01/12/2011
#ederwander
from matplotlib.mlab import find
import pyaudio
import numpy as np
import math

#bin size
chunk = 2048
#
FORMAT = pyaudio.paInt32
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 50


def Pitch(signal):
    signal = np.fromstring(signal, 'Int32');
    crossing = [math.copysign(1.0, s) for s in signal]
    index = find(np.diff(crossing));
    f0=round(len(index) *RATE /(2*np.prod(len(signal))))
    f0=round(f0/50) * 50
    return f0;


p = pyaudio.PyAudio()

stream = p.open(format = FORMAT,
				channels = CHANNELS,
				rate = RATE,
				input = True,
				output = True,
				frames_per_buffer = chunk)

for i in range(0, int(RATE / chunk * RECORD_SECONDS)):
	data = stream.read(chunk)
	Frequency=Pitch(data)
	letterValue = (Frequency - 300) / 50
	enum = { 
	     0 : 'a',
	     1 : 'b',
	     2 : 'c',
	     3 : 'd',
	     4 : 'e',
	     5 : 'f',
	     6 : 'g',
	     7 : 'h',
	     8 : 'i',
	     9 : 'j',
	     10 : 'k',
	     11 : 'l',
	     12 : 'm',
	     13 : 'n',
	     14 : 'o',
	     15 : 'p',
	     16 : 'q',
	     17 : 'r',
	     18 : 's',
	     19 : 't',
	     20 : 'u',
	     21 : 'v',
	     22 : 'w',
	     23 : 'x',
	     24 : 'y',
	     25 : 'z',
	     26 : '1',
	     27 : '2',
	     28 : '3',
	     29 : '4',
	     30 : '5',
	     31 : '6',
	     32 : '7',
	     33 : '8',
	     34 : '9',
	     35 : '0',
	     36 : '-',
	     37 : '=',
	     38 : '[',
	     39 : ']',
	     40 : '\\',
	     41 : ';',
	     42 : '\'',
	     43 : ',',
	     44 : '.',
	     45 : '/',
	}
	print(letterValue)
	print(enum.get(letterValue, '*'))
	print ("Frequency" + str(Frequency))
print (int(RATE / chunk * RECORD_SECONDS))
