#!/usr/bin/env python

# To use the API, copy these 4 lines on each Python file you create
from niryo_one_python_api.niryo_one_api import *
import rospy
import time
import math

rospy.init_node('niryo_one_example_python_api')

print "--- Start NiryoOne"

n = NiryoOne()

def get_coffee():
    n.set_arm_max_velocity(30)
    n.move_joints([0.029,0.491,-0.331,0.015,0.028,-0.010])
    n.change_tool(TOOL_GRIPPER_2_ID)
    n.close_gripper(TOOL_GRIPPER_2_ID,500)
    n.move_joints([0.223,-0.466,0.346,0.080,0.028,-0.010])
    n.open_gripper(TOOL_GRIPPER_2_ID,500)
    n.move_pose(0.188,0.103,0.321,2.137,1.461,2.744)
    n.move_pose(0.250,0.129,0.150,0.174,1.392,0.620)
    n.wait(0.1)
    n.close_gripper(TOOL_GRIPPER_1_ID,500)
    n.wait(2.0)
    n.move_pose(0.206,0.115,0.289,0.383,1.418,0.863)
    n.move_joints([-0.582,-0.039,-0.698,0.022,-0.783,-0.253])
    n.open_gripper(TOOL_GRIPPER_1_ID,500)
    n.change_tool(TOOL_NONE)

   

try:
    # Calibrate robot first
    n.calibrate_auto()
    print "Calibration finished!\n"

    time.sleep(1)

    # Test learning mode
    #n.activate_learning_mode(False)
    #print "Learning mode activated? "
    #print n.get_learning_mode()

    # Work
    robot_mode = 0
    while robot_mode != 4:
        print "Choose number what you want\n"
        robot_mode = input("1. coffee, 2.drawing 3.Hi 4. Quit :  ")

        if robot_mode == 1:
            get_coffee()

        if robot_mode == 2:
            print("second movement done")

        if robot_mode == 3:
            n.move_pose(0.2, 0, 0.2, 0, math.radians(90), 0)
            next_pose = [0.25, 0.1, 0.2, 0.0, math.radians(90), 0.0]
            n.move_pose(*next_pose)
    n.move_joints([0.047,0.008,-0.953,0.084,0.017,-0.005])
    n.activate_learning_mode(True)
except NiryoOneException as e:
    print e
    # handle exception here
    # you can also make a try/except for each command separately

print "--- End"









