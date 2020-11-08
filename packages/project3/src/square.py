import rospy
from duckietown_msgs.msg import Twist2DStamped
from time import sleep

def square():
    rotate=2.4
    stright=0.0
    velocity=0.4
    count=0
    while(count<4):
        pub = rospy.Publisher("car_cmd_switch_node/cmd", Twist2DStamped, queue_size=10)
        rospy.init_node('Square')
        pub.publish(Twist2DStamped(header=None, v=0.4,omega=0.2))
        sleep(2.5)
        pub.publish(Twist2DStamped(header=None, v=0.0,omega=0))
        sleep(1)
        pub.publish(Twist2DStamped(header=None, v=0.0,omega=rotate))
        sleep(1)
        count+=1
    pub.publish(Twist2DStamped(header=None, v=0.0,omega=0))

if __name__ == '__main__':
    square()

