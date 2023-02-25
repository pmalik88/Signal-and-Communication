# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 14:44:26 2023

@author: kiit5444
"""

import numpy as np
import matplotlib.pyplot as plt

# Define carrier and message signals
fc = 100 # Carrier frequency (Hz)
fm = 10  # Message frequency (Hz)
Ac = 1   # Carrier amplitude
Am = 0.5 # Message amplitude

# Time settings
fs = 1000       # Sampling frequency (Hz)
duration = 1.0  # Signal duration (seconds)
t = np.arange(0, duration, 1/fs)  # Time vector

# Create carrier and message signals
carrier = Ac * np.cos(2*np.pi*fc*t)
message = Am * np.cos(2*np.pi*fm*t)

# Perform amplitude modulation
modulated = (Ac + message) * np.cos(2*np.pi*fc*t)

# Plot signals
fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, sharex=True, figsize=(8,8))

ax1.plot(t, carrier)
ax1.set(title='Carrier Signal', ylabel='Amplitude')

ax2.plot(t, message)
ax2.set(title='Message Signal', ylabel='Amplitude')

ax3.plot(t, modulated)
ax3.set(title='Amplitude Modulated Signal', xlabel='Time (s)', ylabel='Amplitude')

plt.tight_layout()
plt.show()
