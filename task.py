import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

a, d = [0, -0.425, -0.39225, 0, 0, 0], [0.089159, 0, 0, 0.10915, 0.09465, 0.0823]
alpha = [np.pi / 2, 0, 0, np.pi / 2, -np.pi / 2, 0]

joint_limits = [
    (-360, 360),  #(Base)
    (-180, 180),  #(Shoulder)
    (-180, 180),  #(Elbow)
    (-360, 360),  #(Wrist 1)
    (-360, 360),  #(Wrist 2)
    (-360, 360)   #(Wrist 3)
]
#Transformation matrix
def dh_transform(theta, d, a, alpha):
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[c, -s * np.cos(alpha), s * np.sin(alpha), a * c],
                     [s, c * np.cos(alpha), -c * np.sin(alpha), a * s],
                     [0, np.sin(alpha), np.cos(alpha), d],
                     [0, 0, 0, 1]])
#forward kinematics
def forward_kinematics(joint_angles):
    T, positions = np.eye(4), [np.zeros(3)]
    for i in range(6):
        T = T @ dh_transform(joint_angles[i], d[i], a[i], alpha[i])
        positions.append(T[:3, 3])
    end_effector_position = T[:3, 3]
    return positions, end_effector_position
#robot plot
def plot_robot(ax, joint_positions, trace_points):
    ax.cla()
    colors = ['blue', 'green', 'red', 'orange', 'purple', 'cyan']
    for i in range(6):
        x, y, z = zip(joint_positions[i], joint_positions[i + 1])
        ax.plot(x, y, z, color=colors[i], lw=3, marker='o')
    ax.scatter(*joint_positions[-1], color='magenta', s=100, label="End Effector")

#plotting tracer
    if trace_points:
        trace_points = np.array(trace_points)
        ax.plot(trace_points[:, 0], trace_points[:, 1], trace_points[:, 2], 'gray', linestyle='--', label="Trace")

        ax.set(xlim=(-1, 1), ylim=(-1, 1), zlim=(0, 1), xlabel='X', ylabel='Y', zlabel='Z')
    ax.legend()
    plt.draw()
    plt.pause(0.1)



