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

usb1_on = 'A0 01 01 A2'
usb2_on = 'A0 02 01 A3'
usb3_on = 'A0 03 01 A4'
usb4_on = 'A0 04 01 A5'
usb5_on = 'A0 05 01 A6'
usb6_on = 'A0 06 01 A7'
usb7_on = 'A0 07 01 A8'
usb8_on = 'A0 08 01 A9'
usb1_off = 'A0 01 00 A1'
usb2_off = 'A0 02 00 A2'
usb3_off = 'A0 03 00 A3'
usb4_off = 'A0 04 00 A4'
usb5_off = 'A0 05 00 A5'
usb6_off = 'A0 06 00 A6'
usb7_off = 'A0 07 00 A7'
usb8_off = 'A0 08 00 A8'
# shape = ''
cap = cv.VideoCapture(6)
#0.01->8~10mm

class RobotCase:
    
    def pub_state(state):

        pub = rospy.Publisher("jdq_state", String, queue_size=10)     
        msg = String()
        msg.data = state
        rate = rospy.Rate(1)

        nt = 0
        while not rospy.is_shutdown():
            
            nt += 1
            pub.publish(msg)
            rate.sleep()
            rospy.loginfo("发布指令:%s", msg.data)

            if nt >= 2:
                break


    # def get_s(msg):
    #     shape = msg.data

    # def get_shape():

    #     pub = rospy.Publisher("cap", String, queue_size=1)     
    #     msg = String()
    #     msg.data = 1
    #     rate = rospy.Rate(1)

    #     nt = 0
    #     while not rospy.is_shutdown():
            
    #         nt += 1
    #         pub.publish(msg)
    #         rate.sleep()
    #         rospy.loginfo("发布指令:%s", msg.data)

    #         if nt >= 2:
    #             break
        

    #     sub = rospy.Subscriber("shape", String, RobotCase.get_s, queue_size=1)
    #     rospy.spin()
        

    def analysis(frame):

        h, w, ch = frame.shape
        result = np.zeros((h, w, ch), dtype=np.uint8)

        # 二值化图像
        print("start to detect lines...\n")

        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
        # cv.imshow("input image", frame)

        contours, hierarchy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

        for cnt in range(len(contours)):

            # 轮廓逼近
            epsilon = 0.01 * cv.arcLength(contours[cnt], True)
            approx = cv.approxPolyDP(contours[cnt], epsilon, True)

            # 分析几何形状
            corners = len(approx)
            shape_type = ""


            if corners == 4:
                shape_type = "矩形"

            elif corners >= 10:
                shape_type = "圆形"

            elif 4 < corners < 10:
                shape_type = "多边形"

            else :
                shape_type = "三角形"

            # shape_type = "圆形"
            # 求解中心位置
            # mm = cv.moments(contours[cnt])
            # cx = int(mm['m10'] / mm['m00'])
            # cy = int(mm['m01'] / mm['m00'])
            # cv.circle(result, (cx, cy), 3, (0, 0, 255), -1)

            # # 颜色分析
            # color = frame[cy][cx]
            # color_str = "(" + str(color[0]) + ", " + str(color[1]) + ", " + str(color[2]) + ")"

            # # 计算面积与周长
            # p = cv.arcLength(contours[cnt], True)
            # area = cv.contourArea(contours[cnt])

        print("识别到物体形状为", shape_type)

        return shape_type



    def color_detection(frame):

        lower_red = np.array([0, 43, 46])
        upper_red = np.array([15, 255, 255])

        lower_blue = np.array([100, 43, 46])
        upper_blue = np.array([124, 255, 255])

        lower_yellow = np.array([20, 40, 40])
        upper_yellow = np.array([40, 255, 255])

        lower_black = np.array([0, 0, 0])
        upper_black = np.array([180, 255, 46])

        hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        red_mask = cv.inRange(hsv_frame, lower_red, upper_red)
        blue_mask = cv.inRange(hsv_frame, lower_blue, upper_blue)
        black_mask = cv.inRange(hsv_frame, lower_black, upper_black)
        yellow_mask = cv.inRange(hsv_frame, lower_yellow, upper_yellow)

        kernel = np.ones((5, 5), np.uint8)
        red_mask = cv.morphologyEx(red_mask, cv.MORPH_OPEN, kernel)
        blue_mask = cv.morphologyEx(blue_mask, cv.MORPH_OPEN, kernel)
        black_mask = cv.morphologyEx(black_mask, cv.MORPH_OPEN, kernel)
        yellow_mask = cv.morphologyEx(yellow_mask, cv.MORPH_OPEN, kernel)

        color = ""
        contours, _ = cv.findContours(red_mask + blue_mask + black_mask + yellow_mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            x, y, w, h = cv.boundingRect(contour)
            # if cv2.contourArea(contour) > 500:  
            if np.any(blue_mask[y:y + h, x:x + w]):
                color = "蓝色"
                # cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            elif np.any(yellow_mask[y:y + h, x:x + w]):
                color = "黄色"
                # cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            elif np.any(black_mask[y:y + h, x:x + w]):
                color = "黑色"
                # cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 0), 2)
            else :
                color = "红色"
                    # cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                # cv2.putText(frame, color, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            # print(color)
        if color == "" :
            color = "红色"
        return color



    #无cartesian规划抓取
    def demo0(arm):

        joint_positions = [0.0, 0.0, 1.57, 0.0, 1.57, 0.0]
        arm.set_joint_value_target(joint_positions)
        arm.set_start_state_to_current_state()
        arm.go()
        rospy.sleep(0.5)
        
        # 获取当前位姿数据最为机械臂运动的起始位姿
        start_pose = arm.get_current_pose(arm.get_end_effector_link()).pose

        # 设置路点数据，并加入路点列表
        wpose = copy.deepcopy(start_pose)

        wpose.position.z -= 0.034
        arm.set_pose_target(wpose)
        arm.go()

        #发送指令，拿起物体
        RobotCase.pub_state(usb1_on)
        rospy.sleep(1)
     
        wpose.position.z += 0.044
        arm.set_pose_target(wpose)
        arm.go()
        rospy.sleep(0.5)

        wpose.position.x += 0.069
        arm.set_pose_target(wpose)
        arm.go()
        rospy.sleep(0.5)

        wpose.position.z -= 0.034
        arm.set_pose_target(wpose)
        arm.go()
        
        #发送指令，放下物体
        RobotCase.pub_state(usb1_off)
        rospy.sleep(1)
        
        wpose.position.z += 0.05
        arm.set_pose_target(wpose)
        arm.go()
        rospy.sleep(0.5)




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

    #打磨模块
    def demo2(arm):

        #拿物料

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
            rospy.sleep(1)


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
            wpose.position.x += 0.15/nt
            waypoints.append(copy.deepcopy(wpose))

        for i in range(nt):    
            wpose.position.z -= 0.035/nt
            waypoints.append(copy.deepcopy(wpose))

        while fraction < 1.0 and attempts < maxtries :
            (plan, fraction) = arm.compute_cartesian_path(waypoints, eef_step, jump_threshold)
            attempts += 1
            if attempts % 10 == 0 :
                rospy.loginfo("Still trying after %d attempts...", attempts)
        
        if fraction == 1.0:
            rospy.loginfo("Path computed successfully. Moving the arm.")
            arm.execute(plan)

            #打开打磨机
            RobotCase.pub_state(usb7_on)    
            rospy.sleep(3)
            #关闭打磨机
            RobotCase.pub_state(usb7_off)    
            rospy.sleep(0.5)


        start_pose = arm.get_current_pose(arm.get_end_effector_link()).pose
        wpose = copy.deepcopy(start_pose)
        waypoints = []
        fraction = 0.0
        attempts = 0
        plan = None

        for i in range(nt):     
            wpose.position.z += 0.03/nt
            waypoints.append(copy.deepcopy(wpose))

        for i in range(nt):    
            wpose.position.x -= 0.15/nt
            waypoints.append(copy.deepcopy(wpose))


        for i in range(nt):     
            wpose.position.z -= 0.03/nt
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

    #不断上料搬运
    def demo3(arm):
        #80,x43,y38
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
        nt = 10

        for i in range(nt):    
            wpose.position.x -= 0.03/nt
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
            rospy.sleep(0.2)


        x = 0.076
        y = 0.118
        tme = 0

        while tme < 8:

            RobotCase.pub_state(usb8_on)
            rospy.sleep(0.5)
            
            if tme % 2 == 0 :
                if tme != 0:
                    y += 0.038
                    x -= 0.043
            else :
                y -= 0.038
            print(x)
            print(y)

            jump_threshold = 0.0
            eef_step = 0.01
            maxtries = 100
            fraction = 0.0
            attempts = 0
            plan = None
            
            start_pose = arm.get_current_pose(arm.get_end_effector_link()).pose
            wpose = copy.deepcopy(start_pose)
            waypoints = []


            for i in range(nt):    
                wpose.position.z += 0.050/nt
                waypoints.append(copy.deepcopy(wpose))

            for i in range(nt):    
                wpose.position.y += y/nt
                waypoints.append(copy.deepcopy(wpose))

            for i in range(nt):    
                wpose.position.x += x/nt
                waypoints.append(copy.deepcopy(wpose))

            for i in range(nt):    
                wpose.position.z -= 0.030/nt
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
                #发送指令，放下物体
                RobotCase.pub_state(usb8_off)
                rospy.sleep(0.5)


            jump_threshold = 0.0
            eef_step = 0.01
            maxtries = 100
            fraction = 0.0
            attempts = 0
            plan = None
            
            start_pose = arm.get_current_pose(arm.get_end_effector_link()).pose
            wpose = copy.deepcopy(start_pose)
            waypoints = []


            for i in range(nt):    
                wpose.position.z += 0.030/nt
                waypoints.append(copy.deepcopy(wpose))

            for i in range(nt):    
                wpose.position.y -= y/nt
                waypoints.append(copy.deepcopy(wpose))

            for i in range(nt):    
                wpose.position.x -= x/nt
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
            
            tme += 1


    #打螺丝
    def demo4(arm) :

        joint_positions = [0.0, -0.0523, 1.57, 0.0, 1.6223, 0.0]
        arm.set_joint_value_target(joint_positions)
        arm.set_start_state_to_current_state()
        arm.go()

        # 获取当前位姿数据最为机械臂运动的起始位姿
        start_pose = arm.get_current_pose(arm.get_end_effector_link()).pose

        # 设置路点数据，并加入路点列表
        wpose = copy.deepcopy(start_pose)
        
        waypoints = []

        #计算机械臂运动的动作组
        nt = 100
            
        for i in range(nt):
            wpose.position.z -= 0.086/nt
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
            rospy.sleep(0.5)
        else :
            rospy.INFO("Path planning failed with only %0.6f success after %d attempts.", fraction, maxtries)



        # 获取当前位姿数据最为机械臂运动的起始位姿
        start_pose = arm.get_current_pose(arm.get_end_effector_link()).pose

        # 设置路点数据，并加入路点列表
        wpose = copy.deepcopy(start_pose)
        waypoints = []
            
        for i in range(nt):
            wpose.position.z += 0.05/nt
            waypoints.append(copy.deepcopy(wpose))
        for i in range(nt):
            wpose.position.x += 0.051/nt
            waypoints.append(copy.deepcopy(wpose))
        for i in range(nt):
            wpose.position.y += 0.01/nt
            waypoints.append(copy.deepcopy(wpose))
        for i in range(nt):
            wpose.position.z -= 0.045/nt
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
            rospy.sleep(0.1)
        else :
            rospy.INFO("Path planning failed with only %0.6f success after %d attempts.", fraction, maxtries)


        joint_positions = arm.get_current_joint_values()
        joint_positions[5] = 12.00
        arm.set_joint_value_target(joint_positions)
        arm.set_start_state_to_current_state()
        arm.go()



        rospy.sleep(0.5)

        # 获取当前位姿数据最为机械臂运动的起始位姿
        start_pose = arm.get_current_pose(arm.get_end_effector_link()).pose

        # 设置路点数据，并加入路点列表
        wpose = copy.deepcopy(start_pose)
        waypoints = []

            
        for i in range(nt):
            wpose.position.z += 0.05/nt
            waypoints.append(copy.deepcopy(wpose))
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
            rospy.sleep(0.1)
        else :
            rospy.INFO("Path planning failed with only %0.6f success after %d attempts.", fraction, maxtries)

    #立库
    def demo5(arm) :

        #移动到初始位位姿
        joint_positions = [0.0, 0.0, 1.57, 0.0, 1.57, 0.0]
        arm.set_joint_value_target(joint_positions)
        arm.set_start_state_to_current_state()
        arm.go()

        # 获取当前位姿数据最为机械臂运动的起始位姿
        start_pose = arm.get_current_pose(arm.get_end_effector_link()).pose

        # 设置路点数据，并加入路点列表
        wpose = copy.deepcopy(start_pose)
        
        waypoints = []

        #计算机械臂运动的动作组
        nt = 100
            
        for i in range(nt):
            wpose.position.z += 0.06/nt
            waypoints.append(copy.deepcopy(wpose))

        for i in range(nt):
            wpose.position.x += 0.07/nt
            waypoints.append(copy.deepcopy(wpose))

        for i in range(nt):
            wpose.position.y += 0.012/nt
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
        else :
            rospy.INFO("Path planning failed with only %0.6f success after %d attempts.", fraction, maxtries)

        while True :
            RobotCase.pub_state(usb8_on)
            rospy.sleep(0.2)

            #吸取物体，移动至立库
            # 获取当前位姿数据最为机械臂运动的起始位姿
            start_pose = arm.get_current_pose(arm.get_end_effector_link()).pose

            # 设置路点数据，并加入路点列表
            wpose = copy.deepcopy(start_pose)
            
            waypoints = []

            #计算机械臂运动的动作组
            nt = 100
                
            for i in range(nt):
                wpose.position.z += 0.024/nt
                waypoints.append(copy.deepcopy(wpose))

            for i in range(nt):
                wpose.position.x -= 0.24/nt
                waypoints.append(copy.deepcopy(wpose))
            for i in range(nt):
                wpose.position.y -= 0.006/nt
                waypoints.append(copy.deepcopy(wpose))

            for i in range(nt):
                wpose.position.z -= 0.060/nt
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
                rospy.sleep(0.5)
            else :
                rospy.INFO("Path planning failed with only %0.6f success after %d attempts.", fraction, maxtries)




            #恢复初始姿态
            # 获取当前位姿数据最为机械臂运动的起始位姿
            start_pose = arm.get_current_pose(arm.get_end_effector_link()).pose

            # 设置路点数据，并加入路点列表
            wpose = copy.deepcopy(start_pose)
            
            waypoints = []

            #计算机械臂运动的动作组
            nt = 100
                
            for i in range(nt):
                wpose.position.z += 0.060/nt
                waypoints.append(copy.deepcopy(wpose))

            for i in range(nt):
                wpose.position.x += 0.24/nt
                waypoints.append(copy.deepcopy(wpose))
            for i in range(nt):
                wpose.position.y += 0.006/nt
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
                RobotCase.pub_state(usb8_off)
                rospy.sleep(0.2)
            else :
                rospy.INFO("Path planning failed with only %0.6f success after %d attempts.", fraction, maxtries)


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

        
    # 颜色识别
    def demo7(arm) :


        for i in range(15) :


            joint_positions = [0.0, -0.52, 1.57, 0.0, 0.0, 0.0]
            arm.set_joint_value_target(joint_positions)
            arm.set_start_state_to_current_state()
            arm.go()


            ret, frame = cap.read()

            result = [0, 0, 0,0 ,0 ,0 ,0 ,0 ]

            man1 = frame[330:600, 340:640]
            man2 = frame[330:600, 630:970]
            man3 = frame[330:600, 970:1270]
            man4 = frame[330:600, 1270:1530]
            man5 = frame[600:850, 360:670]
            man6 = frame[600:850, 670:970]
            man7 = frame[600:850, 970:1270]
            man8 = frame[600:850, 1270:1500]

            result[0] = RobotCase.color_detection(man1)
            result[1] = RobotCase.color_detection(man2)
            result[2] = RobotCase.color_detection(man3)
            result[3] = RobotCase.color_detection(man4)
            result[4] = RobotCase.color_detection(man5)
            result[5] = RobotCase.color_detection(man6)
            result[6] = RobotCase.color_detection(man7)
            result[7] = RobotCase.color_detection(man8)

            # print(result)
        
        for i in range(4):
            k = result[i]
            result[i] = result[i + 4]
            result[i + 4] = k
        # print(result)
        for i in range(2):
            k = result[i]
            result[i] = result[3 - i]
            result[3 - i] = k
            k = result[i + 4]
            result[i + 4] = result[7 - i]
            result[7 - i] = k
        print(result)
        # return 
        rospy.sleep(0.2)

        joint_positions = [0.0, 0.0, 1.57, 0.0, 1.57, 0.0]
        arm.set_joint_value_target(joint_positions)
        arm.set_start_state_to_current_state()
        arm.go()

        dx = [0.067, 0.027, -0.021, -0.066]
        dx1 = [0.067, 0.027, -0.021, -0.066]
        dy = 0.04
        # dx = [0.0, 0.0, 0.0, 0.0]

        for i in range(4) :
            for j in range(4, 8) :
                if result[i] == result[j] :
                    dx1[i] = dx[j - 4]
                    # dx1[i] = dx1[i] - dx[i]
                  
        nt = 100

        for i in range(4) :
            
            start_pose = arm.get_current_pose(arm.get_end_effector_link()).pose
            wpose = copy.deepcopy(start_pose)
            waypoints = []
            for j in range(nt):    
                wpose.position.x += dx[i]/nt
                waypoints.append(copy.deepcopy(wpose))
            for j in range(nt):    
                wpose.position.z -= 0.035/nt
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
                rospy.sleep(0.2)
            else :
                rospy.INFO("Path planning failed with only %0.6f success after %d attempts.", fraction, maxtries)



            start_pose = arm.get_current_pose(arm.get_end_effector_link()).pose
            wpose = copy.deepcopy(start_pose)
            waypoints = []
            for j in range(nt):    
                wpose.position.z += 0.035/nt
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
                rospy.sleep(0.2)
            else :
                rospy.INFO("Path planning failed with only %0.6f success after %d attempts.", fraction, maxtries)



            joint_positions = [0.0, 0.0, 1.57, 0.0, 1.57, 0.0]
            arm.set_joint_value_target(joint_positions)
            arm.set_start_state_to_current_state()
            arm.go()


            start_pose = arm.get_current_pose(arm.get_end_effector_link()).pose
            wpose = copy.deepcopy(start_pose)
            waypoints = []
            for j in range(nt):    
                wpose.position.x += dx1[i]/nt
                waypoints.append(copy.deepcopy(wpose))
            for j in range(nt):    
                wpose.position.y += dy/nt
                waypoints.append(copy.deepcopy(wpose))
            for j in range(nt):    
                wpose.position.z -= 0.025/nt
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
                rospy.sleep(0.2)
            else :
                rospy.INFO("Path planning failed with only %0.6f success after %d attempts.", fraction, maxtries)



            start_pose = arm.get_current_pose(arm.get_end_effector_link()).pose
            wpose = copy.deepcopy(start_pose)
            waypoints = []
            for j in range(nt):    
                wpose.position.z += 0.025/nt
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
                rospy.sleep(0.2)
            else :
                rospy.INFO("Path planning failed with only %0.6f success after %d attempts.", fraction, maxtries)




            joint_positions = [0.0, 0.0, 1.57, 0.0, 1.57, 0.0]
            arm.set_joint_value_target(joint_positions)
            arm.set_start_state_to_current_state()
            arm.go()


    def hdr_msg() :
        # while True :
            RobotCase.pub_state(usb5_on)
            rospy.sleep(4)
            RobotCase.pub_state(usb5_off)

    # 流水线
    def demo8(arm) :

        dx = 0
        dy = 0
        dz = 0
        RobotCase.pub_state(usb7_on)
        # t1 = threading.Thread(target=RobotCase.hdr_msg)
        # t1.start()
        # t1 = threading.Thread(target=RobotCase.hdr_msg)
        for i in range(6) :


            joint_positions = [0.0, 0.0, 1.57, 0.0, 1.57, 0.0]
            arm.set_joint_value_target(joint_positions)
            arm.set_start_state_to_current_state()
            arm.go()


            RobotCase.pub_state(usb6_on)
            rospy.sleep(3)
            RobotCase.pub_state(usb6_off)
            RobotCase.pub_state(usb5_on)
            rospy.sleep(4)
            RobotCase.pub_state(usb5_off)
            # t1.start()

            
            # RobotCase.pub_state(usb7_on)
            # # rospy.sleep(0.2)
            # RobotCase.pub_state(usb6_on)
            # rospy.sleep(2.5)
            # RobotCase.pub_state(usb6_off)

            # RobotCase.pub_state(usb5_on)
            # rospy.sleep(3)    

            if i == 0 :
                dz = 0.050
                dx = -0.126
                dy = -0.003
            elif i == 1 :
                dz = 0.000
                dx = -0.166
            elif i == 2 :
                dz = 0.050
                dx = -0.125
                dy = 0.057

            elif i == 3 :
                dz = 0.000
                dx = -0.164
                dy = 0.054

            elif i == 4 :
                dz = 0.050
                dx = -0.124
                dy = -0.062
            elif i == 5 :
                dz = 0.000
                dx = -0.167
                dy = -0.063

                
            nt = 100


            start_pose = arm.get_current_pose(arm.get_end_effector_link()).pose
            wpose = copy.deepcopy(start_pose)
            waypoints = []
            for j in range(nt):    
                wpose.position.z -= 0.037/nt
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
                # rospy.sleep(0.1)
            else :
                rospy.INFO("Path planning failed with only %0.6f success after %d attempts.", fraction, maxtries)


            # print(123)

            nt = 100


            start_pose = arm.get_current_pose(arm.get_end_effector_link()).pose
            wpose = copy.deepcopy(start_pose)
            waypoints = []

            for j in range(nt):    
                wpose.position.z += (0.067 - dz)/nt
                waypoints.append(copy.deepcopy(wpose))

            for j in range(nt):    
                wpose.position.x += dx/nt
                waypoints.append(copy.deepcopy(wpose))
            
            if dy != 0.00 :
                for j in range(nt):    
                    wpose.position.y += dy/nt
                    waypoints.append(copy.deepcopy(wpose))

            for j in range(nt):    
                wpose.position.z -= 0.037/nt
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
                # rospy.sleep(0.1)
            else :
                rospy.INFO("Path planning failed with only %0.6f success after %d attempts.", fraction, maxtries)

            
        RobotCase.pub_state(usb7_off)



        #走轨迹
    def test1(arm):

        joint_positions = [0.0, -0.0523, 1.57, 0.0, 1.6223, 0.0]
        arm.set_joint_value_target(joint_positions)
        arm.set_start_state_to_current_state()
        arm.go()

        rospy.sleep(0.5)

        start_pose = arm.get_current_pose(arm.get_end_effector_link()).pose
        # print(target_pose)
        wpose = copy.deepcopy(start_pose)
        waypoints = []


        nt = 1500
        for i in range(nt):    
            wpose.position.x -= 0.02/nt
            waypoints.append(copy.deepcopy(wpose))

        for i in range(nt):
            wpose.position.y -= 0.02/nt
            waypoints.append(copy.deepcopy(wpose))

        for i in range(nt):
            wpose.position.x += 0.02/nt
            waypoints.append(copy.deepcopy(wpose))

        for i in range(nt):
            wpose.position.x += 0.015/nt
            wpose.position.y -= 0.022/nt
            waypoints.append(copy.deepcopy(wpose))

        for i in range(nt):
            wpose.position.x += 0.015/nt
            wpose.position.y += 0.022/nt
            waypoints.append(copy.deepcopy(wpose))


        radius = 0.03
        centerA = wpose.position.y
        centerB = wpose.position.x + radius
        th = 3.14
        while th < 6.28 :
            wpose.position.y = centerA + radius * math.sin(th)
            wpose.position.x = centerB + radius * math.cos(th)
            waypoints.append(copy.deepcopy(wpose))
            print(wpose.position)

            th = th + 0.001


        for i in range(nt):    
            wpose.position.x += 0.02/nt
            waypoints.append(copy.deepcopy(wpose))


        radius = 0.03
        centerA = wpose.position.y
        centerB = wpose.position.x + radius
        th = 3.14
        while th < 6.28 :
            wpose.position.y = centerA + radius * math.sin(th)
            wpose.position.x = centerB + radius * math.cos(th)
            waypoints.append(copy.deepcopy(wpose))
            print(wpose.position)

            th = th + 0.001

        radius = 0.025
        centerA = wpose.position.y
        centerB = wpose.position.x - radius
        th = 0.09
        while th < 3.14 :
            wpose.position.y = centerA + radius * math.sin(th)
            wpose.position.x = centerB + radius * math.cos(th)
            waypoints.append(copy.deepcopy(wpose))
            print(wpose.position)

            th = th + 0.001

        radius = 0.02
        centerA = wpose.position.y
        centerB = wpose.position.x + radius
        th = 3.14
        while th < 6.28 :
            wpose.position.y = centerA + radius * math.sin(th)
            wpose.position.x = centerB + radius * math.cos(th)
            waypoints.append(copy.deepcopy(wpose))
            print(wpose.position)

            th = th + 0.01


        jump_threshold = 0.0
        eef_step = 0.01
        fraction = 0.0
        maxtries = 100
        attempts = 0
        plan = None


        while fraction < 1.0 and attempts < maxtries :
            (plan, fraction) = arm.compute_cartesian_path(waypoints, eef_step, jump_threshold)
            attempts += 1
            if attempts % 10 == 0 :
                rospy.loginfo("Still trying after %d attempts...", attempts)
        
        if fraction == 1.0:
            rospy.loginfo("Path computed successfully. Moving the arm.")
            arm.execute(plan)
            rospy.sleep(0.1)


    #走直线
    def test2(arm):

        joint_positions = [0.0, -0.0523, 1.57, 0.0, 1.6223, 0.0]
        arm.set_joint_value_target(joint_positions)
        arm.set_start_state_to_current_state()
        arm.go()

        # 获取当前位姿数据最为机械臂运动的起始位姿
        start_pose = arm.get_current_pose(arm.get_end_effector_link()).pose

        # 设置路点数据，并加入路点列表
        wpose = copy.deepcopy(start_pose)
        
        waypoints = []

        #计算机械臂运动的动作组
        nt = 1000
        for i in range(nt):
            wpose.position.x -= 0.1/nt
            waypoints.append(copy.deepcopy(wpose))

        for i in range(nt):
            wpose.position.x += 0.2/nt
            waypoints.append(copy.deepcopy(wpose))
            
        for i in range(nt):
            wpose.position.x -= 0.1/nt
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
            rospy.sleep(0.1)
        else :
            rospy.INFO("Path planning failed with only %0.6f success after %d attempts.", fraction, maxtries)

    def test(arm):
        #  = PoseStamped()
        # target_pose.header.frame_id = 'base_link'
        # target_pose.header.stamp = rospy.Time.now()     
        target_pose = arm.get_current_pose(arm.get_end_effector_link()).pose
        target_pose.pose.position.x = 0.07960
        target_pose.pose.position.y = 0.03778607379067382
        target_pose.pose.position.z = 0.5925131104891832

        # target_pose.pose.orientation.x = 0.5
        # target_pose.pose.orientation.y = 0.5
        # target_pose.pose.orientation.z = -0.5
        # target_pose.pose.orientation.w = 0.5
        # 设置机器臂当前的状态作为运动初始状态
        arm.set_start_state_to_current_state()
        # 设置机械臂终端运动的目标位姿
        arm.set_pose_target(target_pose, arm.get_end_effector_link())
        arm.go()



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

        # # 控制机械臂先回到初始化位置
        # arm.set_named_target('stand')
        # arm.go()

        # rospy.sleep(0.5)


        # joint_positions = [0.0, 0.0, 1.57, 0.0, 1.57, 0.0]
        # arm.set_joint_value_target(joint_positions)
        # arm.set_start_state_to_current_state()
        # arm.go()


        # joint_positions = [0.0, -0.52, 1.57, 0.0, 0.0, 0.0]
        # arm.set_joint_value_target(joint_positions)
        # arm.set_start_state_to_current_state()
        # arm.go()





        # RobotCase.pub_state(usb6_on)
        # rospy.sleep(3)
        # RobotCase.pub_state(usb6_off)

        # RobotCase.pub_state(usb7_on)
        # RobotCase.pub_state(usb5_on)

        # joint_positions = [0.0, 0.0, 1.57, 0.0, 1.57, 0.0]
        # arm.set_joint_value_target(joint_positions)
        # arm.set_start_state_to_current_state()
        # arm.go()


        joint_positions = [0.0, -0.52, 1.57, 0.0, 0.0, 0.0]
        arm.set_joint_value_target(joint_positions)
        arm.set_start_state_to_current_state()
        arm.go()

        RobotCase.demo7(arm)


        # # 控制机械臂先回到初始化位置
        # arm.set_named_target('stand')
        # arm.go()

        # 关闭并退出moveit
        moveit_commander.roscpp_shutdown()
        moveit_commander.os._exit(0)

    except rospy.ROSInterruptException:
        pass


    #    y|
    #<---------x   机械臂     三摄像头 ------->x
    #     |
    #     |向下
    #          
    #
    #
#    x: 0.07959850101776528
#     y: 0.2720580056728038
#     z: 0.3227374236019059
#   orientation: 
#     x: -0.49996231997858864
#     y: 0.4997496331034366
#     z: 0.4998673944200041
#     w: 0.500420394079182
# ^Carm003@arm003-XiaoXin-14-IAH8:~/ro