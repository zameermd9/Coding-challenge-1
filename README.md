Task:

6 Axis robot simulation Using Python

GITHUB Link:

https://github.com/zameermd9/Coding-challenge-1

Inputs:

1.Enter the Desired angle of links with in the specified limits

Output:

1.We get the end effector Rotation and position at each and every point of Trace

Things i did in Building this Code:

1.I have chosen UR5 robot for the simulation purpose because UR5 robot is available in our University lab and its easy for me to verify the End effector position and Rotation.

2.Define the Robot’s Parameters:

I set the robot’s link lengths, offsets, and angles between the links using arrays. These parameters define the robot's structure.

3.Transformation Matrix:

I wrote a function to compute a matrix for each joint using the (DH) parameters. This matrix calculates the position and orientation of one joint relative to the previous one.

4.Calculate Forward Kinematics:

I created a function to compute the positions of all the robot's joints and the end effector based on the given joint angles. This helps in understanding where the arm will move.

5.Visualize the Robot:

I wrote a function to plot the robot in 3D. It shows the joints as points, the links as lines, and the path of the end effector as a dotted trace.

6.Smooth Motion Simulation:

I made a function to smoothly move the robot from an initial position to a final position by interpolating the angles. This ensures the movement looks natural.

7.Allow User Input:

The code lets users input final joint angles (within safe limits) to customize the robot’s final position.

8.3D Plotting:

Using matplotlib, I created a 3D plot that updates in real-time to show the robot’s movement and the end effector’s path.

9.Joint Angle Limits:

I set limits for each joint to prevent unrealistic or unsafe movements. The user must enter angles within these limits.

10.Real-Time Updates:

As the robot moves, I display the joint angles (in degrees) and the current position of the end effector at every step.

11.Trace Path of End Effector:

The program plots a dotted line to show the path traced by the end effector as the robot moves, making it easier to understand the motion.

12.Final Output:

Once the movement simulation is complete, the program prints the final joint angles and the exact position of the end effector.
