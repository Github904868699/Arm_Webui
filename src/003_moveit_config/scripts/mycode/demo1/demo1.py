# -*- coding: utf-8 -*-
#流水线搬运编码模块 

import rospy, sys
import copy
import moveit_commander
from moveit_commander import MoveGroupCommander
from copy import deepcopy
import geometry_msgs.msg
from std_msgs.msg import String
import cv2 as cv
import math
from geometry_msgs.msg import PoseStamped, Pose
import numpy as np
import threading
from RobotCase import RobotCase

if __name__ == "__main__":
    try:

        moveit_commander.roscpp_initialize(sys.argv)
        rospy.init_node('case', anonymous=True)

        # 初始化需要使用move group控制的机械臂中的arm group
        arm = MoveGroupCommander('arm')
        
        # 当运动规划失败后，允许重新规划
        arm.allow_replanning(True)
        
        # 设置目标位置所使用的参考坐标系
        arm.set_pose_reference_frame('base_link')
                
        # 设置允许的最大速度和加速度
        arm.set_max_velocity_scaling_factor(0.01)
        arm.set_max_acceleration_scaling_factor(0.01)

        # 设置位置(单位：米)和姿态（单位：弧度）的允许误差
        arm.set_goal_position_tolerance(0.001)
        arm.set_goal_orientation_tolerance(0.005)
        
        # # 获取终端link的名称
        end_effector_link = arm.get_end_effector_link()

        # 控制机械臂先回到初始化位置
        arm.set_named_target('stand')
        RobotCase.demo1(arm)


        # 控制机械臂先回到初始化位置
        arm.set_named_target('stand')
        arm.go()

        # 关闭并退出moveit
        moveit_commander.roscpp_shutdown()
        moveit_commander.os._exit(0)

    except rospy.ROSInterruptException:
        pass

