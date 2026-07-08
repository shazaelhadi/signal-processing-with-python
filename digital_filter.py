import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

# Create a noisy signal
fs = 500
t = np.linspace(0, 1, fs)
signal = np.sin(2 * np.pi * 5 * t)
noise = 0.5 * np.random.randn(fs)
noisy_signal = signal + noise

# Butterworth low-pass filter
b, a = butter(4, 10 / (fs / 2), btype='low')
filtered_signal = filtfilt(b, a, noisy_signal)

# Plot
plt.figure(figsize=(10,5))
plt.plot(t, noisy_signal, label='Noisy Signal', alpha=0.6)
plt.plot(t, filtered_signal, label='Filtered Signal', linewidth=2)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Digital Low-Pass Filter")
plt.legend()
plt.grid(True)
plt.show()
