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

#plotting tracer for the end effector
    if trace_points:
        trace_points = np.array(trace_points)
        ax.plot(trace_points[:, 0], trace_points[:, 1], trace_points[:, 2], 'gray', linestyle='--', label="Trace")

        ax.set(xlim=(-1, 1), ylim=(-1, 1), zlim=(0, 1), xlabel='X', ylabel='Y', zlabel='Z')
    ax.legend()
    plt.draw()
    plt.pause(0.1)

def simulate_motion(ax, initial_angles, final_angles, steps=50):
    #simulation with smooth movement
    trace_points = []
    for t in np.linspace(0, 1, steps):
        # Smooth interpolation between initial and final angles
        interpolated_angles = initial_angles + t * (final_angles - initial_angles)
        
        # forward kinematics computation
        joint_positions, end_effector_position = forward_kinematics(interpolated_angles)
        
        # joint_angles(degrees)
        joint_angles_degrees = np.degrees(interpolated_angles)
        
        # Printing joint angles and endeffector position at each and every step
        print(f"Step {int(t * steps)}:")
        print(f"  Joint Angles (degrees): {joint_angles_degrees}")
        print(f"  End Effector Position: ({end_effector_position[0]:.2f}, {end_effector_position[1]:.2f}, {end_effector_position[2]:.2f})")
        
        # To store the Trace of End effector position
        trace_points.append(end_effector_position)
        
        #plotting robot and its movements
        plot_robot(ax, joint_positions, trace_points)
    
    # End output after simulation
    print("\nFinal Configuration Reached:")
    print(f"  Joint Angles (degrees): {np.degrees(final_angles)}")
    print(f"  End Effector Position: ({end_effector_position[0]:.2f}, {end_effector_position[1]:.2f}, {end_effector_position[2]:.2f})")

#Allowing users to input joint angles with in the limits of UR5  
def get_joint_angles():
    angles = []
    for i, (min_angle, max_angle) in enumerate(joint_limits):
        while True:
            try:
                angle = float(input(f"Enter angle for Joint {i + 1} (range: {min_angle}° to {max_angle}°): "))
                if min_angle <= angle <= max_angle:
                    angles.append(angle)
                    break
                else:
                    print(f"Angle out of range! Please enter a value between {min_angle}° and {max_angle}°.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
    return angles

def main():
    # Initial Angles(Default)
    initial_angles_deg = [90, 0, -90, 0, 0, 0]
    print("Initial joint angles are set to (90, 0, -90, 0, 0, 0)")

    # Final Joint Angles
    print("\nEnter the final joint angles:")
    final_angles_deg = get_joint_angles()

    # degrees to radians conversion
    initial_angles_rad = np.radians(initial_angles_deg)
    final_angles_rad = np.radians(final_angles_deg)

    # 3D plot creation
    fig, ax = plt.figure(), plt.axes(projection='3d')

    #smooth movement simulation
    simulate_motion(ax, initial_angles_rad, final_angles_rad)

    plt.show()

if __name__ == "__main__":
    main()



