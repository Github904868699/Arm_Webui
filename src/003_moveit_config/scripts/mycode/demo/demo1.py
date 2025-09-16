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
import RobotCase

usb5_on = 'A0 05 01 A6'
usb6_on = 'A0 06 01 A7'
usb7_on = 'A0 07 01 A8'
usb8_on = 'A0 08 01 A9'
usb5_off = 'A0 05 00 A5'
usb6_off = 'A0 06 00 A6'
usb7_off = 'A0 07 00 A7'
usb8_off = 'A0 08 00 A8'

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
        arm.go()

        # RobotCase.demo1(arm)
        #流水线搬运编码模块，cartesian抓取
        def demo1(arm):
            
            RobotCase.pub_state(usb7_on)
            joint_positions = [0.0, -0.0523, 1.57, 0.0, 1.6223, 0.0]
            arm.set_joint_value_target(joint_positions)
            arm.set_start_state_to_current_state()
            arm.go()


            RobotCase.pub_state(usb6_on)
            rospy.sleep(3)
            RobotCase.pub_state(usb6_off)
            RobotCase.pub_state(usb5_on)
            rospy.sleep(4)
            RobotCase.pub_state(usb5_off)


            jump_threshold = 0.0
            eef_step = 0.01
            maxtries = 100
            fraction = 0.0
            attempts = 0
            plan = None
            
            start_pose = arm.get_current_pose(arm.get_end_effector_link()).pose
            wpose = copy.deepcopy(start_pose)
            waypoints = []

            #设置动作组
            nt = 100


            for i in range(nt):    
                
                wpose.position.x += 0.115/nt
                waypoints.append(copy.deepcopy(wpose))
            for i in range(nt):    
                
                wpose.position.y += 0.02/nt
                waypoints.append(copy.deepcopy(wpose))
            for i in range(nt):    
                
                wpose.position.z -= 0.048/nt
                waypoints.append(copy.deepcopy(wpose))


            #在笛卡尔坐标系下规划
            while fraction < 1.0 and attempts < maxtries :
                (plan, fraction) = arm.compute_cartesian_path(waypoints, eef_step, jump_threshold)
                attempts += 1
                if attempts % 10 == 0 :
                    rospy.loginfo("Still trying after %d attempts...", attempts)
            
            if fraction == 1.0:
                rospy.loginfo("Path computed successfully. Moving the arm.")
                arm.execute(plan)
                #发送指令，拿起物体
                RobotCase.pub_state(usb8_on)
                rospy.sleep(3)



            jump_threshold = 0.0
            eef_step = 0.01
            maxtries = 100
            fraction = 0.0
            attempts = 0
            plan = None
            
            start_pose = arm.get_current_pose(arm.get_end_effector_link()).pose
            wpose = copy.deepcopy(start_pose)
            waypoints = []

            #设置动作组
            nt = 100

            for i in range(nt):    
                wpose.position.z += 0.02/nt
                waypoints.append(copy.deepcopy(wpose))

            #在笛卡尔坐标系下规划
            while fraction < 1.0 and attempts < maxtries :
                (plan, fraction) = arm.compute_cartesian_path(waypoints, eef_step, jump_threshold)
                attempts += 1
                if attempts % 10 == 0 :
                    rospy.loginfo("Still trying after %d attempts...", attempts)
            
            if fraction == 1.0:
                rospy.loginfo("Path computed successfully. Moving the arm.")
                arm.execute(plan)

            joint_positions = [0.0, -0.0523, 1.57, 0.0, 1.6223, 0.0]
            arm.set_joint_value_target(joint_positions)
            arm.set_start_state_to_current_state()
            arm.go()


            jump_threshold = 0.0
            eef_step = 0.01
            maxtries = 100
            fraction = 0.0
            attempts = 0
            plan = None
            
            start_pose = arm.get_current_pose(arm.get_end_effector_link()).pose
            wpose = copy.deepcopy(start_pose)
            waypoints = []

            #设置动作组
            nt = 100

            for i in range(nt):    
                wpose.position.x -= 0.028/nt
                waypoints.append(copy.deepcopy(wpose))

            for i in range(10):    
                wpose.position.y -= 0.001/10
                waypoints.append(copy.deepcopy(wpose))

            for i in range(nt):    
                wpose.position.z -= 0.053/nt
                waypoints.append(copy.deepcopy(wpose))

            #在笛卡尔坐标系下规划
            while fraction < 1.0 and attempts < maxtries :
                (plan, fraction) = arm.compute_cartesian_path(waypoints, eef_step, jump_threshold)
                attempts += 1
                if attempts % 10 == 0 :
                    rospy.loginfo("Still trying after %d attempts...", attempts)
            
            if fraction == 1.0:
                rospy.loginfo("Path computed successfully. Moving the arm.")
                arm.execute(plan)
                RobotCase.pub_state(usb8_off)
                rospy.sleep(2)



            jump_threshold = 0.0
            eef_step = 0.01
            maxtries = 100
            fraction = 0.0
            attempts = 0
            plan = None
            
            start_pose = arm.get_current_pose(arm.get_end_effector_link()).pose
            wpose = copy.deepcopy(start_pose)
            waypoints = []

            #设置动作组
            nt = 100

            for i in range(nt):    
                wpose.position.z += 0.02/nt
                waypoints.append(copy.deepcopy(wpose))

            #在笛卡尔坐标系下规划
            while fraction < 1.0 and attempts < maxtries :
                (plan, fraction) = arm.compute_cartesian_path(waypoints, eef_step, jump_threshold)
                attempts += 1
                if attempts % 10 == 0 :
                    rospy.loginfo("Still trying after %d attempts...", attempts)
            
            if fraction == 1.0:
                rospy.loginfo("Path computed successfully. Moving the arm.")
                arm.execute(plan)

    #2
            joint_positions = [0.0, -0.0523, 1.57, 0.0, 1.6223, 0.0]
            arm.set_joint_value_target(joint_positions)
            arm.set_start_state_to_current_state()
            arm.go()


            RobotCase.pub_state(usb6_on)
            rospy.sleep(3)
            RobotCase.pub_state(usb6_off)
            RobotCase.pub_state(usb5_on)
            rospy.sleep(4)
            RobotCase.pub_state(usb5_off)


            jump_threshold = 0.0
            eef_step = 0.01
            maxtries = 100
            fraction = 0.0
            attempts = 0
            plan = None
            
            start_pose = arm.get_current_pose(arm.get_end_effector_link()).pose
            wpose = copy.deepcopy(start_pose)
            waypoints = []

            #设置动作组
            nt = 100


            for i in range(nt):    
                
                wpose.position.x += 0.115/nt
                waypoints.append(copy.deepcopy(wpose))
            for i in range(nt):    
                
                wpose.position.y += 0.02/nt
                waypoints.append(copy.deepcopy(wpose))
            for i in range(nt):    
                
                wpose.position.z -= 0.048/nt
                waypoints.append(copy.deepcopy(wpose))


            #在笛卡尔坐标系下规划
            while fraction < 1.0 and attempts < maxtries :
                (plan, fraction) = arm.compute_cartesian_path(waypoints, eef_step, jump_threshold)
                attempts += 1
                if attempts % 10 == 0 :
                    rospy.loginfo("Still trying after %d attempts...", attempts)
            
            if fraction == 1.0:
                rospy.loginfo("Path computed successfully. Moving the arm.")
                arm.execute(plan)
                #发送指令，拿起物体
                RobotCase.pub_state(usb8_on)
                rospy.sleep(2)




            jump_threshold = 0.0
            eef_step = 0.01
            maxtries = 100
            fraction = 0.0
            attempts = 0
            plan = None
            
            start_pose = arm.get_current_pose(arm.get_end_effector_link()).pose
            wpose = copy.deepcopy(start_pose)
            waypoints = []

            #设置动作组
            nt = 100

            for i in range(nt):    
                wpose.position.z += 0.02/nt
                waypoints.append(copy.deepcopy(wpose))

            #在笛卡尔坐标系下规划
            while fraction < 1.0 and attempts < maxtries :
                (plan, fraction) = arm.compute_cartesian_path(waypoints, eef_step, jump_threshold)
                attempts += 1
                if attempts % 10 == 0 :
                    rospy.loginfo("Still trying after %d attempts...", attempts)
            
            if fraction == 1.0:
                rospy.loginfo("Path computed successfully. Moving the arm.")
                arm.execute(plan)
                

            joint_positions = [0.0, -0.0523, 1.57, 0.0, 1.6223, 0.0]
            arm.set_joint_value_target(joint_positions)
            arm.set_start_state_to_current_state()
            arm.go()

            jump_threshold = 0.0
            eef_step = 0.01
            maxtries = 100
            fraction = 0.0
            attempts = 0
            plan = None
            
            start_pose = arm.get_current_pose(arm.get_end_effector_link()).pose
            wpose = copy.deepcopy(start_pose)
            waypoints = []

            #设置动作组
            nt = 100

            for i in range(nt):    
                wpose.position.x -= 0.027/nt
                waypoints.append(copy.deepcopy(wpose))
                print(wpose.position.z)

            for i in range(nt):    
                wpose.position.y += 0.029/nt
                waypoints.append(copy.deepcopy(wpose))
                print(wpose.position.z)

            for i in range(nt):    
                wpose.position.z -= 0.050/nt
                waypoints.append(copy.deepcopy(wpose))
                print(wpose.position.z)

            #在笛卡尔坐标系下规划
            while fraction < 1.0 and attempts < maxtries :
                (plan, fraction) = arm.compute_cartesian_path(waypoints, eef_step, jump_threshold)
                attempts += 1
                if attempts % 10 == 0 :
                    rospy.loginfo("Still trying after %d attempts...", attempts)
            
            if fraction == 1.0:
                rospy.loginfo("Path computed successfully. Moving the arm.")
                arm.execute(plan)
                #发送指令，拿起物体
                RobotCase.pub_state(usb8_off)
                rospy.sleep(2)




            jump_threshold = 0.0
            eef_step = 0.01
            maxtries = 100
            fraction = 0.0
            attempts = 0
            plan = None
            
            start_pose = arm.get_current_pose(arm.get_end_effector_link()).pose
            wpose = copy.deepcopy(start_pose)
            waypoints = []

            #设置动作组
            nt = 100

            for i in range(nt):    
                wpose.position.z += 0.02/nt
                waypoints.append(copy.deepcopy(wpose))

            #在笛卡尔坐标系下规划
            while fraction < 1.0 and attempts < maxtries :
                (plan, fraction) = arm.compute_cartesian_path(waypoints, eef_step, jump_threshold)
                attempts += 1
                if attempts % 10 == 0 :
                    rospy.loginfo("Still trying after %d attempts...", attempts)
            
            if fraction == 1.0:
                rospy.loginfo("Path computed successfully. Moving the arm.")
                arm.execute(plan)

            RobotCase.pub_state(usb7_off)
            tme = 0

            while tme < 5 :
                
                # tme = 4
                #面向机械臂，左上
                if tme == 0:

                    joint_positions = [0.0, -0.0523, 1.57, 0.0, 1.6223, 0.0]
                    arm.set_joint_value_target(joint_positions)
                    arm.set_start_state_to_current_state()
                    arm.go()

                    jump_threshold = 0.0
                    eef_step = 0.01
                    maxtries = 100
                    fraction = 0.0
                    attempts = 0
                    plan = None
                    
                    start_pose = arm.get_current_pose(arm.get_end_effector_link()).pose
                    wpose = copy.deepcopy(start_pose)
                    waypoints = []

                    #设置动作组
                    nt = 100

                    # for i in range(10):    
                    #     wpose.position.y += 0.001/10
                    #     waypoints.append(copy.deepcopy(wpose))

                    for i in range(nt):    
                        print(123)
                        wpose.position.x += 0.005/nt
                        waypoints.append(copy.deepcopy(wpose))
                    for i in range(nt):    
                        print(123)
                        wpose.position.y -= 0.005/nt
                        waypoints.append(copy.deepcopy(wpose))
                    for i in range(nt):    
                        print(123)
                        wpose.position.z -= 0.050/nt
                        waypoints.append(copy.deepcopy(wpose))


                    #在笛卡尔坐标系下规划
                    while fraction < 1.0 and attempts < maxtries :
                        (plan, fraction) = arm.compute_cartesian_path(waypoints, eef_step, jump_threshold)
                        attempts += 1
                        if attempts % 10 == 0 :
                            rospy.loginfo("Still trying after %d attempts...", attempts)
                    
                    if fraction == 1.0:
                        rospy.loginfo("Path computed successfully. Moving the arm.")
                        arm.execute(plan)
                        #发送指令，拿起物体
                        RobotCase.pub_state(usb8_on)
                        rospy.sleep(2)


                    start_pose = arm.get_current_pose(arm.get_end_effector_link()).pose
                    wpose = copy.deepcopy(start_pose)
                    waypoints = []
                    fraction = 0.0
                    attempts = 0
                    plan = None

                    for i in range(nt):    
                        wpose.position.z += 0.05/nt
                        waypoints.append(copy.deepcopy(wpose))

                    for i in range(nt):    
                        wpose.position.x -= 0.074/nt
                        waypoints.append(copy.deepcopy(wpose))

                    for i in range(nt):    
                        wpose.position.y -= 0.002/nt
                        waypoints.append(copy.deepcopy(wpose))

                    for i in range(nt):    
                        wpose.position.z -= 0.030/nt
                        waypoints.append(copy.deepcopy(wpose))

                    while fraction < 1.0 and attempts < maxtries :
                        (plan, fraction) = arm.compute_cartesian_path(waypoints, eef_step, jump_threshold)
                        attempts += 1
                        if attempts % 10 == 0 :
                            rospy.loginfo("Still trying after %d attempts...", attempts)
                    
                    if fraction == 1.0:
                        rospy.loginfo("Path computed successfully. Moving the arm.")
                        arm.execute(plan)
                        #发送指令，放下物体
                        RobotCase.pub_state(usb8_off)    
                        rospy.sleep(2)


                    start_pose = arm.get_current_pose(arm.get_end_effector_link()).pose
                    wpose = copy.deepcopy(start_pose)
                    waypoints = []
                    fraction = 0.0
                    attempts = 0
                    plan = None

                    for i in range(nt):    
                        wpose.position.z += 0.044/nt
                        waypoints.append(copy.deepcopy(wpose))

                    while fraction < 1.0 and attempts < maxtries :
                        (plan, fraction) = arm.compute_cartesian_path(waypoints, eef_step, jump_threshold)
                        attempts += 1
                        if attempts % 10 == 0 :
                            rospy.loginfo("Still trying after %d attempts...", attempts)
                    
                    if fraction == 1.0:
                        rospy.loginfo("Path computed successfully. Moving the arm.")
                        arm.execute(plan)


                # #左下
                elif tme == 1 :
                
                    joint_positions = [0.0, -0.0523, 1.57, 0.0, 1.6223, 0.0]
                    arm.set_joint_value_target(joint_positions)
                    arm.set_start_state_to_current_state()
                    arm.go()

                    jump_threshold = 0.0
                    eef_step = 0.01
                    maxtries = 100
                    fraction = 0.0
                    attempts = 0
                    plan = None
                    
                    start_pose = arm.get_current_pose(arm.get_end_effector_link()).pose
                    wpose = copy.deepcopy(start_pose)
                    waypoints = []

                    #设置动作组
                    nt = 100

                    for i in range(nt):    
                        wpose.position.x += 0.004/nt
                        waypoints.append(copy.deepcopy(wpose))
                    for i in range(nt):    
                        wpose.position.y += 0.033/nt
                        waypoints.append(copy.deepcopy(wpose))
                    for i in range(nt):    
                        wpose.position.z -= 0.050/nt
                        waypoints.append(copy.deepcopy(wpose))

                    #在笛卡尔坐标系下规划
                    while fraction < 1.0 and attempts < maxtries :
                        (plan, fraction) = arm.compute_cartesian_path(waypoints, eef_step, jump_threshold)
                        attempts += 1
                        if attempts % 10 == 0 :
                            rospy.loginfo("Still trying after %d attempts...", attempts)
                    
                    if fraction == 1.0:
                        rospy.loginfo("Path computed successfully. Moving the arm.")
                        arm.execute(plan)
                        #发送指令，拿起物体
                        RobotCase.pub_state(usb8_on)
                        rospy.sleep(2)


                    start_pose = arm.get_current_pose(arm.get_end_effector_link()).pose
                    wpose = copy.deepcopy(start_pose)
                    waypoints = []
                    fraction = 0.0
                    attempts = 0
                    plan = None

                    for i in range(nt):    
                        wpose.position.z += 0.05/nt
                        waypoints.append(copy.deepcopy(wpose))

                    for i in range(nt):    
                        wpose.position.x -= 0.073/nt
                        waypoints.append(copy.deepcopy(wpose))

                    for i in range(nt):    
                        wpose.position.y -= 0.003/nt
                        waypoints.append(copy.deepcopy(wpose))

                    for i in range(nt):    
                        wpose.position.z -= 0.032/nt
                        waypoints.append(copy.deepcopy(wpose))

                    while fraction < 1.0 and attempts < maxtries :
                        (plan, fraction) = arm.compute_cartesian_path(waypoints, eef_step, jump_threshold)
                        attempts += 1
                        if attempts % 10 == 0 :
                            rospy.loginfo("Still trying after %d attempts...", attempts)
                    
                    if fraction == 1.0:
                        rospy.loginfo("Path computed successfully. Moving the arm.")
                        arm.execute(plan)
                        #发送指令，放下物体
                        RobotCase.pub_state(usb8_off)    
                        rospy.sleep(0.5)


                    start_pose = arm.get_current_pose(arm.get_end_effector_link()).pose
                    wpose = copy.deepcopy(start_pose)
                    waypoints = []
                    fraction = 0.0
                    attempts = 0
                    plan = None

                    for i in range(nt):    
                        wpose.position.z += 0.041/nt
                        waypoints.append(copy.deepcopy(wpose))

                    while fraction < 1.0 and attempts < maxtries :
                        (plan, fraction) = arm.compute_cartesian_path(waypoints, eef_step, jump_threshold)
                        attempts += 1
                        if attempts % 10 == 0 :
                            rospy.loginfo("Still trying after %d attempts...", attempts)
                    
                    if fraction == 1.0:
                        rospy.loginfo("Path computed successfully. Moving the arm.")
                        arm.execute(plan)

                # #右上
                elif tme == 2 :
                    
                    joint_positions = [0.0, -0.0523, 1.57, 0.0, 1.6223, 0.0]
                    arm.set_joint_value_target(joint_positions)
                    arm.set_start_state_to_current_state()
                    arm.go()

                    jump_threshold = 0.0
                    eef_step = 0.01
                    maxtries = 100
                    fraction = 0.0
                    attempts = 0
                    plan = None
                    
                    start_pose = arm.get_current_pose(arm.get_end_effector_link()).pose
                    wpose = copy.deepcopy(start_pose)
                    waypoints = []

                    #设置动作组
                    nt = 100

                    for i in range(nt):    
                        wpose.position.x -= 0.028/nt
                        waypoints.append(copy.deepcopy(wpose))

                    for i in range(10):    
                        wpose.position.y -= 0.001/10
                        waypoints.append(copy.deepcopy(wpose))

                    for i in range(nt):    
                        wpose.position.z -= 0.056/nt
                        waypoints.append(copy.deepcopy(wpose))

                    #在笛卡尔坐标系下规划
                    while fraction < 1.0 and attempts < maxtries :
                        (plan, fraction) = arm.compute_cartesian_path(waypoints, eef_step, jump_threshold)
                        attempts += 1
                        if attempts % 10 == 0 :
                            rospy.loginfo("Still trying after %d attempts...", attempts)
                    
                    if fraction == 1.0:
                        rospy.loginfo("Path computed successfully. Moving the arm.")
                        arm.execute(plan)
                        #发送指令，拿起物体
                        RobotCase.pub_state(usb8_on)
                        rospy.sleep(2)


                    start_pose = arm.get_current_pose(arm.get_end_effector_link()).pose
                    wpose = copy.deepcopy(start_pose)
                    waypoints = []
                    fraction = 0.0
                    attempts = 0
                    plan = None

                    for i in range(nt):    
                        wpose.position.z += 0.05/nt
                        waypoints.append(copy.deepcopy(wpose))

                    for i in range(nt):    
                        wpose.position.x -= 0.071/nt
                        waypoints.append(copy.deepcopy(wpose))

                    for i in range(nt):    
                        wpose.position.y -= 0.004/nt
                        waypoints.append(copy.deepcopy(wpose))

                    for i in range(nt):    
                        wpose.position.z -= 0.028/nt
                        waypoints.append(copy.deepcopy(wpose))

                    while fraction < 1.0 and attempts < maxtries :
                        (plan, fraction) = arm.compute_cartesian_path(waypoints, eef_step, jump_threshold)
                        attempts += 1
                        if attempts % 10 == 0 :
                            rospy.loginfo("Still trying after %d attempts...", attempts)
                    
                    if fraction == 1.0:
                        rospy.loginfo("Path computed successfully. Moving the arm.")
                        arm.execute(plan)
                        #发送指令，放下物体
                        RobotCase.pub_state(usb8_off)    
                        rospy.sleep(0.5)


                    start_pose = arm.get_current_pose(arm.get_end_effector_link()).pose
                    wpose = copy.deepcopy(start_pose)
                    waypoints = []
                    fraction = 0.0
                    attempts = 0
                    plan = None

                    for i in range(100):    
                        wpose.position.z += 0.044/100
                        waypoints.append(copy.deepcopy(wpose))

                    while fraction < 1.0 and attempts < maxtries :
                        (plan, fraction) = arm.compute_cartesian_path(waypoints, eef_step, jump_threshold)
                        attempts += 1
                        if attempts % 10 == 0 :
                            rospy.loginfo("Still trying after %d attempts...", attempts)
                    
                    if fraction == 1.0:
                        rospy.loginfo("Path computed successfully. Moving the arm.")
                        arm.execute(plan)


                # #右下
                elif  tme == 3 :
                
                    joint_positions = [0.0, -0.0523, 1.57, 0.0, 1.6223, 0.0]
                    arm.set_joint_value_target(joint_positions)
                    arm.set_start_state_to_current_state()
                    arm.go()

                    jump_threshold = 0.0
                    eef_step = 0.01
                    maxtries = 100
                    fraction = 0.0
                    attempts = 0
                    plan = None
                    
                    start_pose = arm.get_current_pose(arm.get_end_effector_link()).pose
                    wpose = copy.deepcopy(start_pose)
                    waypoints = []

                    #设置动作组
                    nt = 100

                    for i in range(nt):    
                        wpose.position.x -= 0.027/nt
                        waypoints.append(copy.deepcopy(wpose))
                        print(wpose.position.z)

                    for i in range(nt):    
                        wpose.position.y += 0.027/nt
                        waypoints.append(copy.deepcopy(wpose))
                        print(wpose.position.z)

                    for i in range(nt):    
                        wpose.position.z -= 0.053/nt
                        waypoints.append(copy.deepcopy(wpose))
                        print(wpose.position.z)

                    #在笛卡尔坐标系下规划
                    while fraction < 1.0 and attempts < maxtries :
                        (plan, fraction) = arm.compute_cartesian_path(waypoints, eef_step, jump_threshold)
                        attempts += 1
                        if attempts % 10 == 0 :
                            rospy.loginfo("Still trying after %d attempts...", attempts)
                    
                    if fraction == 1.0:
                        rospy.loginfo("Path computed successfully. Moving the arm.")
                        arm.execute(plan)
                        #发送指令，拿起物体
                        RobotCase.pub_state(usb8_on)
                        rospy.sleep(2)


                    start_pose = arm.get_current_pose(arm.get_end_effector_link()).pose
                    wpose = copy.deepcopy(start_pose)
                    waypoints = []
                    fraction = 0.0
                    attempts = 0
                    plan = None

                    for i in range(nt):    
                        wpose.position.z += 0.05/nt
                        waypoints.append(copy.deepcopy(wpose))

                    for i in range(nt):    
                        wpose.position.x -= 0.071/nt
                        waypoints.append(copy.deepcopy(wpose))

                    for i in range(nt):    
                        wpose.position.y -= 0.004/nt
                        waypoints.append(copy.deepcopy(wpose))

                    for i in range(nt):    
                        wpose.position.z -= 0.032/nt
                        waypoints.append(copy.deepcopy(wpose))

                    while fraction < 1.0 and attempts < maxtries :
                        (plan, fraction) = arm.compute_cartesian_path(waypoints, eef_step, jump_threshold)
                        attempts += 1
                        if attempts % 10 == 0 :
                            rospy.loginfo("Still trying after %d attempts...", attempts)
                    
                    if fraction == 1.0:
                        rospy.loginfo("Path computed successfully. Moving the arm.")
                        arm.execute(plan)
                        #发送指令，放下物体
                        RobotCase.pub_state(usb8_off)    
                        rospy.sleep(0.5)


                    start_pose = arm.get_current_pose(arm.get_end_effector_link()).pose
                    wpose = copy.deepcopy(start_pose)
                    waypoints = []
                    fraction = 0.0
                    attempts = 0
                    plan = None

                    for i in range(nt):    
                        wpose.position.z += 0.044/nt
                        waypoints.append(copy.deepcopy(wpose))

                    while fraction < 1.0 and attempts < maxtries :
                        (plan, fraction) = arm.compute_cartesian_path(waypoints, eef_step, jump_threshold)
                        attempts += 1
                        if attempts % 10 == 0 :
                            rospy.loginfo("Still trying after %d attempts...", attempts)
                    
                    if fraction == 1.0:
                        rospy.loginfo("Path computed successfully. Moving the arm.")
                        arm.execute(plan)

                else :
                    # 6.5,1.5,8.5

                    jump_threshold = 0.0
                    eef_step = 0.01
                    maxtries = 100
                    fraction = 0.0
                    attempts = 0
                    plan = None
                    
                    start_pose = arm.get_current_pose(arm.get_end_effector_link()).pose
                    wpose = copy.deepcopy(start_pose)
                    waypoints = []

                    #设置动作组
                    nt = 100

                    for i in range(nt):    
                        wpose.position.x -= 0.077/nt
                        waypoints.append(copy.deepcopy(wpose))
                        print(wpose.position.z)

                    for i in range(nt):    
                        wpose.position.y -= 0.016/nt
                        waypoints.append(copy.deepcopy(wpose))
                        print(wpose.position.z)

                    for i in range(nt):    
                        wpose.position.z -= 0.066/nt
                        waypoints.append(copy.deepcopy(wpose))
                        print(wpose.position.z)

                    #在笛卡尔坐标系下规划
                    while fraction < 1.0 and attempts < maxtries :
                        (plan, fraction) = arm.compute_cartesian_path(waypoints, eef_step, jump_threshold)
                        attempts += 1
                        if attempts % 10 == 0 :
                            rospy.loginfo("Still trying after %d attempts...", attempts)
                    
                    if fraction == 1.0:
                        rospy.loginfo("Path computed successfully. Moving the arm.")
                        arm.execute(plan)
                        #发送指令，拿起物体
                        RobotCase.pub_state(usb8_on)
                        rospy.sleep(3)


                    start_pose = arm.get_current_pose(arm.get_end_effector_link()).pose
                    wpose = copy.deepcopy(start_pose)
                    waypoints = []
                    fraction = 0.0
                    attempts = 0
                    plan = None

                    for i in range(nt):    
                        wpose.position.z += 0.054/nt
                        waypoints.append(copy.deepcopy(wpose))

                    for i in range(nt):    
                        wpose.position.x += 0.085/nt
                        waypoints.append(copy.deepcopy(wpose))

                    for i in range(nt):    
                        wpose.position.z -= 0.015/nt
                        waypoints.append(copy.deepcopy(wpose))

                    while fraction < 1.0 and attempts < maxtries :
                        (plan, fraction) = arm.compute_cartesian_path(waypoints, eef_step, jump_threshold)
                        attempts += 1
                        if attempts % 10 == 0 :
                            rospy.loginfo("Still trying after %d attempts...", attempts)
                    
                    if fraction == 1.0:
                        rospy.loginfo("Path computed successfully. Moving the arm.")
                        arm.execute(plan)
                        #发送指令，放下物体
                        RobotCase.pub_state(usb8_off)    
                        rospy.sleep(0.5)


                    start_pose = arm.get_current_pose(arm.get_end_effector_link()).pose
                    wpose = copy.deepcopy(start_pose)
                    waypoints = []
                    fraction = 0.0
                    attempts = 0
                    plan = None

                    for i in range(nt):    
                        wpose.position.z += 0.044/nt
                        waypoints.append(copy.deepcopy(wpose))

                    while fraction < 1.0 and attempts < maxtries :
                        (plan, fraction) = arm.compute_cartesian_path(waypoints, eef_step, jump_threshold)
                        attempts += 1
                        if attempts % 10 == 0 :
                            rospy.loginfo("Still trying after %d attempts...", attempts)
                    
                    if fraction == 1.0:
                        rospy.loginfo("Path computed successfully. Moving the arm.")
                        arm.execute(plan)

                tme += 1

        # 控制机械臂先回到初始化位置
        arm.set_named_target('stand')
        arm.go()

        # 关闭并退出moveit
        moveit_commander.roscpp_shutdown()
        moveit_commander.os._exit(0)

    except rospy.ROSInterruptException:
        pass

