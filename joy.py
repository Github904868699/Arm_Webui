#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Joy
import moveit_commander
import geometry_msgs.msg

class JoyTeleopMoveIt:
    def __init__(self):
        rospy.init_node('joy_teleop_moveit')
        
        # 初始化 MoveIt
        moveit_commander.roscpp_initialize([])
        self.robot = moveit_commander.RobotCommander()
        self.scene = moveit_commander.PlanningSceneInterface()
        self.group = moveit_commander.MoveGroupCommander("arm")  # 修改为你自己 move_group 的名字
        self.group.set_max_velocity_scaling_factor(0.3)
        self.group.set_max_acceleration_scaling_factor(0.3)

        # 订阅手柄数据
        rospy.Subscriber("/joy", Joy, self.joy_callback)

        # 控制增量
        self.step = 0.01

        rospy.loginfo("Joystick MoveIt Teleop is ready!")

    def joy_callback(self, data: Joy):
        # 手柄按键或方向控制
        dx = dy = dz = 0.0

        if data.axes[7] == 1.0:  # Left
            dy = self.step
        elif data.axes[7] == -1.0:  # Right
            dy = -self.step
        if data.axes[6] == -1.0:  # Up
            dx = self.step
        elif data.axes[6] == 1.0:  # Down
            dx = -self.step

        # A（按钮0）上升，B（按钮1）下降
        if data.buttons[0]:  # A
            dz = self.step
        elif data.buttons[1]:  # B
            dz = -self.step
        # X
        if data.buttons[2]:
            self.group.set_named_target("X")
            success = self.group.go(wait=True)
            self.group.stop()
            self.group.clear_pose_targets()
        # Y
        if data.buttons[3]:
            self.group.set_named_target("stand")
            success = self.group.go(wait=True)
            self.group.stop()
            self.group.clear_pose_targets()
        if data.buttons[4]: #LB
            self.group.set_named_target("S")
            success = self.group.go(wait=True)
            self.group.stop()
            self.group.clear_pose_targets()
        # if data.buttons[5]: #RB
        #     self.group.set_named_target("")
        #     success = self.group.go(wait=True)
        #     self.group.stop()
        #     self.group.clear_pose_targets()
        # 若没有按键动作，则不执行
        if dx == 0.0 and dy == 0.0 and dz == 0.0:
            return

        self.move_relative(dx, dy, dz)

    def move_relative(self, dx, dy, dz):
        pose = self.group.get_current_pose().pose

        # 修改目标位置
        pose.position.x += dx
        pose.position.y += dy
        pose.position.z += dz

        self.group.set_pose_target(pose)

        success = self.group.go(wait=True)
        self.group.stop()
        self.group.clear_pose_targets()

        rospy.loginfo(f"Move executed: dx={dx}, dy={dy}, dz={dz} -> success: {success}")
    

if __name__ == '__main__':
    try:
        JoyTeleopMoveIt()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass

