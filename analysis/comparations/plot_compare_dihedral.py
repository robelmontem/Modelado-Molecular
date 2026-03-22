import numpy as np
import matplotlib.pyplot as plt

data298 = np.loadtxt("../analysis_298/dihedral_angles/arg.dat")
data400 = np.loadtxt("../analysis_400/dihedral_angles/arg.dat")

t298 = data298[:, 0]
phi298 = data298[:, 1]
psi298 = data298[:, 2]

t400 = data400[:, 0]
phi400 = data400[:, 1]
psi400 = data400[:, 2]

fig, axes = plt.subplots(2, 1, figsize=(9, 6), sharex=True, sharey=True)

axes[0].plot(t298, phi298, linewidth=1.5, label="phi")
axes[0].plot(t298, psi298, linewidth=1.5, label="psi")
axes[0].set_title("ARG dihedral angles at 298 K")
axes[0].set_ylabel("Angle (deg)")
axes[0].grid(True, linestyle="--", alpha=0.4)
axes[0].legend()

axes[1].plot(t400, phi400, linewidth=1.5, label="phi")
axes[1].plot(t400, psi400, linewidth=1.5, label="psi")
axes[1].set_title("ARG dihedral angles at 400 K")
axes[1].set_xlabel("Frame")
axes[1].set_ylabel("Angle (deg)")
axes[1].grid(True, linestyle="--", alpha=0.4)
axes[1].legend()

plt.tight_layout()
plt.savefig("dihedrals_time_comparison.png", dpi=300)
plt.show()
