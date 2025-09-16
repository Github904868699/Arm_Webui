#!/usr/bin/env python
# -*- coding: utf-8 -*-

#用于与ui界面联动的运动学逆解demo

import rospy, sys
import copy
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
global arm_mode
global arm_mode_last
global arm_position_x
global arm_position_y 
global arm_position_z 
global arm_orientation_x 
global arm_orientation_y 
global arm_orientation_z 
global arm_orientation_w 

#记录上一次发送的位姿
global target_p_x 
global target_p_y
global target_p_z 
global target_o_x 
global target_o_y 
global target_o_z 
global target_o_w 


# 初始化ROS节点
rospy.init_node('moveit_ik_demo')
# 初始化move_group的API
moveit_commander.roscpp_initialize(sys.argv)

# 初始化需要使用move group控制的机械臂中的arm group
arm = moveit_commander.MoveGroupCommander('arm')

# 获取终端link的名称
end_effector_link = arm.get_end_effector_link()
# end_effector_link = 'Link_6'

# 设置目标位置所使用的参考坐标系s
reference_frame = 'base_link'
arm.set_pose_reference_frame(reference_frame)

# 当运动规划失败后，允许重新规划
arm.allow_replanning(True)

# 设置允许的最大速度和加速度
arm.set_max_velocity_scaling_factor(0.05)
arm.set_max_acceleration_scaling_factor(0.05)
# 设置位置(单位：米)和姿态（单位：弧度）的允许误差
arm.set_goal_position_tolerance(0.01)
arm.set_goal_orientation_tolerance(0.05)


