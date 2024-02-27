#! /usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

if __name__ == '__main__' :
    rospy.init_node('velocity_publisher')
    rospy.loginfo("It has started yoooo")

    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    rate = rospy.Rate(2)

while not rospy.is_shutdown():
    move = Twist()
    move.linear.x = 0.22 #max speed is 0.22
    move.angular.z = 1.0 #limited angular velocity is -2.84 to 2.84
    pub.publish(move)
    rate.sleep()

