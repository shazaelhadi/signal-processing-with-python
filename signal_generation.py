import numpy as np
import matplotlib.pyplot as plt

# Generate time values
t = np.linspace(0, 1, 1000)

# Generate a 5 Hz sine wave
signal = np.sin(2 * np.pi * 5 * t)

# Plot the signal
plt.figure(figsize=(8, 4))
plt.plot(t, signal)
plt.title("5 Hz Sine Wave")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
