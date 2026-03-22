import numpy as np
import matplotlib.pyplot as plt

data298 = np.loadtxt("../analysis_298/gyrate/gyrate.xvg", comments=["@", "#"])
data400 = np.loadtxt("../analysis_400/gyrate/gyrate.xvg", comments=["@", "#"])

plt.figure(figsize=(8,5))

plt.plot(data298[:,0], data298[:,1], label="298 K", linewidth=2)
plt.plot(data400[:,0], data400[:,1], label="400 K", linewidth=2)

plt.xlabel("Time (ps)")
plt.ylabel("Radius of gyration (nm)")
plt.title("Comparison of radius of gyration")

plt.legend()
plt.grid(True, linestyle="--", alpha=0.4)

plt.tight_layout()
plt.savefig("gyrate_comparison.png", dpi=300)
plt.show()
