import numpy as np
import matplotlib.pyplot as plt

# Generate a noisy signal
t = np.linspace(0, 1, 1000)
clean_signal = np.sin(2 * np.pi * 5 * t)
noise = np.random.normal(0, 0.3, len(t))
noisy_signal = clean_signal + noise

# Simple moving average filter
window = 10
filtered_signal = np.convolve(noisy_signal, np.ones(window) / window, mode='same')

# Plot results
plt.figure(figsize=(10, 4))
plt.plot(t, noisy_signal, label="Noisy Signal", alpha=0.5)
plt.plot(t, filtered_signal, label="Filtered Signal", linewidth=2)
plt.legend()
plt.title("Noise Reduction")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
