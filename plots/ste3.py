import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    s = 1 / (1 + np.exp(-x))
    return s

def d_sigmoid(x):
    return sigmoid(x) * (1 - sigmoid(x))

fig, axs = plt.subplots(1, 2, figsize=(11, 5))

beta = 1
x = np.arange(-4, 4.001, 0.001)
y = 2 * sigmoid(beta * x) * (1 + beta * x * (1 - sigmoid(beta * x))) - 1
dy = 2 * d_sigmoid(beta * x) * beta * (1 + beta * x * (1 - sigmoid(beta * x))) + 2 * sigmoid(beta * x) * (beta * (1 - sigmoid(beta * x)) + beta * x * (-1 * d_sigmoid(beta * x) * beta))

for ax in axs:
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.grid()

axs[0].set(xlabel='x', ylabel='forward function')
axs[1].set(xlabel='x', ylabel='gradient function')
axs[0].plot(x, y, lw=3)
axs[1].plot(x, dy, lw=3)

fig.savefig('/home/admin/workspace/ustcthesis/figures/ste3.pdf')