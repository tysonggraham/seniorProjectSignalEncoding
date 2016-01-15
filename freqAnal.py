#Eng Eder de Souza 01/12/2011
#ederwander
from matplotlib.mlab import find
import pyaudio
import numpy as np
import math


chunk = 2048
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5


def Pitch(signal):
    signal = np.fromstring(signal, 'Int16');
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

    print ("Frequency" + str(Frequency))
print (int(RATE / chunk * RECORD_SECONDS))


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