# ============================================
# DISEÑO E IMPLEMENTACIÓN DE FILTROS EN PYTHON
# ============================================

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# ==============================
# Parámetros
# ==============================

Fs = 1000                 # Frecuencia de muestreo (Hz)
t = np.arange(0, 1, 1/Fs) # Vector de tiempo (1 segundo)

# ==============================
# Crear señal compuesta
# ==============================

x1 = np.sin(2*np.pi*5*t)        # 5 Hz
x2 = 0.5*np.sin(2*np.pi*50*t)   # 50 Hz
x3 = 0.3*np.sin(2*np.pi*120*t)  # 120 Hz

senal_limpia = x1 + x2 + x3

# Ruido blanco
ruido = 0.5*np.random.randn(len(t))

# Señal contaminada
senal_ruidosa = senal_limpia + ruido

# ==============================
# Graficar señal ruidosa
# ==============================

plt.figure()
plt.plot(t, senal_ruidosa)
plt.title("Señal Ruidosa")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid()
plt.show()

# ==============================
# Filtro IIR Butterworth
# ==============================

fc = 40              # Frecuencia de corte (Hz)
orden = 4

Wn = fc / (Fs/2)     # Normalización

b_bw, a_bw = signal.butter(orden, Wn, btype='low')

senal_filtrada_bw = signal.filtfilt(b_bw, a_bw, senal_ruidosa)

plt.figure()
plt.plot(t, senal_ruidosa, label="Original")
plt.plot(t, senal_filtrada_bw, label="Butterworth")
plt.legend()
plt.title("Filtro IIR Butterworth")
plt.grid()
plt.show()

# ==============================
# Filtro IIR Chebyshev
# ==============================

Rp = 1  # Ripple (dB)

b_ch, a_ch = signal.cheby1(orden, Rp, Wn, btype='low')

senal_filtrada_ch = signal.filtfilt(b_ch, a_ch, senal_ruidosa)

plt.figure()
plt.plot(t, senal_ruidosa, label="Original")
plt.plot(t, senal_filtrada_ch, label="Chebyshev")
plt.legend()
plt.title("Filtro IIR Chebyshev")
plt.grid()
plt.show()

# ==============================
# Filtro FIR con Ventana Hamming
# ==============================

orden_fir = 50

b_fir = signal.firwin(orden_fir+1, Wn, window='hamming')

senal_filtrada_fir = signal.filtfilt(b_fir, [1], senal_ruidosa)

plt.figure()
plt.plot(t, senal_ruidosa, label="Original")
plt.plot(t, senal_filtrada_fir, label="FIR Hamming")
plt.legend()
plt.title("Filtro FIR con Ventana Hamming")
plt.grid()
plt.show()

# ==============================
# Comparación en Frecuencia (FFT)
# ==============================

N = len(senal_ruidosa)
f = np.fft.fftshift(np.fft.fftfreq(N, 1/Fs))

X = np.fft.fftshift(np.fft.fft(senal_ruidosa))
Y = np.fft.fftshift(np.fft.fft(senal_filtrada_bw))

plt.figure()
plt.plot(f, np.abs(X)/N, label="Original")
plt.plot(f, np.abs(Y)/N, label="Filtrada (Butterworth)")
plt.legend()
plt.title("Espectro de Frecuencia")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("|X(f)|")
plt.grid()
plt.show()

# ==============================
# Cálculo de error (MSE)
# ==============================

mse = np.mean((senal_limpia - senal_filtrada_bw)**2)
print("Error cuadrático medio (Butterworth):", mse)