# 根据接收到的armcontrol_Info更新期望数据
def armcontrol_callback(data):

    #刷新数据
    arm_mode = data.arm_mode
    arm_position_x = data.arm_position_x
    arm_position_y = data.arm_position_y
    arm_position_z = data.arm_position_z
    arm_orientation_x = data.arm_orientation_x
    arm_orientation_y = data.arm_orientation_y
    arm_orientation_z = data.arm_orientation_z
    arm_orientation_w = data.arm_orientation_w


    #如果是回到休眠模式，那规划到休眠姿态
    if arm_mode=='arm_sleep':
        rospy.loginfo("arm_sleep")
        arm_mode_last = arm_mode
        # arm.set_named_target('stand')
        # arm.go()
        # rospy.sleep(0.2)

        joint_positions = [0.0, 0.0, 0.0, 0.0, 1.57, 0.0]
        arm.set_joint_value_target(joint_positions)
        arm.set_start_state_to_current_state()
        arm.go()
        # rospy.sleep(0.2)
    #如果是在运动模式调整，那么继续
    elif arm_mode=='arm_control_moveit_ik':
        # rospy.loginfo("arm_control_moveit_ik")
        #如果本次与上次的期望位姿一致，那就不用运动
        # if (target_p_x==arm_position_x)and(target_p_y==arm_position_y)and(target_p_z==arm_position_z)and(target_o_x==arm_orientation_x)and(target_o_y==arm_orientation_y)and(target_o_z==arm_orientation_z)and(target_o_w==arm_orientation_w):
        #     arm_mode_last = arm_mode
        #如果期望位姿发生变化，那就要重新规划并运动
        # else:
            print("2222222222222")
            # arm_mode_last = arm_mode
            # 设置机械臂工作空间中的目标位姿，位置使用x、y、z坐标描述，
            # 姿态使用四元数描述，基于base_link坐标系
            # target_pose = PoseStamped()
            # target_pose = arm.get_current_pose(arm.get_end_effector_link())
            # target_pose.header.frame_id = reference_frame
            # target_pose.header.stamp = rospy.Time.now()     
            # target_pose.pose.position.x = arm_position_x
            # target_pose.pose.position.y = arm_position_y
            # target_pose.pose.position.z = arm_position_z
            # target_pose.pose.orientation.x = arm_orientation_x
            # target_pose.pose.orientation.y = arm_orientation_y
            # target_pose.pose.orientation.z = arm_orientation_z
            # target_pose.pose.orientation.w = arm_orientation_w
            # #记录上一次发送的位姿
            # target_p_x = target_pose.pose.position.x
            # target_p_y = target_pose.pose.position.y
            # target_p_z = target_pose.pose.position.z
            # target_o_x = target_pose.pose.orientation.x
            # target_o_y = target_pose.pose.orientation.y
            # target_o_z = target_pose.pose.orientation.z
            # target_o_w = target_pose.pose.orientation.w
            # print(123)
            # # 设置机器臂当前的状态作为运动初始状态
            # arm.set_start_state_to_current_state()
            # # 设置机械臂终端运动的目标位姿
            # arm.set_pose_target(target_pose, end_effector_link)
            # arm.go()


            # 获取当前位姿数据最为机械臂运动的起始位姿
            start_pose = arm.get_current_pose(arm.get_end_effector_link()).pose
            # 设置路点数据，并加入路点列表
            wpose = copy.deepcopy(start_pose)
            x = (arm_position_x - start_pose.position.x)
            y = (arm_position_y - start_pose.position.y)
            wpose.position.z = 0.282
            wpose.orientation.x = -0.5
            wpose.orientation.y = 0.5
            wpose.orientation.z = 0.5
            wpose.orientation.w = 0.5
            # 设置机器臂当前的状态作为运动初始状态
            # arm.set_start_state_to_current_state()
            # 设置机械臂终端运动的目标位姿
            # arm.set_pose_target(wpose, end_effector_link)
            # arm.go()

            #记录上一次发送的位姿
            # target_p_x = arm_position_x
            # target_p_y = arm_position_y
            # target_p_z = arm_position_z
            # target_o_x = arm_orientation_x
            # target_o_y = arm_orientation_y
            # target_o_z = arm_orientation_z
            # target_o_w = arm_orientation_w

            # 设置路点数据，并加入路点列表
            waypoints = []

            # wpose.position.x += arm_position_x
            # waypoints.append(copy.deepcopy(wpose))
            # wpose.position.y += arm_position_y
            # waypoints.append(copy.deepcopy(wpose))
            # wpose.position.z += arm_position_z
            # waypoints.append(copy.deepcopy(wpose))
            nt = 10
            for i in range(nt):
                wpose.position.x += x/nt
                waypoints.append(copy.deepcopy(wpose))
            for i in range(nt):
                wpose.position.y += y/nt
                waypoints.append(copy.deepcopy(wpose))
            # for i in range(nt):
            #     wpose.position.z -= z/nt
            #     waypoints.append(copy.deepcopy(wpose))
                
            jump_threshold = 0.0
            eef_step = 0.01
            maxtries = 100
            fraction = 0.0
            attempts = 0
            plan = None

            #进行笛卡尔坐标系下运动规划
            while fraction < 1.0 and attempts < maxtries :
                (plan, fraction) = arm.compute_cartesian_path(waypoints, eef_step, jump_threshold)
                attempts += 1
                if attempts % 10 == 0 :
                    rospy.loginfo("Still trying after %d attempts...", attempts)
            
            if fraction == 1:
                rospy.loginfo("Path computed successfully. Moving the arm.")
                arm.execute(plan)
                rospy.sleep(0.1)
            # else :
            #     rospy.INFO("Path planning failed with only %0.6f success after %d attempts.", fraction, maxtries)


            print("target_pose:")
            print(wpose)
            print("current_pose:")
            print(arm.get_current_pose())
            # rospy.sleep(1)
    
    print("get get get get get ")
    print(data)


# 运行Subscriber的线程
def hdr_msg():
    rospy.Subscriber("target_position", hdrarm_msg, armcontrol_callback)
    rospy.spin()


if __name__ == "__main__":
    
    #/armcontrol_Info的实时数据
    arm_mode = "arm_sleep"
    arm_mode_last = "arm_sleep"
    arm_position_x = 0.0
    arm_position_y = 0.0
    arm_position_z = 0.0
    arm_orientation_x = 0.0
    arm_orientation_y = 0.0
    arm_orientation_z = 0.0
    arm_orientation_w = 0.0

    #记录上一次发送的位姿
    target_p_x = 0.0
    target_p_y = 0.0
    target_p_z = 0.0
    target_o_x = 0.0
    target_o_y = 0.0
    target_o_z = 0.0
    target_o_w = 0.0


    # 控制机械臂先回到初始化位置
    arm.set_named_target('stand')
    arm.go()
    rospy.sleep(0.2)
    
    joint_positions = [0.0, 0.0, 1.57, 0.0, 1.57, 0.0]
    arm.set_joint_value_target(joint_positions)
    arm.set_start_state_to_current_state()
    arm.go()
    rospy.sleep(0.2)

    hdr_msg()

    # 关闭并退出moveit
    moveit_commander.roscpp_shutdown()
    moveit_commander.os._exit(0)
