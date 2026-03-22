import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("arg.dat")

t = data[:, 0]
phi = data[:, 1]
psi = data[:, 2]

plt.figure(figsize=(8,5))

plt.plot(t, phi, label="phi (ARG)", linewidth=2)
plt.plot(t, psi, label="psi (ARG)", linewidth=2)

plt.xlabel("Frame")
plt.ylabel("Angle (deg)")
plt.title("Dihedral angles of ARG")

plt.legend()
plt.grid(True, linestyle="--", alpha=0.4)

plt.tight_layout()
plt.savefig("dihedrals_time.png", dpi=300)
plt.show()
