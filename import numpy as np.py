import numpy as np
import matplotlib.pyplot as plt

# NMOS parameters
Vt = 0.4  # Threshold voltage in volts
kn = 1.0  # Process constant in mA/V^2

# Gate voltage range
Vg = np.linspace(0, 1.8, 100)

# Drain current calculation
Id = np.where(Vg < Vt, 0, kn * (Vg - Vt)**2)

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(Vg, Id, label=r'$I_D = k_n(V_G - V_t)^2$', color='blue')
plt.axvline(Vt, color='red', linestyle='--', label=r'$V_t = 0.4\,V$')
plt.title('NMOS Drain Current vs Gate Voltage')
plt.xlabel(r'$V_G$ (V)')
plt.ylabel(r'$I_D$ (mA)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()