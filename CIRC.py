import os
import sys
import math
import copy
import rospy
import moveit_commander
from geometry_msgs.msg import Pose

def draw_circle(axis="z", center_offset=(0.0, 0.0, 0.0), radius=0.05, steps=100, eef_step=0.01):
    # 初始化 MoveIt 和 ROS 节点
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node("draw_circle_demo", anonymous=True)
    arm = moveit_commander.MoveGroupCommander("arm")
    arm.set_pose_reference_frame("base_link")
    arm.allow_replanning(True)
    arm.set_goal_position_tolerance(0.001)
    arm.set_goal_orientation_tolerance(0.01)

    # ① 记录起始姿态
    # start_pose = arm.get_current_pose().pose
    # rospy.loginfo("记录起始位置：x=%.3f y=%.3f z=%.3f" % (start_pose.position.x,
    #                                                     start_pose.position.y,
    #                                                     start_pose.position.z))
    start_joint_values = arm.get_current_joint_values()
    rospy.loginfo("记录初始关节状态: %s" % str(start_joint_values))
    # 回到初始姿势
    # arm.set_named_target("X")
    # arm.go()
    # rospy.sleep(1.0)

    # 获取当前姿势为基准
    start_pose = arm.get_current_pose().pose
    cx = start_pose.position.x + center_offset[0]/100
    cy = start_pose.position.y + center_offset[1]/100
    cz = start_pose.position.z + center_offset[2]/100

    waypoints = []
    for i in range(steps + 1):
        theta = 2 * math.pi * i / steps
        pose = copy.deepcopy(start_pose)

        if axis == "x":
            pose.position.y = cy + (radius/100) * math.cos(theta)
            pose.position.z = cz + (radius/100) * math.sin(theta)
            pose.position.x = cx
        elif axis == "y":
            pose.position.x = cx + (radius/100) * math.cos(theta)
            pose.position.z = cz + (radius/100) * math.sin(theta)
            pose.position.y = cy
        elif axis == "z":
            pose.position.x = cx + (radius/100) * math.cos(theta)
            pose.position.y = cy + (radius/100) * math.sin(theta)
            pose.position.z = cz
        else:
            rospy.logerr("不支持的轴：%s" % axis)
            return

        waypoints.append(pose)

    # 计算轨迹
    plan, fraction = arm.compute_cartesian_path(waypoints, eef_step, False)

    if fraction < 0.9:
        rospy.logwarn(" Flase %.1f%%， -radius/+eef_step", fraction * 100)
    else:
        rospy.loginfo("True %.1f%%", fraction * 100)
        arm.execute(plan, wait=True)

    rospy.loginfo("Planning to Back")
    arm.set_joint_value_target(start_joint_values)
    plan_back = arm.plan()
    if plan_back and plan_back[0]:
        arm.execute(plan_back[1], wait=True)
        rospy.loginfo("True back to start position")
    else:
        rospy.logwarn("False back to start position")

if __name__ == "__main__":
    draw_circle(
        axis="y",               # "x" "y" "z"
        center_offset=(0,5,-10),  # 圆心偏移量cm
        radius=6,            # 圆的半径cm
        steps=100,              # 圆周离散点数
        eef_step=0.01          # 插值步长,越小轨迹越平滑，但越慢
    )
