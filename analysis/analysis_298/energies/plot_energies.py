import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("energy_298.xvg", comments=["@", "#"])

t = data[:, 0]
E_tot = data[:, 2]
E_kin = data[:, 1]

plt.figure(figsize=(8,5))

plt.plot(t, E_tot, label="Total energy", linewidth=1.5)
plt.plot(t, E_kin, label="Kinetic energy", linewidth=1.5)

plt.xlabel("Time (ps)")
plt.ylabel("Energy (kJ/mol)")
plt.title("Energy vs time (298 K)")

plt.legend()
plt.grid(True, linestyle="--", alpha=0.4)

plt.tight_layout()
plt.savefig("energy_298.png", dpi=300)
plt.show()
