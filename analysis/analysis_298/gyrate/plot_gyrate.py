import numpy as np
import matplotlib.pyplot as plt

# Cargar datos ignorando comentarios
data = np.loadtxt("gyrate.xvg", comments=["@", "#"])

time = data[:, 0]
rg = data[:, 1]

plt.figure(figsize=(8,5))

plt.plot(time, rg, label="200 K", linewidth=2)

plt.xlabel("Time (ps)")
plt.ylabel("Radius of gyration (nm)")
plt.title("Radius of gyration")

plt.legend()
plt.grid(True, linestyle="--", alpha=0.4)

plt.tight_layout()
plt.savefig("gyrate_plot_200.png", dpi=300)
plt.show()
