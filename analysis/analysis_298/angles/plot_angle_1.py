import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("angaver_1.xvg", comments=["@", "#"])

time = data[:, 0]
angle2 = data[:, 1]

plt.figure(figsize=(8,5))

plt.plot(time, angle2, linewidth=2, label="CA-CB-CG (ARG)")

plt.xlabel("Time (ps)")
plt.ylabel("Angle (degrees)")
plt.title("Angle at 298 K")

plt.legend()
plt.grid(True, linestyle="--", alpha=0.4)

plt.tight_layout()
plt.savefig("angle_CA-CB-CG.png", dpi=300)
plt.show()
