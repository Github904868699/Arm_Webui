import rospy
from std_msgs.msg import String
from apriltag_ros.msg import AprilTagDetectionArray

def Localizer_init():
    
    sub = rospy.Subscriber("tag_detections", AprilTagDetectionArray, number_callback, queue_size=10)
    
def number_callback(msg):

    last_msg_ = msg
    print(msg)
    

if __name__ == "__main__":

    rospy.init_node("apriltag_detector_subscriber")
    localizer = Localizer_init()
    rospy.spin()

                                                                                                                            