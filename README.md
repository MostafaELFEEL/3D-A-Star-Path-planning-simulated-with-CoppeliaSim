# 3D-A-Star-Path-planning
A* path planning algorithm simulated using ROS and CoppeliaSim.

steps to start code:-

1- You must have ROS and CoppeliaSim installed on Ubuntu first. 

2- Install all needed libraries(numpy, math)

3- Open terminal and paste the following:

- mkdir -p ~/pathplanning/src
- cd ~/pathplanning
- catkin_init_workspace
- cd pathplanning/src        --(go to src)--
- catkin_create_pkg a_star_pathplanning std_msgs rospy
- cd pathplanning            --(return to workspace)--
- catkin build a_star_pathplanning
- source devel/setup.bash
- cd pathplanning/src/a_star_pathplanning    --(go to package)--
- mkdir scripts
- cd scripts
- Paste a_star.py file in this directory
- sudo chmod +x a_star.py
- cd               --(return to home)--
- echo "source ~/pathpanning/devel/setup.bash" >> ~/.bashrc   --(so you don't need to source every time you open a new terminal)--

then you are ready to run the file.

4- run roscore in a new terminal.

5- open coppeliaSim using the following commands:

- cd CoppeliaSim_Edu_V4_3_0_Ubuntu20_04/
- ./coppeliaSim.sh

CoppeliaSim should open.

6- Then open the following scene A_star_simulation_map.ttt

7- Run the simulation first.

8- Then open a new terminal and run the following command:

- rosrun a_star_pathplanning a_star 


results:-


![image](https://user-images.githubusercontent.com/106331831/236013215-c7be6e03-0e10-4e57-bfb5-853b973effb7.png)

![image](https://user-images.githubusercontent.com/106331831/236013216-be6a8fb7-7b31-406d-b5fa-294a69327fd1.png)
