import rospy, sys
from armcontrol_demo_pkg.msg import hdrarm_msg
from apriltag_ros.msg import AprilTagDetectionArray

global nt

def Localizer_init():
    global nt
    nt = 0
    sub = rospy.Subscriber("tag_detections", AprilTagDetectionArray, number_callback, queue_size=10)
    
def number_callback(msg):
    global nt

    pub = rospy.Publisher("target_position", hdrarm_msg, queue_size=10)
    
    data = hdrarm_msg()
    # rospy.loginfo("接收位姿:%s", msg)
    data.arm_mode = 'arm_control_moveit_ik' #arm_control_moveit_fk
    data.arm_position_x = -(msg.detections[0].pose.pose.pose.position.x + 0.075)*0.5 + 0.0795
    data.arm_position_y = (msg.detections[0].pose.pose.pose.position.y - 0.12)*0.5 + 0.2720
    data.arm_position_z = 0.282
    # data.arm_position_z = msg.detections[0].pose.pose.pose.position.z - 0.0763
    # data.arm_orientation_x = msg.detections[0].pose.pose.pose.orientation.x   
    # data.arm_orientation_y = msg.detections[0].pose.pose.pose.orientation.y   
    # data.arm_orientation_z = msg.detections[0].pose.pose.pose.orientation.z   
    # data.arm_orientation_w = msg.detections[0].pose.pose.pose.orientation.w   
    data.arm_orientation_x = -0.5
    data.arm_orientation_y = 0.5
    data.arm_orientation_z = 0.5
    data.arm_orientation_w = 0.5
    print(data.arm_position_x,data.arm_position_x)
    if nt % 5 == 0:
        pub.publish(data)
    nt += 1
    # rospy.loginfo("发布位姿:%s", data)
    # rospy.sleep(1)
    

if __name__ == "__main__":

    rospy.init_node("apriltag_detector_subscriber")
    localizer = Localizer_init()
    rospy.spin()


#摄像头坐标[0.08, 0.26]