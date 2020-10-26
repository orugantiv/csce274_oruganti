#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32

rospy.init_node('test')

publisher = rospy.Publisher('total', Float32, queue_size=1)
rate = rospy.Rate(15) # 3 Hz

while not rospy.is_shutdown():
    publisher.publish(19)
    rate.sleep()
