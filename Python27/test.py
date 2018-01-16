from scipy.spatial import Delaunay
import numpy as np
import matplotlib.pyplot as plt

# Triangle Settings
width = 200
height = 40
pointNumber = 1000
points = np.zeros((pointNumber, 2))
points[:, 0] = np.random.randint(0, width, pointNumber)
points[:, 1] = np.random.randint(0, height, pointNumber)

# Use scipy.spatial.Delaunay for Triangulation
tri = Delaunay(points)

# Plot Delaunay triangle with color filled
center = np.sum(points[tri.simplices], axis=1)/3.0
color = np.array([(x - width/2)**2 + (y - height/2)**2 for x, y in center])
plt.figure(figsize=(7, 3))
plt.tripcolor(points[:, 0], points[:, 1], tri.simplices.copy(), facecolors=color, edgecolors='k')


# Delete ticks, axis and background
plt.tick_params(labelbottom='off', labelleft='off', left='off', right='off',
                bottom='off', top='off')
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['top'].set_color('none')

# Save picture
plt.savefig('Delaunay.png', transparent=True, dpi=600)
