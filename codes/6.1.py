import soundfile as sf
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

# Read .wav file 
input_signal, fs = sf.read('audio-filter-sound.wav') 

# Check the number of channels in the input signal
num_channels = input_signal.shape[1]

# Assuming you want to process the first channel
channel_to_filter = input_signal[:, 0]

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

# Apply the filter using built-in function
output_signal_built_in = signal.filtfilt(b, a, channel_to_filter, padlen=1)

# Apply the filter forward in time
output_signal_manual = signal.lfilter(b, a, channel_to_filter)

# Plot the filtered signals
plt.figure(figsize=(10, 6))
plt.plot(output_signal_built_in, label='Filtered Signal (Built-in)', alpha=0.7)
plt.plot(output_signal_manual, label='Filtered Signal (Manual)', alpha=0.7)

plt.title('Comparison of Filtered Signals')
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()


