import numpy as np
import matplotlib.pyplot as plt

data298 = np.loadtxt("../analysis_298/temperature/temp.xvg", comments=["@", "#"])
data400 = np.loadtxt("../analysis_400/temperature/temp.xvg", comments=["@", "#"])

t298, temp298 = data298[:,0], data298[:,1]
t400, temp400 = data400[:,0], data400[:,1]

plt.figure(figsize=(8,5))

plt.plot(t298, temp298, label="298 K", linewidth=2)
plt.plot(t400, temp400, label="400 K", linewidth=2)

plt.xlabel("Time (ps)")
plt.ylabel("Temperature (K)")
plt.title("Temperature comparison")

plt.legend()
plt.grid(True, linestyle="--", alpha=0.4)

plt.tight_layout()
plt.savefig("temp_comparison.png", dpi=300)
plt.show()

plt.figure(figsize=(7,5))

plt.hist(temp298, bins=30, alpha=0.5, label="298 K", density=True)
plt.hist(temp400, bins=30, alpha=0.5, label="400 K", density=True)

plt.xlabel("Temperature (K)")
plt.ylabel("Density")
plt.title("Temperature distribution")

plt.legend()
plt.grid(True, linestyle="--", alpha=0.4)

plt.tight_layout()
plt.savefig("temp_hist_comparison.png", dpi=300)
plt.show()
