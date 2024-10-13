import matplotlib.pyplot as plt
import numpy as np

def draw_triangle(ax, x, y, size, upside_down=False):
    height = (np.sqrt(3) / 2) * size
    triangle = np.array([[x, y],
                             [x - size / 2, y - height],
                             [x + size / 2, y - height],
                             [x, y]])
    ax.plot(triangle[:, 0], triangle[:, 1], color='black')

fig, ax = plt.subplots()
ax.set_aspect('equal')

rows = 6
size = 3

for row in range(rows):
    for col in range(rows - row):
        x = col * size - (rows - row - 1) * size / 2
        y = -row * (np.sqrt(3) / 2) * size
        draw_triangle(ax, x, y, size)

ax.axis('off')
plt.savefig("patipuja.png")
