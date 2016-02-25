#modules for experiment
import wave
import struct
from scipy import stats
from collections import Counter
import numpy as np
from numpy import linspace, pi, cos, absolute
import cmath
import math

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

def determineCharRep(fs, freq):
  CHUNK = 32;
  step_size = fs/CHUNK
  print(freq/step_size)

#*****************************************************************************************
# This is our implementation of the dft
#*****************************************************************************************
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
          output[k] = s
     return output

#*****************************************************************************************
# This is our implementation of the fft
#*****************************************************************************************
def compute_fft(x):
  #N is sample length or number of samples
  #x is our input array aka our signal
  N = len(x)
  if N <= 1: return x
  #divide and conquer portion of algorithm. Divide evens and odds and do fft on both halves
  even = compute_fft(x[0::2])
  odd =  compute_fft(x[1::2])
    # x(n) * e^-i2pikn/N in practical cryptography site.
  T= [odd[k]*cmath.exp(-2j*pi*k/N) for k in range(N//2)]
      #this represents the real portion of N + this represents the imaginary portion of N
  return np.array([even[k] + T[k] for k in range(N//2)] + [even[k] - T[k] for k in range(N//2)])

#*****************************************************************************************
# This is an optimized implementation of the fft. Same (O) as our fft but use constants 
# instead of calculations in the loop
#*****************************************************************************************
def compute_fft_numpy(input):
     return np.fft.fft(input);

#**Open the Wav in read mode*****************************************************************
waveFile = wave.open('WaveTest.wav', 'r')
#****************************************************************************************
# Set our Variables. Look in useful info below to find variable meanings in more depth.
#***************************Set directly by Wav FIle info************************************
(channels,samp_width,fs,num_frames,compression_type, compression_name) = waveFile.getparams()
frames = waveFile.readframes(num_frames * channels)
#***************************Variables for intermediary calculations******************************
N = int(num_frames/channels)  # Total number of samples?
data = np.asarray(struct.unpack_from("%dh" % num_frames * channels, frames)) #Grab data from Wave to be put into FFT
#**************************Variables used for final calculation*****************************************************
freqs = np.fft.fftfreq(fs, 1/fs)
#NEED TO SPLIT UP DATA HERE BEFORE DOING FFT
splitData = np.split(data, num_frames/fs)
# #Now we need to operate on each splite piece of the data.
amplitude = []
for x in range(len(splitData)):
  if (float.is_integer(math.log2(len(splitData[x])))):
    amplitude.append(1/N * abs(compute_fft(splitData[x])))
  else:
    amplitude.append(1/N * abs(compute_fft_numpy(splitData[x])))
#*********************Reorder the results to print out prettier**************************************
finalFrequencies = np.fft.fftshift(freqs)
finalAmplitudes = np.fft.fftshift(amplitude)
#*******************************Print out the results*************************************************
determineCharRep(8192, 2560);
print ('freq(Hz) : amplitude')
for i in range(len(finalAmplitudes)):
  for x in range(len(finalAmplitudes[i])):
    if (finalAmplitudes[i][x] > 1000 and finalFrequencies[x] >= 0) :
      print (finalFrequencies[x] , ' : ' ,finalAmplitudes[i][x])