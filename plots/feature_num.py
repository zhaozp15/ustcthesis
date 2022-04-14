import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5, 6, 10])
y = np.array([62.95, 66.42, 67.42, 67.79, 68.15, 68.42, 68.62])

fig, ax = plt.subplots()

# ax.set_xlim(0, 11)
ax.set_xticks(np.arange(1, 11, 1))
ax.set_yticks(np.arange(62, 70, 1))
ax.set_xlabel('Num of features')
ax.set_ylabel('Accuracy (%)')
ax.plot(x, y, 'o-')

fig.savefig('/home/admin/workspace/ustcthesis/figures/feature_num.pdf')