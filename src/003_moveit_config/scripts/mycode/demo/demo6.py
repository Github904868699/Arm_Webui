# -*- coding: utf-8 -*-
 
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

usb8_on = 'A0 08 01 A9'
usb8_off = 'A0 08 00 A8'
# shape = ''
cap = cv.VideoCapture(2)
#0.01->8~10mm

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
     
        # def analysis(frame):

        #     h, w, ch = frame.shape
        #     result = np.zeros((h, w, ch), dtype=np.uint8)

        #     # 二值化图像
        #     print("start to detect lines...\n")

        #     gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        #     ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
        #     # cv.imshow("input image", frame)

        #     contours, hierarchy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

        #     for cnt in range(len(contours)):

        #         # 轮廓逼近
        #         epsilon = 0.01 * cv.arcLength(contours[cnt], True)
        #         approx = cv.approxPolyDP(contours[cnt], epsilon, True)

        #         # 分析几何形状
        #         corners = len(approx)
        #         shape_type = ""


        #         if corners == 4:
        #             shape_type = "矩形"

        #         elif corners >= 10:
        #             shape_type = "圆形"

        #         elif 4 < corners < 10:
        #             shape_type = "多边形"

        #         else :
        #             shape_type = "三角形"

        #         # shape_type = "圆形"
        #         # 求解中心位置
        #         # mm = cv.moments(contours[cnt])
        #         # cx = int(mm['m10'] / mm['m00'])
        #         # cy = int(mm['m01'] / mm['m00'])
        #         # cv.circle(result, (cx, cy), 3, (0, 0, 255), -1)

        #         # # 颜色分析
        #         # color = frame[cy][cx]
        #         # color_str = "(" + str(color[0]) + ", " + str(color[1]) + ", " + str(color[2]) + ")"

        #         # # 计算面积与周长
        #         # p = cv.arcLength(contours[cnt], True)
        #         # area = cv.contourArea(contours[cnt])

        #     print("识别到物体形状为", shape_type)

        #     return shape_type   
     
        #形状识别
        def demo6(arm) :

            # for i in range(4) :
            while (1):

                joint_positions = [0.0, -0.52, 1.57, 0.0, 0.0, 0.0]
                arm.set_joint_value_target(joint_positions)
                arm.set_start_state_to_current_state()
                arm.go()

                for j in range(6) :
                # while (1) :


                    lst = [0, 0, 0, 0]
                    ret, frame = cap.read()
                    man = frame[400:800,600:1000]
                    shape = RobotCase.analysis(man)
                    # src = cv.imread("img/1.jpg")
                    # shape = RobotCase.analysis(src)


                    if shape == "三角形" :

                        lst[0] += 1

                    elif shape == "圆形" :
                        
                        lst[1] += 1

                    elif shape == "多边形" :
                        
                        lst[2] += 1

                    elif shape == "矩形" :
                        
                        lst[3] += 1

                tt = lst.index(max(lst))
                dx = 0
                dy = 0

                if tt == 0 :
                    
                    dx = 0.02
                    dy = -0.02

                elif tt == 1 :
                    
                    dx = 0.02
                    dy = 0.02

                elif tt == 2 :
                    
                    dx = -0.02
                    dy = -0.02

                elif tt == 3 :
                    
                    dx = -0.02
                    dy = 0.02
                    

                joint_positions = [0.0, 0.0, 1.57, 0.0, 1.57, 0.0]
                arm.set_joint_value_target(joint_positions)
                arm.set_start_state_to_current_state()
                arm.go()

                nt = 100

                # 获取当前位姿数据最为机械臂运动的起始位姿
                start_pose = arm.get_current_pose(arm.get_end_effector_link()).pose
                # 设置路点数据，并加入路点列表
                wpose = copy.deepcopy(start_pose)
                #计算机械臂运动的动作组
                waypoints = []

                for i in range(nt):
                    wpose.position.z -= 0.020/nt
                    waypoints.append(copy.deepcopy(wpose))

                for i in range(nt):
                    wpose.position.x += 0.097/nt
                    waypoints.append(copy.deepcopy(wpose))
                for i in range(nt):
                    wpose.position.y -= 0.005/nt
                    waypoints.append(copy.deepcopy(wpose))
                for i in range(nt):
                    wpose.position.z -= 0.024/nt
                    waypoints.append(copy.deepcopy(wpose))


                jump_threshold = 0.0
                eef_step = 0.01
                fraction = 0.0
                maxtries = 100
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
                    RobotCase.pub_state(usb8_on)
                    rospy.sleep(0.1)
                else :
                    rospy.INFO("Path planning failed with only %0.6f success after %d attempts.", fraction, maxtries)



                # 获取当前位姿数据最为机械臂运动的起始位姿
                start_pose = arm.get_current_pose(arm.get_end_effector_link()).pose
                # 设置路点数据，并加入路点列表
                wpose = copy.deepcopy(start_pose)
                # 计算机械臂运动的动作组
                waypoints = []

                
                nt = 100
                for i in range(nt):
                    wpose.position.z += 0.033/nt
                    waypoints.append(copy.deepcopy(wpose))

                for i in range(nt):
                    wpose.position.x -= (0.095-dx)/nt
                    waypoints.append(copy.deepcopy(wpose))

                for i in range(nt):
                    wpose.position.y += dy/nt
                    waypoints.append(copy.deepcopy(wpose))

                for i in range(nt):
                    wpose.position.z -= 0.02/nt
                    waypoints.append(copy.deepcopy(wpose))

                jump_threshold = 0.0
                eef_step = 0.01
                fraction = 0.0
                maxtries = 100
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
                    RobotCase.pub_state(usb8_off)
                    print(shape)
                    rospy.sleep(0.1)
                else :
                    rospy.INFO("Path planning failed with only %0.6f success after %d attempts.", fraction, maxtries)



                # # 获取当前位姿数据最为机械臂运动的起始位姿
                # start_pose = arm.get_current_pose(arm.get_end_effector_link()).pose
                # # 设置路点数据，并加入路点列表
                # wpose = copy.deepcopy(start_pose)
                # # 计算机械臂运动的动作组
                # waypoints = []

                

                # 控制机械臂先回到初始化位置
                # arm.set_named_target('stand')
                # arm.go()

        # 控制机械臂先回到初始化位置
        arm.set_named_target('stand')
        arm.go()

        # 关闭并退出moveit
        moveit_commander.roscpp_shutdown()
        moveit_commander.os._exit(0)

    except rospy.ROSInterruptException:
        pass

