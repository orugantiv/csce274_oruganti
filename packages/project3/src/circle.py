#!/usr/bin/env python3
#i used class slides
import rospy
from duckietown_msgs.msg import Twist2DStamped

rospy.init_node('circle')

publisher = rospy.Publisher("car_cmd_switch_node/cmd", Twist2DStamped, queue_size=1)
msg= Twist2DStamped(header=None, v='0.1',omega='0')
sleep(3)
msg= Twist2DStamped(header=None, v='0.1',omega='0')

while not rospy.is_shutdown():
    publisher.publish(msg)
    rate.sleep()

