#!/usr/bin/env python
#-*-coding: utf-8-*-

import rospy
import cv2
from cv_bridge import CvBridge
import numpy as np
from sensor_msgs.msg import CompressedImage

class Follower:
    def __init__(self):
        #self.image_callback = None
        rospy.init_node('follower')
        self.bridge = CvBridge()
        cv2.namedWindow("window", 1)
        rospy.Subscriber('/raspicam_node/image/compressed', CompressedImage, self.image_callback)
        rospy.spin()

    def image_callback(self, msg):
        np_arr =np.fromstring(msg.data, np.uint8)
        image_np = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        #image = self.bridge.imgmsg_to_cv2(msg)
        hsv = cv2.cvtColor(image_np, cv2.COLOR_BGR2HSV)

    	#lower_red = np.array([150, 50, 50])  # 빨강색 범위
    	#upper_red = np.array([180, 255, 255])


   	# mask2 = cv2.inRange(hsv, lower_red, upper_red)

    	# Bitwise-AND mask and original image

   	#res2 = cv2.bitwise_and(image, image, mask=mask2)  # 흰색 영역에 빨강색 마스크를 씌워줌.

        cv2.imshow('frame', hsv)  # 원본 영상을 보여줌
   	# cv2.imshow('red', res2)    # 마스크 위에 빨강색을 씌운 것을 보여줌.
        cv2.waitKey(3)


if __name__ == '__main__':
    follow = Follower()
