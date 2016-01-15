import wave
import struct
import numpy as np
from scipy import stats

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
    print('freqs')
    print(freqs[:len(freqs)/16])
    print(freqs[:len(freqs)/16].min(), freqs[:len(freqs)/16].max(), stats.mode(freqs[:len(freqs)/16]))
    print(freqs.min(), freqs.max())
    # (-0.5, 0.499975)

    # Find the peak in the coefficients
    idx = np.argmax(np.abs(w))
    freq = freqs[idx]
    freq_in_hertz = abs(freq * frate)
    print(freq_in_hertz)
    # 439.8975