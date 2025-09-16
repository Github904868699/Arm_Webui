import math
import rospy, sys
import copy
import moveit_commander
import moveit_msgs.msg 
import trajectory_msgs.msg 
import geometry_msgs.msg

if __name__ == "__main__":

    # 初始化moveit_commander和ROS节点
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('moveit_circle_demo', anonymous=True)

    # 初始化机械臂的MoveGroupCommander
    arm = moveit_commander.MoveGroupCommander('arm')

    # 获取末端执行器的link名称
    end_effector_link = arm.get_end_effector_link()
    # 设置参考坐标系
    reference_frame = "base_link"
    arm.set_pose_reference_frame(reference_frame)

    # 允许重新规划
    arm.allow_replanning(True)

    # 设置位置和姿态的容差
    arm.set_goal_position_tolerance(0.001)
    arm.set_goal_orientation_tolerance(0.01)

    # 设置最大加速度和速度的缩放因子
    arm.set_max_acceleration_scaling_factor(0.8)
    arm.set_max_velocity_scaling_factor(0.8)

    # 先让机械臂回到初始位置（stand）
    # arm.set_named_target('stand')
    # arm.go()
    # rospy.sleep(1)
    
    # 设置目标关节角度
    joint_positions = [0.0, 0.0, -1.57, 0.0, -1.57, 0.0]

    # 运动到指定关节角度
    arm.set_joint_value_target(joint_positions)
    arm.set_start_state_to_current_state()
    arm.go()

    # 获取当前末端执行器的位姿
    start_pose = arm.get_current_pose(arm.get_end_effector_link()).pose
    wpose = copy.deepcopy(start_pose)
    waypoints = []

    # 设置圆弧的半径
    radius = 0.05
    # 计算圆心  
    centerA = wpose.position.y
    centerB = wpose.position.x + radius

    # 按照圆弧轨迹生成路径点
    th = 0.0
    while th <= 2 * math.pi:
        wpose.position.y = centerA + radius * math.sin(th)
        wpose.position.x = centerB + radius * math.cos(th)
        waypoints.append(copy.deepcopy(wpose))
        th += 0.02  # 建议步长 0.01～0.02，避免太密

    # 轨迹规划参数
    jump_threshold = 0.0
    eef_step = 0.01
    fraction = 0.0
    maxtries = 100
    attempts = 0
    plan = None

    # 尝试多次规划，直到路径完整或达到最大尝试次数
    while fraction < 1.0 and attempts < maxtries :
        (plan, fraction) = arm.compute_cartesian_path(waypoints,0.01,False)

    attempts += 1
    if attempts % 10 == 0 :
        rospy.loginfo("Still trying after %d attempts...", attempts)

    
    if fraction == 1:
        rospy.loginfo("Path computed successfully. Moving the arm.")

        arm.execute(plan)
        # rospy.sleep(100)th planning failed with only %0.6f success after %d attempts.", fraction, maxtries)
        rospy.loginfo("Path planning failed with only %0.6f success after %d attempts.", fraction, maxtries)

    # 运动回初始位置
    arm.set_named_target("stand")
    # joint_positions = [0.0, 0.0, -1.57, 0.0, -1.57, 0.0]
    # arm.set_joint_value_target(joint_positions)
    # arm.set_start_state_to_current_state()
    arm.go()
    print(arm.get_current_pose())
    rospy.sleep(0.1)

    # 关闭moveit_commander
    moveit_commander.roscpp_shutdown()
    moveit_commander.os._exit(0)
