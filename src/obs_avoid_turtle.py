#!/usr/bin/env python3
from sensor_msgs.msg import LaserScan # LaserScan type message is defined in sensor_msgs
import rospy                          #  ROS Python Library
from geometry_msgs.msg import Twist   #

def return_back (dt):
    threshold_1 = 0.7 # Laser scan range threshold
    threshold_2 = 0.7
    print('-------------------------------------------')
    print('Range data at 0 deg:   {}'.format(dt.ranges[0]))
    print('Range data at 15 deg:  {}'.format(dt.ranges[15]))
    print('Range data at 345 deg: {}'.format(dt.ranges[345]))
    print('-------------------------------------------')
    
    if dt.ranges[0]>threshold_1 and dt.ranges[20]>threshold_2 and dt.ranges[350]>threshold_2:  #obstacle check infront
                                                                         # 20 degrees left and right
									                                     # Threshold angle range
        
        turn_move.angular.z = 0.0 # rotate with angular velocity
        turn_move.linear.x = 0.5 # go forward with linear velocity
    else:
        turn_move.linear.x = 0.0 # to stop the linear motion of the robot
        turn_move.angular.z = 1.0 # rotate anti-clockwise # for clockwise change the number to -2.0
        if dt.ranges[0]>threshold_1 and dt.ranges[15]>threshold_2 and dt.ranges[345]>threshold_2:
            turn_move.linear.x = 0.5
            turn_move.angular.z = 0.0
    pub.publish(turn_move)         # publishing turn_move object

turn_move = Twist()                # Twist message type object created
rospy.init_node('obstacle_avoid_node') # Initializes a node
pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)  # Publisher object which will publish "Twist" type messages
                            				 # on the "/cmd_vel" Topic, "queue_size" is the size of the
                                                         

sub = rospy.Subscriber("/scan", LaserScan, return_back )  # Subscriber object which will listen "LaserScan" type messages
                                                      # from the "/scan" Topic and call the "return_back" function
						      # each time it reads something from the Topic

rospy.spin() #kill the program with ctrl+c which closes the infinite loops

