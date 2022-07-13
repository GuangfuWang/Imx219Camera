# Basic ROS 2 program to publish real-time streaming video 
# from your built-in camera.
# Author:
# - Guangfu WANG
# - thuwgf@gmail.com

# importing all dependencies.
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import os


def gstreamer_pipeline(
  capture_width=1280,
  capture_height=720,
  display_width=640,
  display_height=360,
  framerate=30,
  flip_method=0,
  ):
  return (
      "nvarguscamerasrc ! "
      "video/x-raw(memory:NVMM),"
      "width=(int)%d, height=(int)%d, "
      "format=(string)NV12, framerate=(fraction)%d/1 ! "
      "nvvidconv flip-method=%d ! "
      "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
      "videoconvert ! "
      "video/x-raw, format=(string)BGR ! appsink"
      % (
          capture_width,
          capture_height,
          framerate,
          flip_method,
          display_width,
          display_height,
      )
  )
  


class Imx219Publisher(Node):
  def __init__(self):
    super().__init__('imx219_pub_node')
    
    self.publisher_ = self.create_publisher(Image,'imx219cam',30)

    time_period = 1/30
    self.timer = self.create_timer(time_period,self.timer_callback)

    self.cap = cv2.VideoCapture(gstreamer_pipeline(flip_method=0),cv2.CAP_GSTREAMER)

    self.br = CvBridge()

  def timer_callback(self):
    ret,frame = self.cap.read()
    if ret == True:
      self.publisher_.publish(self.br.cv2_to_imgmsg(frame))
    self.get_logger().info("Publishing images from imx219")

def main(args=None):
  rclpy.init(args=args)

  imagePub = Imx219Publisher()
  rclpy.spin(imagePub)

  imagePub.destroy_node()

  rclpy.shutdown()

if __name__ == '__main__':
  main()

