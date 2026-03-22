import numpy as np
import matplotlib.pyplot as plt

phi = np.loadtxt("phi_arg.dat")
psi = np.loadtxt("psi_arg.dat")

t = phi[:, 0]
phi_vals = phi[:, 1]
psi_vals = psi[:, 1]

plt.figure(figsize=(8,5))

plt.plot(t, phi_vals, label="phi (ARG)", linewidth=2)
plt.plot(t, psi_vals, label="psi (ARG)", linewidth=2)

plt.xlabel("Frame")
plt.ylabel("Angle (deg)")
plt.title("Dihedral angles (ARG)")

plt.legend()
plt.grid(True, linestyle="--", alpha=0.4)

plt.tight_layout()
plt.savefig("dihedrals.png", dpi=300)
plt.show()
