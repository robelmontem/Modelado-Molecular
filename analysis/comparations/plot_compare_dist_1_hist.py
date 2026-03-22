import numpy as np
import matplotlib.pyplot as plt


data298 = np.loadtxt("../analysis_298/distances/dist.xvg", comments=["@", "#"])
data400 = np.loadtxt("../analysis_400/distances/dist.xvg", comments=["@", "#"])

bond1_298 = data298[:, 1]
bond1_400 = data400[:, 1]

plt.figure(figsize=(8, 5))

plt.hist(bond1_298, bins=25, alpha=0.5, density=True, label="298 K")
plt.hist(bond1_400, bins=25, alpha=0.5, density=True, label="400 K")

plt.xlabel("Distance (nm)")
plt.ylabel("Density")
plt.title("Distribution of C(ALA)-N(ARG) bond distance")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.4)

plt.tight_layout()
plt.savefig("bond1_hist.png", dpi=300)
plt.show()
