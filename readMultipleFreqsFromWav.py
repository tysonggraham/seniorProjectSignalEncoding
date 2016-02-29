import wave
import struct
from collections import Counter
import numpy as np
#try to reduce this to just one math library. Find logbase2 function in cmath or pi and exp and stuff in math
import cmath
import math

def main():
  #uppercase characters array
  cap = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '{', '}', '|', ':', '"', '<', '>', '?'];
  #lowercase characters array
  low = ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', '[', ']', '\\', ';', '\'', ',','.', '/'];

  # Each character is assigned a frequency in hz here.
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
    26 : '`',
    27 : '1',
    28 : '2',
    29 : '3',
    30 : '4',
    31 : '5',
    32 : '6',
    33 : '7',
    34 : '8',
    35 : '9',
    36 : '0',
    37 : '-',
    38 : '=',
    39 : '[',
    40 : ']',
    41 : '\\',
    42 : ';',
    43 : '\'',
    44 : ',',
    45 : '.',
    46 : '/'
  }

  def isCapital(letter):
    if (letter.islower()): #if it is an uppercase letter
      return letter.upper();
    elif (letter in low): #or if it is in the caps array
      return cap[low.index(letter)];
      print(letter)
    return ''

  def determineCharRep(fs, freq):
    step_size = 100
    letter = (int(freq/step_size))-3
    return enum.get(letter, ' ')

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

  def filterResultString(stringOfResults):
    import re
    #definitely keep
    newPrevChar = ''
    guessString = ''
    alternativeString = ''
    #might keep
    semiFinalString = ''
    finalString = ''

    for currentCharIndex in range(len(stringOfResults)//2):
      if(stringOfResults[currentCharIndex * 2] == stringOfResults[currentCharIndex * 2 + 1]):
        guessString += stringOfResults[currentCharIndex * 2]
        alternativeString += stringOfResults[currentCharIndex * 2]
      else:
        if(ord(stringOfResults[currentCharIndex * 2]) > ord(stringOfResults[currentCharIndex * 2+1])):
          guessString += stringOfResults[currentCharIndex * 2]
          alternativeString += stringOfResults[currentCharIndex * 2+1]
        else:
          guessString += stringOfResults[currentCharIndex * 2+1]
          alternativeString += stringOfResults[currentCharIndex * 2]
    print(alternativeString)
    print(guessString)
    guessString = re.sub(r'.*zz+yy+(.+)zz+yy+.*', r'\1', guessString)
    print(guessString)
    return guessString
  #**Open the Wav in read mode*****************************************************************
  waveFile = wave.open('output.wav', 'r')
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
  print('data')
  print(data)
  print('num_frames')
  print(num_frames)
  print('fs')
  print(fs)

  splitData = np.split(data, num_frames/fs)
  # #Now we need to operate on each splite piece of the data.
  amplitudes = []
  for x in range(len(splitData)):
    if (float.is_integer(math.log2(len(splitData[x])))):
      amplitudes.append(1/N * abs(compute_fft(splitData[x])))
    else:
      amplitudes.append(1/N * abs(compute_fft_numpy(splitData[x])))
  #*******************************Print out the results************************************************
  stringOfResults = ""
  count = 0
  prevLetter = ''
  for i in range(len(amplitudes)):
    maxIndex = np.argmax(amplitudes[i])
    if(maxIndex > fs):
      maxIndex -= fs
    stringOfResults += determineCharRep(fs,abs(freqs[maxIndex]))
  print('stringOfResults')
  print(stringOfResults)
  stringOfResults = filterResultString(stringOfResults);
  print('stringOfResults')
  print(stringOfResults)

  prevLetter = ''
  finalResult = ''
  for letter in stringOfResults:
    if (prevLetter == letter):
      count +=1
      if(count > 3):
        prevLetter = isCapital(letter)
        count = 1
    else:
      for x in range(count):
        finalResult += prevLetter
      prevLetter = letter
      count = 1
  for i in range(count):
    finalResult += prevLetter
  print('finalResult')
  print(finalResult)

if __name__ == "__main__":
  main()