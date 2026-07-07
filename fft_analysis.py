import numpy as np
import matplotlib.pyplot as plt

# Time vector
fs = 1000
t = np.linspace(0, 1, fs, endpoint=False)

# Signal with two frequencies
signal = np.sin(2 * np.pi * 50 * t) + 0.5 * np.sin(2 * np.pi * 120 * t)

# FFT
fft_result = np.fft.fft(signal)
frequencies = np.fft.fftfreq(len(signal), 1 / fs)

# Plot
plt.figure(figsize=(8, 4))
plt.plot(frequencies[:fs // 2], np.abs(fft_result[:fs // 2]))
plt.title("FFT Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid(True)
plt.show()
