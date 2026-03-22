import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("temp.xvg", comments=["@", "#"])

time = data[:, 0]
temp = data[:, 1]

plt.figure(figsize=(8,5))

plt.plot(time, temp, linewidth=2)

plt.xlabel("Time (ps)")
plt.ylabel("Temperature (K)")
plt.title("Temperature vs time (298 K)")

plt.grid(True, linestyle="--", alpha=0.4)

plt.tight_layout()
plt.savefig("temp_298.png", dpi=300)
plt.show()

plt.figure(figsize=(7,5))

plt.hist(temp, bins=30, alpha=0.7)

plt.xlabel("Temperature (K)")
plt.ylabel("Counts")
plt.title("Temperature distribution (298 K)")

plt.grid(True, linestyle="--", alpha=0.4)

plt.tight_layout()
plt.savefig("temp_hist_298.png", dpi=300)
plt.show()
