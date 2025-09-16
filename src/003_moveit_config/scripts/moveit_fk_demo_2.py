#!/usr/bin/env python
# -*- coding: utf-8 -*-

#用于展示搬运的运动学正解demo

import rospy, sys
import moveit_commander
from control_msgs.msg import GripperCommand

class MoveItFkDemo:
    def __init__(self):
        # 初始化move_group的API
        moveit_commander.roscpp_initialize(sys.argv)

        # 初始化ROS节点
        rospy.init_node('moveit_fk_demo', anonymous=True)
 
        # 初始化需要使用move group控制的机械臂中的arm group
        arm = moveit_commander.MoveGroupCommander('arm')
        
        # 设置机械臂和夹爪的允许误差值
        arm.set_goal_joint_tolerance(0.001)
        #gripper.set_goal_joint_tolerance(0.001)
        
        while not rospy.is_shutdown():
            print(arm.get_current_pose())
            rospy.sleep(1)
        
        # 关闭并退出moveit
        moveit_commander.roscpp_shutdown()
        moveit_commander.os._exit(0)
        
if __name__ == "__main__":
    try:
        MoveItFkDemo()
    except rospy.ROSInterruptException:
        pass










#   position: 
#     x: 0.07892708225298968
#     y: -0.26985675109924034
#     z: 0.1678777885584007
#   orientation: 
#     x: 0.5010755147529511
#     y: 0.5028447189926422
#     z: -0.4989207286862227
#     w: 0.49714044653747924

# joint_positions = [0.0, 0.0, -1.57, 0.0, -1.57, 0.0]
        # arm.set_joint_value_target(joint_positions)
        # arm.set_start_state_to_current_state()
        # arm.go()
        # rospy.sleep(1)


#0.079, -0.27, 0.23 , 0.5 0.5 -0.5 0.5