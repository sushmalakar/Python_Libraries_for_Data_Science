import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

# Generate data
x = np.linspace(-5,5,100)
y= np.linspace(-5,5,100)
X, Y =np.meshgrid(x,y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# Create a figure and a 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create and empty 3D wireframe plot
wireframe = ax.plot_wireframe(X,Y,Z)

ax.set_title('Self-Rotating 3D Wireframe Plot')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

# Function to update the plot during animation
def update(frame):
    # Clear previous plot
    ax.clear()

    # Update data for the wireframe plot
    new_Z = np.sin(np.sqrt((X+frame/50)**2 + (Y+frame/50)**2))
    wireframe = ax.plot_wireframe(X, Y, new_Z, color="b")

    # Set plot title and labels
    ax.set_title('Self-Rotating 3D Wireframe Plot')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')

    # Set view angle for rotation
    ax.view_init(elev=30, azim=frame)
    return wireframe,

# Create an animation
ani = animation.FuncAnimation(fig,update,frames=np.arange(0,360,2), interval=50, blit=False)

plt.show()