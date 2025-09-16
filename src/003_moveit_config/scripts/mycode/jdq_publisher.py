import rospy, sys
from std_msgs.msg import String

if __name__ == "__main__":
    
    rospy.init_node("jdq_publisher")

    pub = rospy.Publisher("jdq_state", String, queue_size=10)
    
    msg = String()

    # str = 'A0 01 01 A2'
    # str = 'A0 08 01 A9'
    str = 'A0 08 00 A8'

    rate = rospy.Rate(1)
    nt = 0

    while not rospy.is_shutdown():

        msg.data = str

        pub.publish(msg.data)

        rate.sleep()

        rospy.loginfo("发布指令:%s", msg.data)

        nt += 1
        if nt >= 2:
            break


