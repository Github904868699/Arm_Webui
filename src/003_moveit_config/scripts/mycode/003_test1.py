# import math
# import rospy, sys
# import copy
# import moveit_commander
# import moveit_msgs.msg
# import trajectory_msgs.msg
# import geometry_msgs.msg

# if __name__ == "__main__":

#     moveit_commander.roscpp_initialize(sys.argv)
#     rospy.init_node('moveit_circle_demo', anonymous=True)

#     # 初始化机械臂控制组
#     arm = moveit_commander.MoveGroupCommander('arm')

#     # 获取末端执行器链接和参考坐标系
#     end_effector_link = arm.get_end_effector_link()
#     reference_frame = "base_link"
#     arm.set_pose_reference_frame(reference_frame)

#     # 设置一些参数
#     arm.allow_replanning(True)
#     arm.set_goal_position_tolerance(0.001)
#     arm.set_goal_orientation_tolerance(0.01)
#     arm.set_max_acceleration_scaling_factor(0.8)
#     arm.set_max_velocity_scaling_factor(0.8)

#     # 设定起始位置
#     arm.set_named_target('stand')
#     arm.go()
#     rospy.sleep(1)
    
#     joint_positions = [0.0, 0.0, -1.57, 0.0, -1.57, 0.0]

#     arm.set_joint_value_target(joint_positions)
#     arm.set_start_state_to_current_state()
#     arm.go()

#     start_pose = arm.get_current_pose(arm.get_end_effector_link()).pose
#     wpose = copy.deepcopy(start_pose)

#     waypoints = []

#     # 矩形的边长和偏移量
#     side_length = 0.06  # 可根据需要调整
#     offset = 0.05  # 可根据需要调整

#     # 计算矩形的四个顶点
#     top_left = geometry_msgs.msg.Pose()
#     top_left.position.x = start_pose.position.x - side_length / 2
#     top_left.position.y = start_pose.position.y + side_length / 2
#     top_left.position.z = start_pose.position.z
#     top_left.orientation = geometry_msgs.msg.Quaternion(0, 0, 0, 1)

#     top_right = geometry_msgs.msg.Pose()
#     top_right.position.x = start_pose.position.x + side_length / 2
#     top_right.position.y = start_pose.position.y + side_length / 2
#     top_right.position.z = start_pose.position.z
#     top_right.orientation = geometry_msgs.msg.Quaternion(0, 0, 0, 1)

#     # bottom_right = geometry_msgs.msg.Pose()
#     # bottom_right.position.x = start_pose.position.x + side_length / 2
#     # bottom_right.position.y = start_pose.position.y - side_length / 2
#     # bottom_right.position.z = start_pose.position.z
#     # bottom_right.orientation = geometry_msgs.msg.Quaternion(0, 0, 0, 1)

#     # bottom_left = geometry_msgs.msg.Pose()
#     # bottom_left.position.x = start_pose.position.x - side_length / 2
#     # bottom_left.position.y = start_pose.position.y - side_length / 2
#     # bottom_left.position.z = start_pose.position.z
#     # bottom_left.orientation = geometry_msgs.msg.Quaternion(0, 0, 0, 1)

#     # 将四个顶点添加到路径点列表
#     waypoints.append(copy.deepcopy(top_left))
#     waypoints.append(copy.deepcopy(top_right))
#     # waypoints.append(copy.deepcopy(bottom_right))
#     # waypoints.append(copy.deepcopy(bottom_left))

#     jump_threshold = 0.0
#     eef_step = 0.01
#     fraction = 0.0
#     maxtries = 100
#     attempts = 0
#     plan = None

#     while fraction < 1.0 and attempts < maxtries :
#         (plan, fraction) = arm.compute_cartesian_path(waypoints, eef_step, jump_threshold)
#         attempts += 1
#         if attempts % 10 == 0 :
#             rospy.loginfo("Still trying after %d attempts...", attempts)

#     if fraction == 1:
#         rospy.loginfo("Path computed successfully. Moving the arm.")
#         arm.execute(plan)
#         rospy.sleep(0.1)
#     else :
#         rospy.loginfo("Path planning failed with only %0.6f success after %d attempts.", fraction, maxtries)

#     arm.set_named_target("stand")
#     arm.go()

