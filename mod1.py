#!/usr/bin/env python

# To use the API, copy these 4 lines on each Python file you create
from niryo_one_python_api.niryo_one_api import *
import rospy
import time
import math
import module1

rospy.init_node('niryo_one_example_python_api')

print "--- Start NiryoOne"

n = NiryoOne()

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
            module1.get_coffee(n)

        if robot_mode == 2:
            print("second movement done")

        if robot_mode == 3:
            module1.say_hi(n)
            

    n.move_joints([0.047,0.008,-0.953,0.084,0.017,-0.005])
    n.activate_learning_mode(True)
except NiryoOneException as e:
    print e
    # handle exception here
    # you can also make a try/except for each command separately

print "--- End"









