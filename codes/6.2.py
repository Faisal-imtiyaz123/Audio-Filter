import soundfile as sf
import matplotlib.pyplot as plt
from scipy import signal
import numpy as np

# Read .wav file 
input_signal, fs = sf.read('audio-filter-sound.wav') 

# Assuming you want to process the first channel
channel_to_process = input_signal[:, 0]

# Sampling frequency of input signal
sampl_freq = fs

# Order of the filter
order = 4

# Cutoff frequency 
cutoff_freq = 1000.0  

# Digital frequency
Wn = 2 * cutoff_freq / sampl_freq  

# Design the filter
b, a = signal.butter(order, Wn, 'low') 

# Get partial fraction expansion
r, p, k = signal.residuez(b, a)
print(r, "r")
print(p, "p")
print(k, "k")

# Number of terms of the impulse response
sz = 100
sz_lin = np.arange(sz)

# Vectorized function to compute the impulse response
def rp_vec(x):
    return np.sum(r * p**x)

# Apply the vectorized function to sz_lin to compute impulse response for the selected channel
h_channel = np.vectorize(rp_vec)(sz_lin)
k_add = np.pad(k, (0, sz - len(k)), 'constant', constant_values=(0, 0))
h = h_channel + k_add

# Plotting impulse response for the selected channel
plt.figure(figsize=(10, 6))
plt.stem(sz_lin, h)
plt.xlabel('n')
plt.ylabel('h(n)')
plt.title('Impulse Response (Single Channel)')
plt.grid()
plt.savefig("h(n)_single_channel.png")
plt.show()
