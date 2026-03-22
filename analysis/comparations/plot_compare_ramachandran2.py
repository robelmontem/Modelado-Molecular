import numpy as np
import matplotlib.pyplot as plt


data298 = np.loadtxt("../analysis_298/dihedral_angles/arg.dat")
data400 = np.loadtxt("../analysis_400/dihedral_angles/arg.dat")

phi298, psi298 = data298[:, 1], data298[:, 2]
phi400, psi400 = data400[:, 1], data400[:, 2]

def wrap_angles(a):
    return (a + 180) % 360 - 180

phi298 = wrap_angles(phi298)
psi298 = wrap_angles(psi298)
phi400 = wrap_angles(phi400)
psi400 = wrap_angles(psi400)

# límites robustos a partir de la nube principal
all_phi = np.concatenate([phi298, phi400])
all_psi = np.concatenate([psi298, psi400])

x_min, x_max = np.percentile(all_phi, [1, 99])
y_min, y_max = np.percentile(all_psi, [1, 99])

# pequeño margen
x_pad = 0.05 * (x_max - x_min)
y_pad = 0.05 * (y_max - y_min)

xlim = (x_min - x_pad, x_max + x_pad)
ylim = (y_min - y_pad, y_max + y_pad)

fig, axes = plt.subplots(1, 2, figsize=(10, 5), sharex=True, sharey=True)

axes[0].scatter(phi298, psi298, s=10, alpha=0.5)
axes[0].set_title("Ramachandran (298 K)")
axes[0].set_xlabel("Phi (deg)")
axes[0].set_ylabel("Psi (deg)")
axes[0].set_xlim(*xlim)
axes[0].set_ylim(*ylim)
axes[0].grid(True, linestyle="--", alpha=0.4)

axes[1].scatter(phi400, psi400, s=10, alpha=0.5)
axes[1].set_title("Ramachandran (400 K)")
axes[1].set_xlabel("Phi (deg)")
axes[1].set_ylabel("Psi (deg)")
axes[1].set_xlim(*xlim)
axes[1].set_ylim(*ylim)
axes[1].grid(True, linestyle="--", alpha=0.4)

plt.tight_layout()
plt.savefig("rama_comparison_zoom.png", dpi=300)
plt.show()
