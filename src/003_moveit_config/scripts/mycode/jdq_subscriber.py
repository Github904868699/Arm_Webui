import rospy, sys
from std_msgs.msg import String

import serial

ser = serial.Serial("/dev/ttyCH341USB0", baudrate = 9600, bytesize = 8, parity = 'N', stopbits = 1)

def send_hex_data(hex_string):
    byte_array = bytearray.fromhex(hex_string)

    ser.write(byte_array)


def getMsg(msg):

    rospy.loginfo("获得指令：%s", msg.data)

    send_hex_data(msg.data)

    # ser.close()

if __name__ == "__main__":
    
    rospy.init_node("jdq_subscriber")

    sub = rospy.Subscriber("jdq_state", String, getMsg, queue_size=10)
    rospy.spin()

    