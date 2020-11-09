#!/usr/bin/env python3
import rospy
from duckietown_msgs.msg import Twist2DStamped
from time import sleep

def square():
    pub = rospy.Publisher("car_cmd_switch_node/cmd", Twist2DStamped, queue_size=10)
    rospy.init_node('Square')

    rotate=1.55
    stright=0.0
    velocity=0.4
    i=0

    while (i<4):
        pub.publish(Twist2DStamped(header=None, v=velocity,omega=0.0))
        sleep(2.5)
        pub.publish(Twist2DStamped(header=None, v=0.0,omega=rotate))
        sleep(1)
        i+=1

    pub.publish(Twist2DStamped(header=None, v=0.0,omega=0))

if __name__ == '__main__':
    square()

