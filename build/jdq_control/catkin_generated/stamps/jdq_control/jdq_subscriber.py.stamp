import rospy
from jdq_control.msg import jdq_state
def getMsg(msg):
    rospy.loginfo("获得指令:")
    rospy.loginfo(msg)

if __name__ == "__main__":
    
    rospy.init_node("jdq_subscriber")

    pub = rospy.Subscriber("jdq_state", jdq_state, getMsg, queue_size=10)
    
    rospy.spin()