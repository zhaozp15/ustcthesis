import numpy as np
import matplotlib.pyplot as plt

fig, axs = plt.subplots(1, 2, figsize=(11, 5))

x = np.arange(-4, 4.001, 0.001)
y = (-1 * (x < -1)
    + x * (x > -1) * (x < 1)
    + 1 * (x > 1))
dy = 1 * (x > -1) * (x < 1)

for ax in axs:
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.grid()

axs[0].set(xlabel='x', ylabel='forward function')
axs[1].set(xlabel='x', ylabel='gradient function')
axs[0].plot(x, y, lw=3)
axs[1].plot(x, dy, lw=3)

fig.savefig('/home/admin/workspace/ustcthesis/figures/ste1.pdf')