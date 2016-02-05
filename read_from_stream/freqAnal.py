#Eng Eder de Souza 01/12/2011
#ederwander
import pyaudio
from numpy import linspace, pi, cos, absolute
import math
import cmath
import numpy as np

#bin size of n
chunk = 2048
#definition of integer type of the values coming out as frequencies
#choices include PaInt32, PaInt16, PaUint16, PaUint32
FORMAT = pyaudio.paInt32
#1 for mono, 2 for stereo
CHANNELS = 1
#Frame rate (i.e. frames/second) These frames will be divided by bins of chunk size
RATE = 44100 # is this in hz? find out
#duration that the microphone will listen
RECORD_SECONDS = 100
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

def compute_dft(input):
     # Number of inputs
     n = len(input)
     output = [complex(0)] * n
     for k in range(n):  # For each output element
          # Reset output
          s = complex(0)
          for t in range(n):  # For each input element
               # input times e^(-2(pi)i*t*k/n)
               s += input[t] * cmath.exp(-2j * cmath.pi * t * k / n)
          # Set bin
          # Not sure if we need to take abs value yet. Will switch if necessary.
          # output[k] = abs(s)
          output[k] = s
     return output

def compute_fft(input):
     return np.fft.fft(input);


def Pitch(signal):
     #build an array of 32 bit ints from a string
     signal = np.fromstring(signal, 'Int32');
     #for each entry in the signal array, copysign helps us determine whether
     #we are looking at a signal with a frequency we can use.
     crossing = [math.copysign(1.0, s) for s in signal]
     # take the difference between each pair of elements. The latter - the former
     #this is a fancy array of changes in frequency.
     index = find(np.diff(crossing));
     print('signal')
     print(len(signal))
     # print('index')
     # print('index')
     # print('signal')
     # print('signal')
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
     signal = np.fromstring(data, 'Int32')
     # Frequency = Pitch(data)
     # print (np.fft.fft(signal))
     # print ("Frequency" + str(Frequency))
print (int(RATE / chunk * RECORD_SECONDS))

fs=64
length = 1
n = fs * length
t = linspace(0,length,num=n,endpoint=False)
f = 8 #input frequency
signalTest = cos(2*pi*f*t)  
# print(signalTest)
#MAY USE LATER
N = fs * length
k = 56
freqs = np.fft.fftfreq(N, 1/fs)
# print('(k * fs)/N')
amplitude = 1/N * abs(compute_fft(signalTest))
fftshiftthing = np.fft.fftshift(freqs)
fftshiftthingamplitude = np.fft.fftshift(amplitude)
for x in range(len(fftshiftthing)):
     if (fftshiftthingamplitude[x] > .1) :
          print (fftshiftthing[x] , ' : ' ,fftshiftthingamplitude[x])

# print('amplitude')
# print(amplitude)
# S = 0.7*cmath.sin(2*cmath.pi*50*t) + cmath.sin(2*cmath.pi*120*t);
# print(signalTest)
# print (compute_dft(signalTest))
# print (compute_fft(signalTest))