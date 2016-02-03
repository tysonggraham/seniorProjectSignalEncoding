# http://stackoverflow.com/questions/3694918/how-to-extract-frequency-associated-with-fft-values-in-python
import wave
import struct
import numpy as np
from scipy import stats
from collections import Counter
# def ffind_nearest(array, value):
#     idx = (np.abs(array-value))
#     return idx

# if __name__ == '__main__':
#     data_size = 11400
#     fname = "WaveTest.wav"
#     frate = 11025.0
#     wav_file = wave.open(fname, 'r')
#     data = wav_file.readframes(data_size)
#     wav_file.close()
#     data = struct.unpack('{n}h'.format(n=data_size), data)
#     data = np.array(data)

#     w = np.fft.fft(data)
#     freqs = np.fft.fftfreq(len(w))
#     mode = stats.mode(np.abs(w))[0][0]
#     print('mode')
#     print(mode)
#     # itemindex = np.nonzero(w<mode)
#     itemindex =len(np.abs(w-mode))
#     print('itemindex')
#     print(itemindex)
#     # print('freqs')
#     # print(freqs[:len(freqs)/16])
#     # print(freqs[:len(freqs)/16].min(), freqs[:len(freqs)/16].max(), stats.mode(freqs[:len(freqs)/16]))
#     # print(freqs.min(), freqs.max())
#     # (-0.5, 0.499975)


#     # Find the peak in the coefficients
#     idx3 = np.argmax(np.abs(w))
#     idx2 = np.argmax(freqs)
#     # freq = freqs[idx]
#     freq_in_hertz = abs(freq * frate)
#     print(freq_in_hertz)
#     # 439.8975
#     

waveFile = wave.open('WaveTest.wav', 'r')
#num frames is the frate in Monowav.py
# need to find chunk now aka bin size
(num_channels,samp_width,frame_rate,num_frames,compression_type, compression_name) = waveFile.getparams()
frames = waveFile.readframes(num_frames * num_channels)
#Should print out 1
print('num_channels')
print(num_channels)
#Should print out 2
print('samp_width')
print(samp_width)
#Should print out 5000
print('frame_rate')
print(frame_rate)
#Should print out 5000 * num seconds in wav file
print('num_frames')
print(num_frames)
#Should print out NONE or some compression type
print('compression_type')
print(compression_type)
#Should print out either compressed or not compressed
print('compression_name')
print(compression_name)

#Duration
print((num_frames/frame_rate))

data = struct.unpack_from("%dh" % num_frames * num_channels, frames)
    
if num_channels == 2:
    left = np.array(data[0::2])
    right = np.array(data[1::2])
else:
    left = np.array(data)
    right = left
print('left')
print(left)
print('right')
print(right)

# for i in range(0,length):
#     waveData=waveFile.readframes(1)
#     data = struct.unpack("<h", waveData)
#     print (int(data[0]))