#!/usr/bin/python

# Company : ITESM - Campus Qro
# Author : Israel Ivan Arroyo P A01706190
# Project name : camera.py
# target device: AR parrot drone 2, 2.3.3 frimware version
# target simulation: gazebo v9.0.0 with tum_simulator_meodic ros library
# tool version : python 2.7.17
# Description: Make drone follow a green line

import rospy
from std_msgs.msg import String
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist
from ardrone_autonomy.msg import Navdata

from sensor_msgs.msg import Image
from cv_bridge import CvBridge,CvBridgeError

from ar_track_alvar_msgs.msg import AlvarMarkers

import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from math import sin,cos,pi
KP = 6
KI = 0
KD = 0
TARGET = (0,0,0)

class Quadrotor:

    def __init__(self):
        self.cmdPub = rospy.Publisher("cmd_vel",Twist, queue_size=10)
        self.takeoffPub = rospy.Publisher("ardrone/takeoff", Empty, queue_size=10)
        self.navdataSub = rospy.Subscriber("/ar_pose_marker",AlvarMarkers,self.tagCallback)
        self.auxRate = 15.0 #Hz
        self.rate = rospy.Rate(15)
        self.dt = float(1.0/self.auxRate) #ultima vez que se llamo la func(s)
        self.error = 0
        self.i_error = 0
        self.d_error=0
        self.last_error = 0
        self.auxiliar = [0]*100
        self.i = 0

    def takeoff(self):
        # despegar
        while (not rospy.is_shutdown()):# and (self.navdataVar.altd != 800):
            # print(self.navdataVar.altd)
            self.takeoffPub.publish(Empty())
            self.rate.sleep()

    def tagCallback(self,data):
        if data.markers:
            # print(data.markers[0].pose.pose)
            self.error = 0 - data.markers[0].pose.pose.orientation.z
            self.i_error+= self.error*self.dt
            self.d_error = (self.error - self.last_error)/self.dt
            self.last_error = self.error
            self.velCommand(KP*self.error + KI*self.i_error + KD*self.d_error)
        else:
            self.velCommand(0)
            print("no markers")



    def velCommand(self,x_in):
        # self.auxiliar[self.i] = x_in
        vel = Twist()
        vel.linear.x = x_in
        self.cmdPub.publish(vel)
        # self.i +=1
        # if self.i == 99:
        #     plt.plot(self.auxiliar)
        #     plt.show()
        #     self.i = 0


if __name__ == '__main__':
  try:
      print("start")
      rospy.init_node('movement',anonymous=True)
      quad = Quadrotor()
      rospy.spin()
    #   quad.takeoff()

  except rospy.ROSInterruptException:
      pass