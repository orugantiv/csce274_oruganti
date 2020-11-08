#!/usr/bin/env python3
import rospy
from duckietown_msgs.msg import Twist2DStamped
from time import sleep

def circle():
    #On lecture slides "lec07.pdf", there was a formula given to find omega for the robot
    #to go in a circle with a radius and choosen velocity. Formula omega=velocity/(radius-(length/2)) 
    velocity=0.4# desired velocity
    diameter=1# desired diameter of the circle in meters
    radius=diameter/2#radius of the circle in meters
    length=0.0762#length between two wheels in meters
    omga=velocity/(radius-(length/2))
    pub = rospy.Publisher("car_cmd_switch_node/cmd", Twist2DStamped, queue_size=10)
    rospy.init_node('Circle')
    pub.publish(Twist2DStamped(header=None, v=velocity,omega=omga))
    sleep(15)
    pub.publish(Twist2DStamped(header=None, v=0.0,omega=0))

if __name__ == '__main__':
    circle()
