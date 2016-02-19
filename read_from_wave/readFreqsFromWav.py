#modules for experiment
import wave
import struct
from scipy import stats
from collections import Counter
import numpy as np
from numpy import linspace, pi, cos, absolute
import cmath
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
          # output[k] = abs(s)
          output[k] = s
     return output

#*****************************************************************************************
# This is our implementation of the fft
#*****************************************************************************************
def compute_fft(input):
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
     return np.array(output)

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
#***************************Set directly by Wav FIle info******************************************
(channels,samp_width,fs,num_frames,compression_type, compression_name) = waveFile.getparams()
frames = waveFile.readframes(num_frames * channels)
#***************************Variables for intermediary calculations******************************
length = num_frames/(fs*channels) #Length of each sample?
N = int(fs * length)  # Total number of samples?
t = linspace(0,length,num=N,endpoint=False) # NEED TO EXPLAIN THIS BETTER
data = struct.unpack_from("%dh" % num_frames * channels, frames) #Grab data from Wave to be put into FFT
k = 56
#**************************Variables used for final calculation*****************************************************
freqs = np.fft.fftfreq(N, 1/fs)
amplitude = 1/N * abs(compute_fft_numpy(data))
#Test to make sure ours works. comment line above and uncomment line below to initiate test.
# amplitude = 1/N * abs(compute_fft(data))

#*********************Reorder the results to print out prettier**************************************
finalFrequencies = np.fft.fftshift(freqs)
finalAmplitude = np.fft.fftshift(amplitude)
#*******************************Print out the results*************************************************
print ('freq(Hz) : amplitude')
for x in range(len(finalFrequencies)):
     if (finalAmplitude[x] > 2500 and finalFrequencies[x] >= 0) :
          print (finalFrequencies[x] , ' : ' ,finalAmplitude[x])

#******************************Divide the array into two if it's stereo**********************
if channels == 2:
    left = np.array(data[0::2])
    right = np.array(data[1::2])
#******************************Keep it the same if it is Mono**********************
else:
    left = np.array(data)
    right = left

#Useful information:
#We can use this to create a signal
#-------------------------------------
# fs=5000 Sampling Frequency
# N = int(fs * length)  # Total number of samples?
# t = linspace(0,length,num=N,endpoint=False)
# f = 312 #input frequency
#length = num_frames/(fs*channels) This will be used to give the total number of samples? This is the length of each sample I think
# signalTest = cos(2*pi*f*t) creates the signal called signalTest
#(num_frames/fs) calculates Duration
# num frames is the frate in Monowav.py
# (num_channels,samp_width,fs,num_frames,compression_type, compression_name) = waveFile.getparams()
# frames = waveFile.readframes(num_frames * num_channels)