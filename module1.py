from niryo_one_python_api.niryo_one_api import *
import rospy
import time
import math

def get_coffee(n):
    n.set_arm_max_velocity(30)
    n.move_joints([0.029,0.491,-0.331,0.015,0.028,-0.010])
    n.change_tool(TOOL_GRIPPER_1_ID)
    n.close_gripper(TOOL_GRIPPER_1_ID,500)
    n.move_joints([0.223,-0.466,0.346,0.080,0.028,-0.010])
    n.open_gripper(TOOL_GRIPPER_1_ID,500)
    n.move_pose(0.188,0.103,0.321,2.137,1.461,2.744)
    n.move_pose(0.250,0.129,0.150,0.174,1.392,0.620)
    n.wait(0.1)
    n.close_gripper(TOOL_GRIPPER_1_ID,500)
    n.wait(2.0)
    n.move_pose(0.206,0.115,0.289,0.383,1.418,0.863)
    n.move_joints([-0.582,-0.039,-0.698,0.022,-0.783,-0.253])
    n.open_gripper(TOOL_GRIPPER_1_ID,500)
    n.change_tool(TOOL_NONE)
    
def say_hi(n):
    n.set_arm_max_velocity(50)
    n.move_joints([-0.034,0.497,-0.505,-0.029,0.014,-0.218])
    n.move_joints([-0.025,0.481,-0.500,-0.017,1.550,-0.025])
    n.move_joints([-0.039,0.540,-0.500,-0.574,1.550,-0.010])
    n.move_joints([-0.132,0.558,-0.500,0.387,1.550,-0.066])
    n.move_joints([-0.044,0.142,-1.289,0.137,0.002,-0.304])
    
    