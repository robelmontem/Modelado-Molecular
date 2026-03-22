import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("energy_400.xvg", comments=["@", "#"])

t = data[:, 0]
E_tot = data[:, 1]
E_kin = data[:, 2]

plt.figure(figsize=(8,5))

plt.plot(t, E_tot, label="Total energy", linewidth=1.5)
plt.plot(t, E_kin, label="Kinetic energy", linewidth=1.5)

plt.xlabel("Time (ps)")
plt.ylabel("Energy (kJ/mol)")
plt.title("Energy vs time (400 K)")

plt.legend()
plt.grid(True, linestyle="--", alpha=0.4)

plt.tight_layout()
plt.savefig("energy_400.png", dpi=300)
plt.show()
