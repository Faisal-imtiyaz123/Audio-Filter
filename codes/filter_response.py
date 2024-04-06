import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import soundfile as sf

# Read .wav file 
input_signal, fs = sf.read('audio-filter-sound.wav') 

# Assuming you want to process the first channel
channel_to_process = input_signal[:, 0]

# Sampling frequency obtained from the audio file
sampl_freq = fs 

# Order of the filter
order = 4

# Cutoff frequency 4kHz
cutoff_freq = 1000.0 

# Digital frequency
Wn = 2 * cutoff_freq / sampl_freq  

# Design the filter
b, a = signal.butter(order, Wn, 'low') 

# DTFT
def H(z):
    num = np.polyval(b, z**(-1))
    den = np.polyval(a, z**(-1))
    H = num / den
    return H

# Input and Output
omega = np.linspace(0, np.pi, 100)

# Compute the frequency response for each channel
num_channels = input_signal.shape[1]
plt.figure(figsize=(10, 6))
for i in range(num_channels):
    channel_response = H(np.exp(1j * omega))
    plt.plot(omega, abs(channel_response), label=f'Channel {i+1}')

plt.xlabel('$\omega$')
plt.ylabel('$|H(e^{j\omega})|$')
plt.title("Butterworth Filter Frequency Response")
plt.legend()
plt.grid()
plt.savefig("Filter_Response.png")
plt.show()
