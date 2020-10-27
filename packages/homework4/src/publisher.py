#!/usr/bin/env python3
# i used this video https://www.youtube.com/watch?v=xcQcs0wJ7GE&feature=emb_logo
import rospy
from std_msgs.msg import Float32

rospy.init_node('talker')

publisher = rospy.Publisher("homework1/delta", Float32, queue_size=1)
rate = rospy.Rate(15) # 3 Hz

while not rospy.is_shutdown():
    publisher.publish(19)
    rate.sleep()

