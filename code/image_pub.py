







import cv2
import rospy
import numpy as np
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import CompressedImage

class ImageCapture:
    def __imit__(self, capture_rate=10.0, publish_rate=5.0):
        self.image = np.empty((640, 480), dtype=np.uint8)
        self.pub = rospy.Publisher('rpi_image', CompressedImage, queue_size=1)
        rospy.Timer(rospy.Duration(1/capture_rate), self.capture_image)
        rospy.Timer(rospy.Duration(1/publish_rate), self.pulish_image)

    def capture_image(self, event=None):
        cam = cv2.VideoCapture("/dev/video0", cv2.CAP_V4L)
        cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        ret = False
        while not ret:
            ret, frame = cam.read()
        self.image = frame
        rospy.loginfo("image was captured")
        cam.release()

    def publish_image(self, event=None):
        bridge = CvBridge()
        try:
            msg = bridge.cv2_to_compressed_imgmsg(self.image)
        except CvBridgeError as e:
            print(e)
        self.pub.publish(msg)
        rospy.loginfo("image was published")

    if __name__ == "__main__":
        rospy.init_node("image_capture")
        ImageCapture(capture_image(4.0, publish_rate=2.0))
        rospy.spin()

