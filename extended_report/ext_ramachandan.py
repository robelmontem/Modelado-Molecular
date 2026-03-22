import numpy as np
import matplotlib.pyplot as plt

# ---------- Lectura ----------
ala = np.loadtxt("rama_ALA.dat")
arg = np.loadtxt("rama_ARG.dat")
met = np.loadtxt("rama_MET.dat")

# ---------- Clasificación aproximada ----------
# Es una clasificación práctica para el informe.
# Sirve para identificar la región dominante del mapa.
def classify_region(phi, psi):
    # alpha_R
    if (-160 <= phi <= -30) and (-90 <= psi <= 45):
        return "αR"
    # beta / extended
    if (-180 <= phi <= -60) and (90 <= psi <= 180):
        return "β"
    # alpha_L
    if (30 <= phi <= 100) and (0 <= psi <= 120):
        return "αL"
    return "other"

def summarize_regions(data, name):
    labels = [classify_region(phi, psi) for phi, psi in data]
    total = len(labels)
    counts = {}
    for lab in labels:
        counts[lab] = counts.get(lab, 0) + 1

    print(f"\n{name}")
    for lab, count in sorted(counts.items(), key=lambda x: x[1], reverse=True):
        print(f"  {lab}: {count:6d} frames ({100*count/total:6.2f}%)")

    dominant = max(counts, key=counts.get)
    print(f"  Dominant conformation: {dominant}")
    return counts

# ---------- Resumen por regiones ----------
counts_ala = summarize_regions(ala, "ALA")
counts_arg = summarize_regions(arg, "ARG")
counts_met = summarize_regions(met, "MET")

# ---------- Función de ploteo ----------
def plot_rama(ax, data, title):
    phi = data[:, 0]
    psi = data[:, 1]

    h = ax.hist2d(
        phi, psi,
        bins=72,
        range=[[-180, 180], [-180, 180]],
        density=True
    )

    ax.set_xlim(-180, 180)
    ax.set_ylim(-180, 180)
    ax.set_xticks([-180, -90, 0, 90, 180])
    ax.set_yticks([-180, -90, 0, 90, 180])
    ax.set_xlabel("φ (degrees)")
    ax.set_ylabel("ψ (degrees)")
    ax.set_title(title)

    # marcar máximos de densidad
    H, xedges, yedges = np.histogram2d(
        phi, psi,
        bins=72,
        range=[[-180, 180], [-180, 180]],
        density=True
    )
    idx = np.unravel_index(np.argmax(H), H.shape)
    phi_center = 0.5 * (xedges[idx[0]] + xedges[idx[0] + 1])
    psi_center = 0.5 * (yedges[idx[1]] + yedges[idx[1] + 1])
    ax.plot(phi_center, psi_center, marker="x", markersize=10, mew=2)
    ax.text(phi_center + 5, psi_center + 5,
            f"max density\n({phi_center:.1f}, {psi_center:.1f})",
            fontsize=8)

    return h

# ---------- Figura ----------
fig, axes = plt.subplots(1, 3, figsize=(15, 4.8), sharex=True, sharey=True)

h = plot_rama(axes[0], ala, "ALA")
plot_rama(axes[1], arg, "ARG")
plot_rama(axes[2], met, "MET")

cbar = fig.colorbar(h[3], ax=axes, shrink=0.9)
cbar.set_label("Density")

plt.tight_layout()
plt.savefig("ext_ramachandran_three_residues.png", dpi=300)
plt.show()
