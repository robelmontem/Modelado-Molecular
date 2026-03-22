import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("angaver_0.xvg", comments=["@", "#"])

time = data[:, 0]
angle1 = data[:, 1]

plt.figure(figsize=(8,5))

plt.plot(time, angle1, linewidth=2, label="N-CA-C (ALA)")

plt.xlabel("Time (ps)")
plt.ylabel("Angle (degrees)")
plt.title("Angle at 400 K")

plt.legend()
plt.grid(True, linestyle="--", alpha=0.4)

plt.tight_layout()
plt.savefig("angle_N-CA-C.png", dpi=300)
plt.show()
