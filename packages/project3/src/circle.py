#!/usr/bin/env python3
#i used class slides
import rospy
from duckietown_msgs.msg import Twist2DStamped
from time import sleep

def circle():

    pub = rospy.Publisher("car_cmd_switch_node/cmd", Twist2DStamped, queue_size=10)
    rospy.init_node('Circle')
    pub.publish(Twist2DStamped(header=None, v=0.5,omega=0.0))
    sleep(10)
    pub.publish(Twist2DStamped(header=None, v=0.0,omega=0))

if __name__ == '__main__':
    circle()

