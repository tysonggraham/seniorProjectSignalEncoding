from cmath import exp, pi

def fft(x):
	#N is sample length or number of samples
	#x is our input array aka our signal
	N = len(x)
	if N <= 1: return x
	#divide and conquer portion of algorithm. Divide evens and odds and do fft on both halves
	even = fft(x[0::2])
	odd =  fft(x[1::2])
		#x(n) * e^-i2pikn/N in practical cryptography site.
	T= [odd[k]*exp(-2j*pi*k/N) for k in range(N//2)]
			#this represents the real portion of N + this represents the imaginary portion of N
	return [even[k] + T[k] for k in range(N//2)] + [even[k] - T[k] for k in range(N//2)]
print( ' '.join("%5.3f" % abs(f)
				for f in fft([1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0])) )