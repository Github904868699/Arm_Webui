import rospy
from jdq_control.msg import jdq_state

if __name__ == "__main__":
    
    rospy.init_node("jdq_publisher")

    pub = rospy.Publisher("jdq_state", jdq_state, queue_size=10)
    
    msg = jdq_state()

    msg.USB1 = 'A00101A2'

    rate = rospy.Rate(1)

    while not rospy.is_shutdown():

        pub.publish(msg)

        rate.sleep()

        rospy.loginfo("发布指令:%s", msg.USB1)

        # break