#     moveit_commander.roscpp_shutdown()
#     moveit_commander.os._exit(0)


import math
import rospy, sys
import copy
import moveit_commander
import moveit_msgs.msg
import trajectory_msgs.msg
import geometry_msgs.msg

if __name__ == "__main__":

    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('moveit_square_demo', anonymous=True)

    # 初始化机械臂控制组
    arm = moveit_commander.MoveGroupCommander('arm')

    # 获取末端执行器链接和参考坐标系
    end_effector_link = arm.get_end_effector_link()
    reference_frame = "base_link"
    arm.set_pose_reference_frame(reference_frame)

    # 设置一些参数
    arm.allow_replanning(True)
    arm.set_goal_position_tolerance(0.001)
    arm.set_goal_orientation_tolerance(0.01)
    arm.set_max_acceleration_scaling_factor(0.8)
    arm.set_max_velocity_scaling_factor(0.8)

    # 设定起始位置
    arm.set_named_target('stand')
    arm.go()
    rospy.sleep(1)

    joint_positions = [0.0, 0.0, -1.57, 0.0, -1.57, 0.0]

    arm.set_joint_value_target(joint_positions)
    arm.set_start_state_to_current_state()
    arm.go()

    start_pose = arm.get_current_pose(arm.get_end_effector_link()).pose
    wpose = copy.deepcopy(start_pose)

    waypoints = []

    # 方形的边长和偏移量（在 X 轴和 Y 轴平面上）
    side_length = 0.04  # 可根据需要调整
    offset = 0.05  # 可根据需要调整

    # # 假设 start_pose 是机械臂当前的姿态
    # start_pose = geometry_msgs.msg.Pose()

    # 计算方形的四个顶点
    top_left = geometry_msgs.msg.Pose()
    top_left.position.x = start_pose.position.x - side_length / 2
    top_left.position.y = start_pose.position.y + side_length / 2
    top_left.position.z = start_pose.position.z  # 保持在同一平面
    # top_left.orientation = geometry_msgs.msg.Quaternion(1, 0, 0, 0)  # 末端朝下

    top_right = geometry_msgs.msg.Pose()
    top_right.position.x = start_pose.position.x + side_length / 2
    top_right.position.y = start_pose.position.y + side_length / 2
    top_right.position.z = start_pose.position.z  # 保持在同一平面
    # top_right.orientation = geometry_msgs.msg.Quaternion(0, 1, 0, 0)  # 末端朝下

    bottom_right = geometry_msgs.msg.Pose()
    bottom_right.position.x = start_pose.position.x + side_length / 2
    bottom_right.position.y = start_pose.position.y - side_length / 2
    bottom_right.position.z = start_pose.position.z  # 保持在同一平面
    # bottom_right.orientation = geometry_msgs.msg.Quaternion(0, 0, 1, 0)  # 末端朝下

    bottom_left = geometry_msgs.msg.Pose()
    bottom_left.position.x = start_pose.position.x - side_length / 2
    bottom_left.position.y = start_pose.position.y - side_length / 2
    bottom_left.position.z = start_pose.position.z  # 保持在同一平面
    # bottom_left.orientation = geometry_msgs.msg.Quaternion(0, 0, 0, -1)  # 末端朝下

    # 设置末端朝向 z 轴负方向的四元数
    z_neg_orientation = geometry_msgs.msg.Quaternion(0, 0, 1, 0)

    # 应用这个姿态到四个顶点
    top_left.orientation = z_neg_orientation
    top_right.orientation = z_neg_orientation
    bottom_right.orientation = z_neg_orientation
    bottom_left.orientation = z_neg_orientation

    # 将四个顶点添加到路径点列表
    waypoints.append(copy.deepcopy(top_left))
    waypoints.append(copy.deepcopy(top_right))
    waypoints.append(copy.deepcopy(bottom_right))
    waypoints.append(copy.deepcopy(bottom_left))

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

    if fraction == 1:
        rospy.loginfo("Path computed successfully. Moving the arm.")
        arm.execute(plan)
        rospy.sleep(0.1)
    else :
        rospy.loginfo("Path planning failed with only %0.6f success after %d attempts.", fraction, maxtries)

    arm.set_named_target("stand")
    arm.go()

    moveit_commander.roscpp_shutdown()
    moveit_commander.os._exit(0)

