# 3D A* Path Planning

This repository contains a 3D A* path planning algorithm that is simulated using ROS and CoppeliaSim.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [How the Code Works](#how-the-code-works)
- [Results](#results)

## Prerequisites

Before you can run this code, make sure you have the following installed on your Ubuntu system:

1. [ROS (Robot Operating System)](http://wiki.ros.org/ROS/Installation)
2. [CoppeliaSim](https://www.coppeliarobotics.com/previousVersions) - Download the appropriate version for your system.
3. Python libraries: `numpy`, `math`

## Getting Started

Follow these steps to set up and run the code:

1. Clone this repository and navigate to your workspace:

    ```bash
    mkdir -p ~/pathplanning/src
    cd ~/pathplanning
    catkin_init_workspace
    cd pathplanning/src
    catkin_create_pkg a_star_pathplanning std_msgs rospy
    cd pathplanning
    catkin build a_star_pathplanning
    source devel/setup.bash
    cd pathplanning/src/a_star_pathplanning
    mkdir scripts
    cd scripts
    ```

2. Paste the `a_star.py` file in the `scripts` directory and make it executable:

    ```bash
    sudo chmod +x a_star.py
    ```

3. Open a new terminal and add the following line to your `~/.bashrc` to avoid sourcing the workspace every time:

    ```bash
    echo "source ~/pathplanning/devel/setup.bash" >> ~/.bashrc
    ```

4. Start a ROS core in a new terminal:

    ```bash
    roscore
    ```

5. Open CoppeliaSim using the following commands:

    ```bash
    cd CoppeliaSim_Edu_V4_3_0_Ubuntu20_04/
    ./coppeliaSim.sh
    ```

    CoppeliaSim should open.

6. Load the scene `A_star_simulation_map.ttt` in CoppeliaSim.

7. Run the scene in CoppeliaSim.

8. Open a new terminal and run the following command to execute the Python script:

    ```bash
    rosrun a_star_pathplanning a_star.py
    ```

## How the Code Works

The code works by creating a 3D array map to represent walkable and non-walkable areas (e.g., `map[x, y, z] = 0` or `1`). After defining the map, two random points are chosen as start and end points. The algorithm follows this flowchart:

![Algorithm Flowchart](https://user-images.githubusercontent.com/106331831/236201740-8626b4d5-e1f8-4ea8-aebe-7ddca2a3137e.png)

## Results

Here are some visual results of the path planning algorithm:

![Result 1](https://user-images.githubusercontent.com/106331831/236013382-e2b344d6-5023-44ce-8e22-e5fd6a714716.png)

![Result 2](https://user-images.githubusercontent.com/106331831/236013215-c7be6e03-0e10-4e57-bfb5-853b973effb7.png)
