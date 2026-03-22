import numpy as np
import matplotlib.pyplot as plt

data298 = np.loadtxt("../analysis_298/angles/angaver_1.xvg", comments=["@", "#"])
data400 = np.loadtxt("../analysis_400/angles/angaver_1.xvg", comments=["@", "#"])

angle1_298 = data298[:, 1]
angle1_400 = data400[:, 1]

plt.figure(figsize=(8,5))

plt.hist(angle1_298, bins=30, alpha=0.5, density=True, label="298 K")
plt.hist(angle1_400, bins=30, alpha=0.5, density=True, label="400 K")

plt.xlabel("Angle (degrees)")
plt.ylabel("Density")
plt.title("Distribution of CA-CB-CG (ARG) angle")

plt.legend()
plt.grid(True, linestyle="--", alpha=0.4)

plt.tight_layout()
plt.savefig("angle_1_hist.png", dpi=300)
plt.show()
