#!/usr/bin/env python
# -*- coding: utf-8 -*-

#用于展示视觉追踪功能的的运动学逆解demo
#此demo是基于moveit ik解算、apriltag识别、hdrarm_msg状态控制的联合测试
#运行效果是，机械臂首先运行到 x0,2 y0.2 z0.2 yaw0 pitch1.57 roll0 的状态
#随后识别放在桌面上的apriltag，调节x和y运动，实现机械臂末端坐标系跟随apriltag码
#注意：本文选用的是apriltag_36h11 id=30
#x和y的调节范围都是正负0.1m

import rospy, sys
import moveit_commander
from moveit_msgs.msg import RobotTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint

from geometry_msgs.msg import PoseStamped, Pose
from tf.transformations import euler_from_quaternion, quaternion_from_euler

import threading
import time

# 引入机械臂控制的自定义消息
from armcontrol_demo_pkg.msg import hdrarm_msg

# 引入apriltag识别消息
from apriltag_ros.msg import AprilTagDetectionArray

# 运动学ik解算所需数据
arm_mode = "arm_sleep"
arm_mode_last = "arm_sleep"
arm_position_x = 0.2
arm_position_y = 0.2
arm_position_z = 0.3
arm_orientation_x = 0.0
arm_orientation_y = 0.707
arm_orientation_z = 0.0
arm_orientation_w = 0.707


def MoveItIkDemo():
    # 同步全局变量
    global arm_mode
    global arm_mode_last
    global arm_position_x
    global arm_position_y
    global arm_position_z
    global arm_orientation_x
    global arm_orientation_y
    global arm_orientation_z
    global arm_orientation_w

    # 初始化move_group的API
    moveit_commander.roscpp_initialize(sys.argv)

    # 初始化需要使用move group控制的机械臂中的arm group
    arm = moveit_commander.MoveGroupCommander('arm')

    # 获取终端link的名称
    #end_effector_link = arm.get_end_effector_link()
    end_effector_link = 'Link_6'

    # 设置目标位置所使用的参考坐标系s
    reference_frame = 'base_link'
    arm.set_pose_reference_frame(reference_frame)

    # 当运动规划失败后，允许重新规划
    arm.allow_replanning(True)

    # 设置位置(单位：米)和姿态（单位：弧度）的允许误差
    arm.set_goal_position_tolerance(0.01)
    arm.set_goal_orientation_tolerance(0.05)

    # 控制机械臂先回到初始化位置
    arm.set_named_target('stand')
    arm.go()
    rospy.sleep(1)

    #记录上一次发送的位姿
    target_p_x = 0.0
    target_p_y = 0.0
    target_p_z = 0.0
    target_o_x = 0.0
    target_o_y = 0.0
    target_o_z = 0.0
    target_o_w = 0.0

    while not rospy.is_shutdown():
        #rospy.loginfo("hello")
        #如果是回到休眠模式，那规划到休眠姿态
        if arm_mode=='arm_sleep':
            rospy.loginfo("arm_sleep")
            arm_mode_last = arm_mode
            arm.set_named_target('stand')
            arm.go()
            rospy.sleep(0.2)
        #如果是在运动模式调整，那么继续
        elif arm_mode=='arm_control_moveit_ik':
            # rospy.loginfo("arm_control_moveit_ik")
            #如果本次与上次的期望位姿一致，那就不用运动(xy容忍一定的误差)
            if (abs(target_p_x-arm_position_x)<0.005)and(abs(target_p_y-arm_position_y)<0.005)and(target_p_z==arm_position_z)and(target_o_x==arm_orientation_x)and(target_o_y==arm_orientation_y)and(target_o_z==arm_orientation_z)and(target_o_w==arm_orientation_w):
                arm_mode_last = arm_mode
            #如果期望位姿发生变化，那就要重新规划并运动
            else:
                arm_mode_last = arm_mode
                # 设置机械臂工作空间中的目标位姿，位置使用x、y、z坐标描述，
                # 姿态使用四元数描述，基于base_link坐标系
                target_pose = PoseStamped()
                target_pose.header.frame_id = reference_frame
                target_pose.header.stamp = rospy.Time.now()     
                target_pose.pose.position.x = arm_position_x
                target_pose.pose.position.y = arm_position_y
                target_pose.pose.position.z = arm_position_z
                target_pose.pose.orientation.x = arm_orientation_x
                target_pose.pose.orientation.y = arm_orientation_y
                target_pose.pose.orientation.z = arm_orientation_z
                target_pose.pose.orientation.w = arm_orientation_w

                print("px:{} py:{} pz:{}".format(target_pose.pose.position.x,target_pose.pose.position.y,target_pose.pose.position.z))
                #记录上一次发送的位姿
                target_p_x = target_pose.pose.position.x
                target_p_y = target_pose.pose.position.y
                target_p_z = target_pose.pose.position.z
                target_o_x = target_pose.pose.orientation.x
                target_o_y = target_pose.pose.orientation.y
                target_o_z = target_pose.pose.orientation.z
                target_o_w = target_pose.pose.orientation.w
                # 设置机器臂当前的状态作为运动初始状态
                arm.set_start_state_to_current_state()
                # 设置机械臂终端运动的目标位姿
                arm.set_pose_target(target_pose, end_effector_link)
                arm.go()
                rospy.sleep(0.2)

    # 关闭并退出moveit
    moveit_commander.roscpp_shutdown()
    moveit_commander.os._exit(0)

# 从/tag_detections刷新xy数据
#arm_position_x = 0.2 + camera.x
#arm_position_y = 0.2 + camera.x
def tag_callback(data):
    #同步全局变量
    global arm_position_x
    global arm_position_y
    
    #rospy.loginfo("resource tag data")

    if data.detections:
        # #刷新数据
        arm_position_x = -(data.detections[0].pose.pose.pose.position.x + 0.075)*0.2 + 0.20
        arm_position_y = (data.detections[0].pose.pose.pose.position.y - 0.12)*0.2 + 0.20
        # arm_position_x = data.detections[0].pose.pose.pose.position.x + 0.20
        # arm_position_y = data.detections[0].pose.pose.pose.position.y + 0.20

        if arm_position_x<0.1:
            arm_position_x=0.1
        elif arm_position_x>0.3:
            arm_position_x=0.3

        if arm_position_y<0.1:
            arm_position_y=0.1
        elif arm_position_y>0.3:
            arm_position_y=0.3
        
        rospy.loginfo("x=%.2f   y=%.2f",arm_position_x,arm_position_y)

    


# 从/armcontrol_Info刷新arm_mode
def armcontrol_callback(data):
    #同步全局变量
    global arm_mode
    global arm_mode_last
    global arm_orientation_x
    global arm_orientation_y
    global arm_orientation_z
    global arm_orientation_w

    #刷新数据
    arm_mode = data.arm_mode
    arm_orientation_x = data.arm_orientation_x
    arm_orientation_y = data.arm_orientation_y
    arm_orientation_z = data.arm_orientation_z
    arm_orientation_w = data.arm_orientation_w

    #rospy.loginfo("resource armcontrol data")

# 运行Subscriber的线程
def hdr_msg():
    rospy.Subscriber("/armcontrol_Info", hdrarm_msg, armcontrol_callback)

    rospy.Subscriber("/tag_detections", AprilTagDetectionArray, tag_callback)
    rospy.spin()

if __name__ == "__main__":
    # 初始化ROS节点
    rospy.init_node('moveit_ik_demo')
    # 开辟一个线程用来运行Subscriber
    t1 = threading.Thread(target=hdr_msg)
    t1.start()
    # 这个只能在主线程里运行
    MoveItIkDemo()

