import wave
import struct
import numpy as np
from scipy import stats
from collections import Counter
def ffind_nearest(array, value):
    idx = (np.abs(array-value))
    return idx

if __name__ == '__main__':
    data_size = 11400
    fname = "WaveTest.wav"
    frate = 11025.0
    wav_file = wave.open(fname, 'r')
    data = wav_file.readframes(data_size)
    wav_file.close()
    data = struct.unpack('{n}h'.format(n=data_size), data)
    data = np.array(data)

    w = np.fft.fft(data)
    freqs = np.fft.fftfreq(len(w))
    mode = stats.mode(np.abs(w))[0][0]
    print('mode')
    print(mode)
    # itemindex = np.nonzero(w<mode)
    itemindex =len(np.abs(w-mode))
    print('itemindex')
    print(itemindex)
    # print('freqs')
    # print(freqs[:len(freqs)/16])
    # print(freqs[:len(freqs)/16].min(), freqs[:len(freqs)/16].max(), stats.mode(freqs[:len(freqs)/16]))
    # print(freqs.min(), freqs.max())
    # (-0.5, 0.499975)


    # Find the peak in the coefficients
    idx3 = np.argmax(np.abs(w))
    idx2 = np.argmax(freqs)
    # freq = freqs[idx]
    freq_in_hertz = abs(freq * frate)
    print(freq_in_hertz)
    # 439.8975
    