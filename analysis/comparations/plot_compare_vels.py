import numpy as np
import matplotlib.pyplot as plt

data298 = np.loadtxt("../analysis_298/velocities/veloc_298.xvg", comments=["@", "#"])
data400 = np.loadtxt("../analysis_400/velocities/veloc_400.xvg", comments=["@", "#"])

t298 = data298[:, 0]
t400 = data400[:, 0]

labels = ["C (ACE)", "CA (ALA)", "CA (ARG)", "CB (ARG)", "CA (MET)"]
cols = [4, 8, 12, 16, 20]

fig, axes = plt.subplots(5, 2, figsize=(10, 12), sharex=True)

for i, (label, col) in enumerate(zip(labels, cols)):
    axes[i, 0].plot(t298, data298[:, col], linewidth=1.2)
    axes[i, 0].set_ylabel(label)
    axes[i, 0].grid(True, linestyle="--", alpha=0.4)
    axes[i, 0].set_title("298 K" if i == 0 else "")

    axes[i, 1].plot(t400, data400[:, col], linewidth=1.2)
    axes[i, 1].grid(True, linestyle="--", alpha=0.4)
    axes[i, 1].set_title("400 K" if i == 0 else "")

axes[-1, 0].set_xlabel("Time (ps)")
axes[-1, 1].set_xlabel("Time (ps)")

plt.tight_layout()
plt.savefig("velocities_by_atom.png", dpi=300)
plt.show()
