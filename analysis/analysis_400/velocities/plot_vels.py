import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("veloc_400.xvg", comments=["@", "#"])

t = data[:, 0]

labels = ["C (ACE)", "CA (ALA)", "CA (ARG)", "CB (ARG)", "CA (MET)"]
cols = [4, 8, 12, 16, 20]

fig, axes = plt.subplots(5, 1, figsize=(9, 10), sharex=True)

for ax, label, col in zip(axes, labels, cols):
    ax.plot(t, data[:, col], linewidth=1.2)
    ax.set_ylabel(label)
    ax.grid(True, linestyle="--", alpha=0.4)

axes[0].set_title("Velocity magnitudes of 5 selected atoms at 298 K")
axes[-1].set_xlabel("Time (ps)")

plt.tight_layout()
plt.savefig("velocities_400_subplots.png", dpi=300)
plt.show()
