import numpy as np
import matplotlib.pyplot as plt

data298 = np.loadtxt("../analysis_298/distances/dist.xvg", comments=["@", "#"])
data400 = np.loadtxt("../analysis_400/distances/dist.xvg", comments=["@", "#"])

t298 = data298[:, 0]
t400 = data400[:, 0]

bond1_298 = data298[:, 1]
bond1_400 = data400[:, 1]

fig, axes = plt.subplots(2, 1, figsize=(8, 6), sharex=True, sharey=True)

axes[0].plot(t298, bond1_298, linewidth=1.5)
axes[0].set_title("C(ALA)-N(ARG) at 298 K")
axes[0].set_ylabel("Distance (nm)")
axes[0].grid(True, linestyle="--", alpha=0.4)

axes[1].plot(t400, bond1_400, linewidth=1.5)
axes[1].set_title("C(ALA)-N(ARG) at 400 K")
axes[1].set_xlabel("Time (ps)")
axes[1].set_ylabel("Distance (nm)")
axes[1].grid(True, linestyle="--", alpha=0.4)

plt.tight_layout()
plt.savefig("bond1_panels.png", dpi=300)
plt.show()
