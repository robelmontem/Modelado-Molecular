import numpy as np
import matplotlib.pyplot as plt

data298 = np.loadtxt("../analysis_298/energies/energy_298.xvg", comments=["@", "#"])
data400 = np.loadtxt("../analysis_400/energies/energy_400.xvg", comments=["@", "#"])

t298, Ekin298 = data298[:,0], data298[:,1]
t400, Ekin400 = data400[:,0], data400[:,1]

plt.figure(figsize=(8,5))

plt.plot(t298, Ekin298, label="298 K", linewidth=2)
plt.plot(t400, Ekin400, label="400 K", linewidth=2)

plt.xlabel("Time (ps)")
plt.ylabel("Kinetic energy (kJ/mol)")
plt.title("Kinetic energy comparison")

plt.legend()
plt.grid(True, linestyle="--", alpha=0.4)

plt.tight_layout()
plt.savefig("Ekin_comparison.png", dpi=300)
plt.show()
