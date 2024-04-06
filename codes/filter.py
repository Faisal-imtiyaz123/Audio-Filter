import soundfile as sf
from scipy import signal

# Read .wav file 
input_signal, fs = sf.read('audio-filter-sound.wav') 

# Check the number of channels in the input signal
num_channels = input_signal.shape[1]

# If there are multiple channels, separate them
if num_channels > 1:
    channel1 = input_signal[:, 0]  # Assuming you want to process the first channel
else:
    channel1 = input_signal  # Use the single channel

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

# Apply the filter to the chosen channel
output_signal = signal.filtfilt(b, a, channel1, padlen=1)

# Write the output signal into .wav file
sf.write('Sound_With_ReducedNoise.wav', output_signal, fs)