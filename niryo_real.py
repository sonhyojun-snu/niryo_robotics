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
   joint_target = [math.radians(45), -math.pi/4.0,math.pi/4.0, 1.57/2,0.0,0.0]
   n.move_joints(joint_target)


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
    print "원하는 동작을 입력하세요\n"
    robot_mode = input("1. 커피타기, 2.그림그리기 3.인사하기 :  ")
    
    if robot_mode == 1
        get_coffee()
    
   else if robot_mode == 2
        print("second movement done")
    
    else if robot_mode == 3
        n.move_pose(0.2, 0, 0.2, 0, math.radians(90), 0)
        next_pose = [0.25, 0.1, 0.2, 0.0, math.radians(90), 0.0]
        n.move_pose(*next_pose)

except NiryoOneException as e:
    print e
    # handle exception here
    # you can also make a try/except for each command separately

print "--- End"

