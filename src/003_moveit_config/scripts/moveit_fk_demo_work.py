#!/usr/bin/env python
# -*- coding: utf-8 -*-

#用于展示搬运的运动学正解demo

import rospy, sys
import moveit_commander
from control_msgs.msg import GripperCommand
import geometry_msgs.msg

class MoveItFkDemo:
    def __init__(self):
        # 初始化move_group的API
        moveit_commander.roscpp_initialize(sys.argv)

        # 初始化ROS节点
        rospy.init_node('moveit_fk_demo', anonymous=True)
 
        # 初始化需要使用move group控制的机械臂中的arm group
        arm = moveit_commander.MoveGroupCommander('arm')
        reference_frame = 'base_link'
        # 初始化需要使用move group控制的机械臂中的gripper group
        #gripper = moveit_commander.MoveGroupCommander('gripper')
        
        # 设置机械臂和夹爪的允许误差值
        arm.set_goal_joint_tolerance(0.001)
        #gripper.set_goal_joint_tolerance(0.001)
        
        while not rospy.is_shutdown():
            
            # 控制机械臂先回到站立位置
          #  arm.set_named_target('stand')
          #  print(arm.get_current_pose())
          #  arm.go()
          #  print("1")
          #  rospy.sleep(0.05)

            # 设置机械臂的目标位置，使用六轴的位置数据进行描述（单位：弧度）
           # joint_positions = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
            #arm.set_joint_value_target(joint_positions)
         #   arm.set_start_state_to_current_state()
            # 控制机械臂完成运动
           # arm.go()
           # rospy.sleep(0.05)

            # 设置机械臂的目标位置，使用六轴的位置数据进行描述（单位：弧度)
          #  joint_positions = [-2.8, -0.8, 2.3, 1.8, 1.6, 3.0]
          #  arm.set_joint_value_target(joint_positions)
          #  arm.set_start_state_to_current_state()
          #  # 控制机械臂完成运动
          #  arm.go()
          #  rospy.sleep(0.05)

           # # 设置机械臂的目标位置，使用六轴的位置数据进行描述（单位：弧度）
           # joint_positions = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
          #  arm.set_joint_value_target(joint_positions)
            #arm.set_start_state_to_current_state()
            # 控制机械臂完成运动
         #   arm.go()
           # rospy.sleep(0.05)

            # 设置机械臂的目标位置，使用六轴的位置数据进行描述（单位：弧度）
          #  joint_positions = [2.8, 0.8, -2.3, -1.8, -1.6, -3.0]
          #  arm.set_joint_value_target(joint_positions)
          #  arm.set_start_state_to_current_state()
          #  # 控制机械臂完成运动
          #  arm.go()
          #  rospy.sleep(0.05)

            # 设置机械臂的目标位置，使用六轴的位置数据进行描述（单位：弧度）
           # joint_positions = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
          #  arm.set_joint_value_target(joint_positions)
           # arm.set_start_state_to_current_state()
            # 控制机械臂完成运动
           # arm.go()
           # rospy.sleep(0.05)

            # 设置机械臂的目标位置，使用六轴的位置数据进行描述（单位：弧度）
          #  joint_positions = [0.0347804, 0.73802410, 0.9704769, 0.10306746, 1.5460993, 1.5747416]
          #  joint_positions = [0.0, 0.0, 1.57, 0.0, 1.57, 0.0]
          #  target_pose = geometry_msgs.msg.Pose()
          #  target_pose.orientation.x = 0.0
          #  target_pose.orientation.y = 0.0
          #  target_pose.orientation.z = 0.0003
          #  target_pose.orientation.w = 0.999

          #  target_pose.position.x = 0.117
          #  target_pose.position.y = 0.0
          #  target_pose.position.z = 0.7


          #  arm.set_joint_value_target(joint_positions)

          #  target_pose = geometry_msgs.msg.Pose()
          #  target_pose.orientation.x = 0.0
          #  target_pose.orientation.y = 0.707
          #  target_pose.orientation.z = 0.0
          #  target_pose.orientation.w = 0.707

          #  target_pose.position.x = 0.2
          #  target_pose.position.y = 0.2
          #  target_pose.position.z = 0.3
    
          #  arm.set_pose_target(target_pose)
          #  arm.go()
          #  arm.set_start_state_to_current_state()
           print("2")
           print(arm.get_current_pose())
           # 控制机械臂完成运动
          #  arm.go()
           rospy.sleep(1)
           break
        
        # 关闭并退出moveit
        moveit_commander.roscpp_shutdown()
        moveit_commander.os._exit(0)

if __name__ == "__main__":
    try:
        MoveItFkDemo()
    except rospy.ROSInterruptException:
        pass

# pose: 
#   position: 
#     x: 0.1173996781232019
#     y: -8.215905928548514e-05
#     z: 0.5924999975786889
#   orientation: 
#     x: 7.380530654527417e-05
#     y: -1.8994561637665727e-07
#     z: 0.00030188254901947263
#     w: 0.9999999517098324