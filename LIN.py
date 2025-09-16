#!/usr/bin/env python3
import sys
import rospy
import copy
import moveit_commander

def move_along_axis(arm, axis, distance, eef_step=0.01):
    # 获取当前末端位置
    current_pose = arm.get_current_pose().pose
    target_pose = copy.deepcopy(current_pose)

    # 沿指定方向偏移
    if axis == 'x':
        target_pose.position.x += distance
    elif axis == 'y':
        target_pose.position.y += distance
    elif axis == 'z':
        target_pose.position.z += distance
    else:
        rospy.logerr("False %s x/y/z", axis)
        return

    # 规划并执行
    waypoints = [target_pose]
    plan, fraction = arm.compute_cartesian_path(waypoints, eef_step, False)

    if fraction > 0.9:
        arm.execute(plan, wait=True)
        rospy.loginfo("True %s to Move %.3f M", axis, distance)
    else:
        rospy.logwarn("False %.1f%%，缩短距离/+ eef_step", fraction * 100)


if __name__ == "__main__":
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node("move_xyz_demo", anonymous=True)

    arm = moveit_commander.MoveGroupCommander("arm")
    arm.set_pose_reference_frame("base_link")
    arm.set_goal_position_tolerance(0.001)
    arm.set_goal_orientation_tolerance(0.01)
    arm.set_max_velocity_scaling_factor(0.3)
    arm.set_max_acceleration_scaling_factor(0.2)

    rospy.sleep(1.0)

    move_along_axis(arm, axis='y', distance=0.15)
    # move_along_axis(arm, axis='x', distance=-0.10)
    # move_along_axis(arm, axis='y', distance=-0.00)
    moveit_commander.roscpp_shutdown()

