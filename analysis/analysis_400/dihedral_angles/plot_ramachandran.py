import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("arg.dat")

t = data[:, 0]
phi = data[:, 1]
psi = data[:, 2]

plt.figure(figsize=(6,6))

plt.scatter(phi, psi, s=10, alpha=0.5)

plt.xlabel("Phi (deg)")
plt.ylabel("Psi (deg)")
plt.title("Ramachandran plot (ARG)")

plt.grid(True, linestyle="--", alpha=0.4)

plt.tight_layout()
plt.savefig("rama_arg.png", dpi=300)
plt.show()
