

# -*- coding: utf-8 -*-
 
import rospy, sys
import copy
import moveit_commander
from moveit_commander import MoveGroupCommander
from copy import deepcopy
import geometry_msgs.msg
from std_msgs.msg import String
import cv2 
import math
from geometry_msgs.msg import PoseStamped, Pose
import numpy as np
import threading
import serial

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

ser = serial.Serial("/dev/ttyCH341USB0", baudrate = 9600, bytesize = 8, parity = 'N', stopbits = 1)

def pub_state(state):

    # pub = rospy.Publisher("jdq_state", String, queue_size=10)     
    # msg = String()
    # msg.data = state
    # rate = rospy.Rate(1)

    # nt = 0
    # while not rospy.is_shutdown():
        
    #     nt += 1
    #     pub.publish(msg)
    #     rate.sleep()
    #     rospy.loginfo("发布指令:%s", msg.data)

    #     if nt >= 2:
    #         break

    byte_array = bytearray.fromhex(state)

    ser.write(byte_array)

def camera(n):
    
    cap = cv2.VideoCapture(2)
    i = 0
    while True:
        print(i)
        if i >= n:
            break
        ret, frame = cap.read() #读取一帧图像
        if not ret:
            break
        print(frame.shape)
        frame1 = cv2.resize(frame, (2560, 720))
        print(frame1.shape)
        # print(frame1.shape)
        cv2.imwrite('/home/arm003/yolov5-master/img.jpg', frame1) #保存为JPEG格式
        # break

        i += 1
  

    cap.release() #释放摄像头资源
    cv2.destroyAllWindows() #销毁所有窗口


    #坐标计算完毕，可以进行规划
    with open("/home/arm003/yolov5-master/get.txt", "w", encoding='utf-8') as f:
        print('拍照完毕')
        f.write('calculate')
        f.close()


def plan(arm):

    # dx = dy = dz = 0.0

    with open("/home/arm003/yolov5-master/result.txt", "r", encoding='utf-8') as f:
        # 读取数据    
        lines = f.readlines()
        tms = 0 
        for line in lines: 
            s = str(line).split(",")
            x = '%.5f'%float(s[0])
            y = '%.5f'%float(s[1])
            z = '%.5f'%float(s[2])
            dx = float(x)/100.0
            dy = float(y)/100.0
            dz = float(z)/100.0
            print(dx,dy,dz)
        
            #计算目标物体与吸嘴的相对坐标
            x = -(dx - 0.594)
            y = dy + 0.02
            z = -(dz - 0.128)
            print('目标坐标为：', x, y, z)

            # 获取当前位姿数据最为机械臂运动的起始位姿
            start_pose = arm.get_current_pose(arm.get_end_effector_link()).pose

            # 设置路点数据，并加入路点列表
            wpose = copy.deepcopy(start_pose)
            
            waypoints = []

            #计算机械臂运动的动作组
            nt = 100

            for i in range(nt):
                wpose.position.z += (z/2)/nt
                waypoints.append(copy.deepcopy(wpose))
            for i in range(nt):
                wpose.position.y += 0.65*y/nt
                waypoints.append(copy.deepcopy(wpose))
            for i in range(nt):
                wpose.position.x += (x/2)/nt
                waypoints.append(copy.deepcopy(wpose))
            for i in range(nt):
                wpose.position.z += (z/2)/nt
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
                pub_state(usb6_on)
                rospy.sleep(0.1)
            else :
                rospy.INFO("Path planning failed with only %0.6f success after %d attempts.", fraction, maxtries)


            joint_positions = [0.0, 0.0, 0.52, -1.04, 1.57, 0.11]
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
                wpose.position.z -= 0.2/nt
                # wpose.position.z -= (0.2 - tms * 0.03)/nt
                waypoints.append(copy.deepcopy(wpose))
            for i in range(nt):
                wpose.position.y += 0.1/nt
                waypoints.append(copy.deepcopy(wpose))
            for i in range(nt):
                wpose.position.x += 0.2/nt
                waypoints.append(copy.deepcopy(wpose))
            for i in range(nt):
                wpose.position.z -= 0.05/nt
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
                pub_state(usb6_off)
                rospy.sleep(0.1)
            else :
                rospy.INFO("Path planning failed with only %0.6f success after %d attempts.", fraction, maxtries)


            joint_positions = [0.0, 0.0, 0.52, -1.04, 1.57, 0.11]
            arm.set_joint_value_target(joint_positions)
            arm.set_start_state_to_current_state()
            arm.go()

            tms += 1
        
        f.close()

    with open("/home/arm003/yolov5-master/get.txt", "w", encoding='utf-8') as f:
        print('拍照完毕')
        f.write('camera')
        f.close()

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

        joint_positions = [0.0, 0.0, 0.52, -1.04, 1.57, 0.11]
        arm.set_joint_value_target(joint_positions)
        arm.set_start_state_to_current_state()
        arm.go()
        
        camera(7)
        i = 0
        nt = 0
        while True:
            
            s = ''

            with open("/home/arm003/yolov5-master/get.txt", "r", encoding='utf-8') as f:
                s = f.readline()
                f.close()

            if s == 'plan':
                i += 1
                print('第' + str(i) + '次抓取')
                plan(arm)

            if s == 'camera':
                camera(4)



        


        # 控制机械臂先回到初始化位置
        # arm.set_named_target('stand')
        # arm.go()

        # 关闭并退出moveit
        moveit_commander.roscpp_shutdown()
        moveit_commander.os._exit(0)

    except rospy.ROSInterruptException:
        pass

# 机械臂坐标
    #    y| 
    #<---------x   机械臂     三摄像头 ------->x
    #     |
    #     |向下
    #      
    # 摄像头坐标
    #     |y    
    #x-------->
    #     |
    #     |向下
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



# 吸嘴 的三维坐标 (x:29.4cm, y:-2.0cm, z:29cm)



