#!/usr/bin/env python3
import rospy
from duckietown_msgs.msg import Twist2DStamped,LanePose,BoolStamped

from time import sleep
def callback(data):
    return print()
def value(bo):
    return bo.data
def listener():
    pub = rospy.Publisher("lane_controller_node/car_cmd", Twist2DStamped, queue_size=10)
    rospy.init_node('listener')
    stat= rospy.Subscriber("lane_controller_node/switch", BoolStamped, value)
    pub.publish(Twist2DStamped(header=None, v=1,omega=0))
if __name__ == '__main__':
    stat= rospy.Subscriber("lane_controller_node/switch", BoolStamped, value)

    while (stat):
        stat= rospy.Subscriber("lane_controller_node/switch", BoolStamped, value)
        listener()
    rospy.spin()

