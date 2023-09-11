import numpy as np
import matplotlib.pyplot as plt

ax = plt.axes(projection = "3d")

x_data = np.arange(-5,5,0.1)
y_data = np.arange(-5,5,0.1)

X,Y = np.meshgrid(x_data,y_data)

Z = np.sin(X) *np.cos(Y)


ax.plot_surface(X,Y,Z,cmap="plasma")

ax.view_init(azim = 0, elev =90)
ax.set_title("SOME FUNCTION")
ax.set_xlabel("My x values")
ax.set_ylabel("My y values")
ax.set_zlabel("fancy results")
plt.show()

#azimuth =0 & elevation = 90