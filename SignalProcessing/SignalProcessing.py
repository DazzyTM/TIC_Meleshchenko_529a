import numpy as np
from scipy import signal, fft
import matplotlib.pyplot as plt

# Генерація випадкового сигналу
n = 500
random = np.random.normal(0, 10, n)

# Визначення відліків часу
Fs = 1000
t = np.arange(n)/Fs

# Розрахунок параметрів ФНЧ
F_max = 19
w = F_max/(Fs/2)
b, a = signal.butter(3, w, 'low', output='ba')[:2]

# Фільтрація сигналу
filtered = signal.filtfilt(b, a, random)

# Побудова графіка сигналу
fig, ax = plt.subplots(figsize=(21/2.54, 14/2.54))
ax.plot(t, filtered, linewidth=1)
ax.set_xlabel('Час, с', fontsize=14)
ax.set_ylabel('Амплітуда', fontsize=14)
plt.title('Випадковий сигнал', fontsize=14)
plt.grid()
fig.savefig('./figures/signal.png', dpi=600)

# Розрахунок спектру
spectrum = fft.fft(filtered)
spectrum = np.abs(fft.fftshift(spectrum))
freqs = fft.fftshift(fft.fftfreq(n, 1/n))

# Побудова графіка спектру
fig, ax = plt.subplots(figsize=(21/2.54, 14/2.54))
ax.plot(freqs, spectrum, linewidth=1)
ax.set_xlabel('Частота, Гц', fontsize=14)
ax.set_ylabel('Амплітуда', fontsize=14)
plt.title('Спектр сигналу', fontsize=14)
plt.grid()
fig.savefig('./figures/spectrum.png', dpi=600)

plt.show()