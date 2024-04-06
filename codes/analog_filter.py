import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Sampling frequency from the audio file
sampl_freq = 44100
T = 1.0 / sampl_freq

# Order of the filter
order = 4

# Cutoff frequency 
cutoff_freq = 1000.0 

# Digital frequency
Wn = 2 * cutoff_freq / sampl_freq  

# Design the filter
b, a = signal.butter(order, Wn, 'low') 

# Bilinear Transform
def H(s):
    num = np.polyval(b, ((1 + s * (T / 2)) / (1 - s * (T / 2)))**(-1))
    den = np.polyval(a, ((1 + s * (T / 2)) / (1 - s * (T / 2)))**(-1))
    H = num / den
    return H

# Input and Output
analog_f = np.arange(0, 5000, 100)

# Compute the frequency response for each channel
num_channels = 2  # Example number of channels (replace with the actual number of channels)
plt.figure(figsize=(10, 6))
for i in range(num_channels):
    plt.plot(analog_f, abs(H(1j * analog_f)), label=f'Channel {i+1}')

plt.xlabel('$\omega$')
plt.ylabel('$|H(e^{j\omega})|$')
plt.title("Butterworth Filter Frequency Response (Analog Domain)")
plt.legend()
plt.grid()
plt.savefig("Butterworth_analog_multi_channel.png")
plt.show()
