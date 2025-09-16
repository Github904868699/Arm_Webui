#!/usr/bin/env python
# -*- coding: utf-8 -*-

#用于与ui界面联动的运动学正解demo

import rospy, sys
import moveit_commander
from moveit_msgs.msg import RobotTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint

from geometry_msgs.msg import PoseStamped, Pose
from tf.transformations import euler_from_quaternion, quaternion_from_euler

import threading
import time

#引入机械臂控制的自定位消息
from armcontrol_demo_pkg.msg import hdrarm_msg

#/armcontrol_Info的实时数据
arm_mode = "arm_sleep"
arm_mode_last = "arm_sleep"
joint1_angle = 0.0
joint2_angle = 0.0
joint3_angle = 0.0
joint4_angle = 0.0
joint5_angle = 0.0
joint6_angle = 0.0

#定义
#arm = moveit_commander.MoveGroupCommander('arm')
#reference_frame = 'base_link'
#end_effector_link = arm.get_end_effector_link()

def MoveItFkDemo():
    #同步全局变量
    global arm_mode
    global arm_mode_last
    global joint1_angle
    global joint2_angle
    global joint3_angle
    global joint4_angle
    global joint5_angle
    global joint6_angle

    # 初始化move_group的API
    moveit_commander.roscpp_initialize(sys.argv)

    # 初始化需要使用move group控制的机械臂中的arm group
    arm = moveit_commander.MoveGroupCommander('arm')

    # 设置机械臂和夹爪的允许误差值
    arm.set_goal_joint_tolerance(0.001)
    #gripper.set_goal_joint_tolerance(0.001)

    #记录上一次发送的位姿
    j1 = 0.0
    j2 = 0.0
    j3 = 0.0
    j4 = 0.0
    j5 = 0.0
    j6 = 0.0

    while not rospy.is_shutdown():
        #如果是回到休眠模式，那规划到休眠姿态
        if arm_mode=='arm_sleep':
            rospy.loginfo("arm_sleep")
            arm_mode_last = arm_mode
            arm.set_named_target('stand')
            arm.go()
            rospy.sleep(0.2)
        #如果是在运动模式调整，那么继续
        elif arm_mode=='arm_control_moveit_fk':
            rospy.loginfo("arm_control_moveit_fk")
            #如果本次与上次的期望位姿一致，那就不用运动
            if (j1==joint1_angle)and(j2==joint2_angle)and(j3==joint3_angle)and(j4==joint4_angle)and(j5==joint5_angle)and(j6==joint6_angle):
                arm_mode_last = arm_mode
            #如果期望位姿发生变化，那就要重新规划并运动
            else:
                arm_mode_last = arm_mode
                # 设置机械臂的目标位置，使用六轴的位置数据进行描述（单位：弧度）
                joint_positions = [joint1_angle, joint2_angle, joint3_angle, joint4_angle, joint5_angle, joint6_angle]
                arm.set_joint_value_target(joint_positions)
                arm.set_start_state_to_current_state()
                # 控制机械臂完成运动
                arm.go()
                rospy.sleep(0.1)
                #记录上一次发送的位姿
                j1 = joint1_angle
                j2 = joint2_angle
                j3 = joint3_angle
                j4 = joint4_angle
                j5 = joint5_angle
                j6 = joint6_angle

    # 关闭并退出moveit
    moveit_commander.roscpp_shutdown()
    moveit_commander.os._exit(0)


# 根据接收到的armcontrol_Info更新期望数据
def armcontrol_callback(data):
    #同步全局变量
    global arm_mode
    global joint1_angle
    global joint2_angle
    global joint3_angle
    global joint4_angle
    global joint5_angle
    global joint6_angle

    #刷新数据
    arm_mode = data.arm_mode
    joint1_angle = data.joint1_angle
    joint2_angle = data.joint2_angle
    joint3_angle = data.joint3_angle
    joint4_angle = data.joint4_angle
    joint5_angle = data.joint5_angle
    joint6_angle = data.joint6_angle

    rospy.loginfo("resource data")

# 运行Subscriber的线程
def hdr_msg():
    rospy.Subscriber("/armcontrol_Info", hdrarm_msg, armcontrol_callback)
    rospy.spin()

if __name__ == "__main__":
    # 初始化ROS节点
    rospy.init_node('moveit_fk_demo')
    # 开辟一个线程用来运行Subscriber
    t1 = threading.Thread(target=hdr_msg)
    t1.start()
    # 这个只能在主线程里运行
    MoveItFkDemo()

