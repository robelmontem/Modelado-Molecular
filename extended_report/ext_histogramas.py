import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, pi

# ---------- Lectura de datos ----------
temp_data = np.loadtxt("temp.xvg", comments=["@", "#"])
vel_data = np.loadtxt("vel_atom19.xvg", comments=["@", "#"])

time_temp = temp_data[:, 0]
temp = temp_data[:, 1]

# Para un solo átomo: columnas = time, vx, vy, vz, |v|
time_vel = vel_data[:, 0]
vx = vel_data[:, 1]
vy = vel_data[:, 2]
vz = vel_data[:, 3]
vmod = vel_data[:, 4]

# ---------- Función gaussiana ----------
def gaussian(x, mu, sigma):
    return 1.0 / (sigma * sqrt(2 * pi)) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

# ---------- Figura 1: histogramas ----------
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Temperatura
axes[0, 0].hist(temp, bins=50, density=True)
axes[0, 0].set_xlabel("Temperature (K)")
axes[0, 0].set_ylabel("Density")
axes[0, 0].set_title("Temperature distribution")
axes[0, 0].grid(True, linestyle="--", alpha=0.4)

# vx
x = np.linspace(vx.min(), vx.max(), 400)
axes[0, 1].hist(vx, bins=50, density=True, alpha=0.7, label="vx")
axes[0, 1].plot(x, gaussian(x, vx.mean(), vx.std(ddof=1)),
                label=f"Gaussian fit\nμ={vx.mean():.3f}, σ={vx.std(ddof=1):.3f}")
axes[0, 1].set_xlabel("vx (nm/ps)")
axes[0, 1].set_ylabel("Density")
axes[0, 1].set_title("vx distribution")
axes[0, 1].legend()
axes[0, 1].grid(True, linestyle="--", alpha=0.4)

# vy
x = np.linspace(vy.min(), vy.max(), 400)
axes[1, 0].hist(vy, bins=50, density=True, alpha=0.7, label="vy")
axes[1, 0].plot(x, gaussian(x, vy.mean(), vy.std(ddof=1)),
                label=f"Gaussian fit\nμ={vy.mean():.3f}, σ={vy.std(ddof=1):.3f}")
axes[1, 0].set_xlabel("vy (nm/ps)")
axes[1, 0].set_ylabel("Density")
axes[1, 0].set_title("vy distribution")
axes[1, 0].legend()
axes[1, 0].grid(True, linestyle="--", alpha=0.4)

# vz
x = np.linspace(vz.min(), vz.max(), 400)
axes[1, 1].hist(vz, bins=50, density=True, alpha=0.7, label="vz")
axes[1, 1].plot(x, gaussian(x, vz.mean(), vz.std(ddof=1)),
                label=f"Gaussian fit\nμ={vz.mean():.3f}, σ={vz.std(ddof=1):.3f}")
axes[1, 1].set_xlabel("vz (nm/ps)")
axes[1, 1].set_ylabel("Density")
axes[1, 1].set_title("vz distribution")
axes[1, 1].legend()
axes[1, 1].grid(True, linestyle="--", alpha=0.4)

plt.tight_layout()
plt.savefig("ext_temperature_velocity_histograms.png", dpi=300)
plt.show()

# ---------- Figura 2 opcional: series temporales ----------
fig, axes = plt.subplots(4, 1, figsize=(10, 9), sharex=False)

axes[0].plot(time_temp, temp, linewidth=1.0)
axes[0].set_title("Temperature vs time")
axes[0].set_ylabel("T (K)")
axes[0].grid(True, linestyle="--", alpha=0.4)

axes[1].plot(time_vel, vx, linewidth=1.0)
axes[1].set_title("vx vs time")
axes[1].set_ylabel("vx (nm/ps)")
axes[1].grid(True, linestyle="--", alpha=0.4)

axes[2].plot(time_vel, vy, linewidth=1.0)
axes[2].set_title("vy vs time")
axes[2].set_ylabel("vy (nm/ps)")
axes[2].grid(True, linestyle="--", alpha=0.4)

axes[3].plot(time_vel, vz, linewidth=1.0)
axes[3].set_title("vz vs time")
axes[3].set_ylabel("vz (nm/ps)")
axes[3].set_xlabel("Time (ps)")
axes[3].grid(True, linestyle="--", alpha=0.4)

plt.tight_layout()
plt.savefig("ext_temperature_velocity_timeseries.png", dpi=300)
plt.show()

# ---------- Resumen numérico ----------
print("Temperature:")
print(f"  mean = {temp.mean():.3f} K")
print(f"  std  = {temp.std(ddof=1):.3f} K")

print("\nVelocity components:")
for name, arr in [("vx", vx), ("vy", vy), ("vz", vz)]:
    print(f"  {name}: mean = {arr.mean():.5f} nm/ps, std = {arr.std(ddof=1):.5f} nm/ps")
