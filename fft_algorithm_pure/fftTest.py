import cmath
import numpy as np
import timeit
from cmath import exp, pi

def fft(x):
	#N is sample length or number of samples
	#x is our input array aka our signal
	N = len(x)
	if N <= 1: return x
	#divide and conquer portion of algorithm. Divide evens and odds and do fft on both halves
	even = fft(x[0::2])
	odd =  fft(x[1::2])
		# x(n) * e^-i2pikn/N in practical cryptography site.
	T= [odd[k]*exp(-2j*pi*k/N) for k in range(N//2)]
			#this represents the real portion of N + this represents the imaginary portion of N
	return [even[k] + T[k] for k in range(N//2)] + [even[k] - T[k] for k in range(N//2)]

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


setup = '''
import random
from __main__ import fft
from __main__ import compute_fft

random.seed('slartibartfast')
s = [random.random() for i in range(100)]

'''

print( ' '.join("%5.3f" % abs(f)
				for f in compute_fft([1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0])) )
print(min(timeit.Timer('a=s[:]; compute_fft(a)', setup=setup).repeat(7, 1000)))
# print( timeit.timeit(compute_fft([1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0], number=1000)))

print( ' '.join("%5.3f" % abs(f)
				for f in fft([1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0])) )
print(min(timeit.Timer('a=s[:]; fft(a)', setup=setup).repeat(7, 1000)))
# print( timeit.timeit(fft([1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0], number=1000)))







