







import cv2
import rospy
import numpy as np
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg    import CompressedImage

class ImageAnalysis:
    def __init__(self):
        self.sub = rospy.Subscriber('rpi_image', CompressedImage, self.analyze_image)

        @staticmethod
        def imfill(bw_image):
            h, w = bw_image.shape[:2]
            im_filled = bw_image.copy()

        @staticmethod
        def create_mask(base_image):
            lower1 = np.array([0, 130, 20])
            upper1 = np.array([10, 255, 255])
            lower2 = np.array([165, 130, 20])
            upper2 = np.array([179, 255, 255])

            lower_mask = cv2.inRange(base_image, lower1, upper1)
            upper_mask = cv2.inRange(base_image, lower2, upper2)

            full_mask = lower_mask + upper_mask
            return imfill(full_mask)

    def analyze_image(self, msg):
        bridge = CvBridge()
        try:
            self.image = bridge.compressed_imgmsg_to_cv2(msg, "brg8")
            rospy.loginfo("Image was received")
        except CvBridgeError as e:
            print(e)
        hsv_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)

        mask = create_mask(hsv_image)
        masked_image =cv2.bitwise_and(self.image, self.image, mask=mask)

        cv2.imshow('original', self.image)
        cv2.imshow('masked', masked_image)
        key = cv2.waitkey(0)
        if key==27 or key==old('q'):
            cv2.destroyWindows()
        rospy.loginfo("image was analyzed")

        
if __name__ == "__main__":
    rospy.init_node("image_analize")
    ImageAnalysis()
    rospy.spin()
