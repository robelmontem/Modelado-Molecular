import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("dist.xvg", comments=["@", "#"])

time = data[:, 0]
bond1 = data[:, 1]
bond2 = data[:, 2]

plt.figure(figsize=(8, 5))

plt.plot(time, bond1, linewidth=2, label="C(ALA)-N(ARG)")
plt.plot(time, bond2, linewidth=2, label="CA(ARG)-CB(ARG)")

plt.xlabel("Time (ps)")
plt.ylabel("Distance (nm)")
plt.title("Bond distances at 400 K")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.4)

plt.tight_layout()
plt.savefig("bond_distances_400.png", dpi=300)
plt.show()
