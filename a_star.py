#!/usr/bin/python3
#######################################################################################
#### 1. Importing Libraries needed for creating the pathplanning algorithm and communication between nodes 
import numpy as np
import math
import rospy
from geometry_msgs.msg import Quaternion
#######################################################################################
#### 2. Function that creates neighbors(children) of a node(parent) and puts them in a list
def successors(node):
    global Map
    List_successors=[]  #list of all successors
    for i in -1,0,1:
        for j in -1,0,1:
            for k in -1,0,1:
                if Map[node.position[0]+i,node.position[1]+j,node.position[2]+k]>0:
                    List_successors.append(node_class([node.position[0]+i,node.position[1]+j,node.position[2]+k],None,None,None,node,Map[node.position[0]+i,node.position[1]+j,node.position[2]+k]))
    
    for node in List_successors:
        if node.position==node.parent:  #remove the node if it is the parent
            List_successors.remove(node) 
    return List_successors
#######################################################################################
#### 3. Defining class for the nodes   
class node_class:
    def __init__(self, position,g,h,f,parent,Type):  
        self.parent = parent
        self.position = position
        self.g =g 
        self.h =h
        self.f =f 
        self.type=Type
#######################################################################################
#### 4. Function that calculates Euclidean distance
def distance(node,goal): 
    return math.dist(node.position,goal.position)  
#######################################################################################
#### 5. Function that finds the minimum h value among the nodes with the minimum f value
def get_minimum(List):
    min_f_list=[]
    min_value_f=1000
    min_value_h=1000
    min_index=0
    for i in range(len(List)):
        if List[i].f < min_value_f:
            min_value_f=List[i].f
            min_index = i

    for i in range(len(List)):
        if List[i].f == min_value_f:
            min_f_list.append(i)

    for i in min_f_list:
        if List[i].h < min_value_h:
            min_value_h=List[i].h
            min_index = i
    return List[min_index],min_index
#######################################################################################
#### 5. Function A* algorithm
def A_star(start,goal):
    open_list = []
    closed_list = []
    open_list.append(start)
    rate.sleep()
    while len(open_list) > 0:
        parent,index=get_minimum(open_list)
        
        pub.publish(Quaternion(((parent.position[0]+n)/(n*2))-3,((parent.position[1]+n)/(n*2))-3,(parent.position[2]-1)/(n*2),5))
        open_list.pop(index)
        childern=successors(parent)

        for child in childern:
            if child.position == goal.position:
                goal.parent=parent
                return goal

        for child in childern:
            g_cost=parent.g+distance(parent,child)
            h_cost=distance(child,goal)
            f_cost=g_cost+h_cost
            child.g=g_cost
            child.h=h_cost
            child.f=f_cost
            flag1=0
            flag2=0
            for i in range(len(open_list)):
                if child.position==open_list[i].position:
                    flag1=1
                    index1=i
                    break
            
            for i in range(len(closed_list)):
                if child.position==closed_list[i].position:
                    flag2=1
                    index2=i
                    break

            if(flag2==1):
                if(child.f<closed_list[index2].f):
                    closed_list[index2]=child
            elif(flag1==1):
                if(child.f<open_list[index1].f):
                    open_list[index1]=child
            else:
                open_list.append(child) 
        
        closed_list.append(parent)
#######################################################################################
#### 6. Function that generates list of coordinates of the path
def path_generation(path):  
    path_list_rev=[]  #list of all points in reverse
    path_list=[]  #list of all points
    while 1: #a loop that untangles 
        path_list_rev.append(path.position)
        path=path.parent
        if path==None:
            break

    for i in range(len(path_list_rev)):
        path_list.append(path_list_rev[len(path_list_rev)-1-i]) 
    return path_list
#######################################################################################
#### 7. Functions needed to create the map
def Draw_Horizontal(Array,Index1,Index2):   #Draws A horizontal Line from index1 to index2
	Local_Counter = Index1[1]
	while(Local_Counter <= Index2[1]):
		Array[Index1[0],Local_Counter,Index1[2]]= 0
		Local_Counter+=1

def Draw_Vertical(Array,Index1,Index2):    #Draws A Vertical Line from index1 to index2
	Local_Counter = Index1[0]
	while(Local_Counter <= Index2[0]):
		Array[Local_Counter,Index1[1],Index1[2]]= 0
		Local_Counter+=1


def Draw(Map):    #Draws a Map
    draw_counter=0
    global x,y,z,n
    while(draw_counter<x):
        Draw_Horizontal(Map,[draw_counter,0,0],[draw_counter,y-1,0])    #Draws bottom boundary
        Draw_Horizontal(Map,[draw_counter,0,1],[draw_counter,y-1,1])    #Draws 2nd bottom boundary
        Draw_Horizontal(Map,[draw_counter,0,z-1],[draw_counter,y-1,z-1])  #Draws top boundary
        
        draw_counter=draw_counter+1
    draw_counter=0

    while(draw_counter<z):
        Draw_Horizontal(Map,[0,0,draw_counter],[0,y-1,draw_counter])  #Draws left boundary
        Draw_Horizontal(Map,[x-1,0,draw_counter],[x-1,y-1,draw_counter])  #Draws right boundary
        Draw_Vertical(Map,[0,0,draw_counter],[x-1,0,draw_counter])      #Draws front boundary   
        Draw_Vertical(Map,[0,y-1,draw_counter],[x-1,y-1,draw_counter])  #Draws back boundary

        Draw_Horizontal(Map,[n*2,0,draw_counter],[n*2,y-3,draw_counter]) ####trial boundaries
        Draw_Horizontal(Map,[n*4,2,draw_counter],[n*4,y-1,draw_counter]) ####trial boundaries
        Draw_Horizontal(Map,[n*6,0,draw_counter],[n*6,y-3,draw_counter]) ####trial boundaries
        Draw_Horizontal(Map,[n*8,2,draw_counter],[n*8,y-1,draw_counter]) ####trial boundaries
        draw_counter=draw_counter+1
#######################################################################################
#### 8. Main function
if __name__ == '__main__':     # Main function that is executed 

    rospy.init_node('Path_planning', anonymous=True)
    pub = rospy.Publisher('/sim_ros_interface/map/state',Quaternion, queue_size=27000)

    rate = rospy.Rate(0.5) 
    rate2= rospy.Rate(1000)

    n = 2  #map resolution (keep it even and low or simulation will take a lot of time)
    x = (n*10)+1 #map dimensions x
    y = (n*10)+1 #map dimensions y
    z = 3*n    #map dimensions z
    Map = np.ones((x,y,z))  #map
    Draw(Map)  #draw map

    # define start and end also you can change them to try different paths
    start=node_class([1,1,1],0,0,0,None,2)  #position,g,h,f,parent,value
    goal=node_class([(n*9)-1,(n*9)-1,z-1],0,0,0,None,3)  #position,g,h,f,parent,value

    Map[start.position[0],start.position[1],start.position[2]]=start.type
    Map[goal.position[0],goal.position[1],goal.position[2]]=goal.type

    path = A_star(start,goal)
    final_path=path_generation(path)
    final_path.pop(0)  #remove start 
    final_path.pop(-1)  #remove end
    for i in final_path:
        Map[i[0],i[1],i[2]]=4   #assign all path points to value 4 

    pub.publish(Quaternion(0,0,0,6))   #send a dummy point
    rate.sleep()


    for i in range(x):
        for j in range(y):
            for k in range(1,z):
                pub.publish(Quaternion(((i+n)/(n*2))-3,((j+n)/(n*2))-3,(k-1)/n,Map[i,j,k]))  #send all points
                rate2.sleep()

