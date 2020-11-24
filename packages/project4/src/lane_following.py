#!/usr/bin/env python3
import rospy
from duckietown_msgs.msg import Twist2DStamped,LanePose,BoolStamped

from time import sleep

class lanefollowing:
    def __init__(self):

        self.previous_error_d = 0
        self.set_point_d = 0.19
        self.kp_d=5.5
        self.kd_d=6
        self.dt=0.1
        self.previous_error_phi=0
        self.set_point_phi =0.05
        self.kp_phi=4.5
        self.kd_phi=1.2
        self.d=0
        self.phi=0
        self.pub = rospy.Publisher("lane_controller_node/car_cmd", Twist2DStamped, queue_size=10)
        self.avg=0
    def pd_controller_d(self,val):
        self.error = self.set_point_d - val
        self.derivative = (self.error - self.previous_error_d)/self.dt
        self.previous_error_d = self.error
        return self.kp_d*self.error + self.kd_d*self.derivative

    def pd_controller_phi(self,val):
        self.error = self.set_point_phi - val
        self.derivative = (self.error - self.previous_error_phi)/self.dt
        self.previous_error_phi = self.error
        return self.kp_phi*self.error + self.kd_phi*self.derivative


    def callback(self,data):
        self.dt=data.header.stamp.nsecs*10**-9
        self.d=data.d
        self.d=self.pd_controller_d(self.d)
        self.phi=self.pd_controller_phi(data.phi)
        if (self.phi>4):
            self.pub.publish(Twist2DStamped(header=None, v=0.2,omega=4))
        elif (self.phi<-4):
            self.pub.publish(Twist2DStamped(header=None, v=0.2,omega=-4))
        else:
            self.pub.publish(Twist2DStamped(header=None, v=0.4,omega=self.phi))
        rospy.loginfo(rospy.get_caller_id() + 'This is by V.N.Anirudh Oruganti LANE FOLLOWING CODE. phi %s', self.phi)

    def listener(self):
        rospy.init_node('listener')
        rospy.Subscriber('lane_filter_node/lane_pose', LanePose, self.callback)
        #self.pd_controller_d(self.d)
        rospy.spin()
if __name__ == '__main__':
   i=lanefollowing()
   i.listener()


