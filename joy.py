#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Joy
import moveit_commander


class JoyTeleopMoveIt:
    def __init__(self):
        rospy.init_node("joy_teleop_moveit")

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
        self.cartesian_step = rospy.get_param("~cartesian_step", 0.01)
        self.joint_step = rospy.get_param("~joint_step", 0.05)
        self.webui_frame_id = rospy.get_param("~webui_frame_id", "arm_webui")

        rospy.loginfo(
            "Joystick MoveIt Teleop is ready! (cartesian_step=%.3f, joint_step=%.3f)",
            self.cartesian_step,
            self.joint_step,
        )

    def joy_callback(self, data: Joy):
        """根据不同来源的 /joy 消息执行控制"""
        if data.header.frame_id == self.webui_frame_id:
            handled = self.handle_webui_message(data)
            if not handled:
                rospy.logdebug("WebUI message received but no action was triggered.")
        else:
            self.handle_legacy_message(data)

    def handle_webui_message(self, data: Joy) -> bool:
        """处理来自 Web UI 的消息."""
        handled = False
        if data.axes:
            handled = self.handle_joint_axes(data) or handled
        if data.buttons:
            handled = self.handle_cartesian_buttons(data) or handled
        return handled

    def handle_joint_axes(self, data: Joy) -> bool:
        """依据轴向值调整关节."""
        joint_values = self.group.get_current_joint_values()
        max_axes = min(len(joint_values), len(data.axes), 6)
        updated = False

        for idx in range(max_axes):
            value = data.axes[idx]
            if abs(value) > 1e-3:
                joint_values[idx] += value * self.joint_step
                updated = True

        if updated:
            self.group.go(joint_values, wait=True)
            self.group.stop()
            self.group.clear_pose_targets()
            rospy.loginfo("Joint update executed with step %.3f", self.joint_step)

        return updated

    def handle_cartesian_buttons(self, data: Joy) -> bool:
        """处理笛卡尔方向按钮."""
        buttons = list(data.buttons)
        if len(buttons) < 6:
            return False

        pos_x = 1 if buttons[0] else 0
        neg_x = 1 if buttons[1] else 0
        pos_y = 1 if buttons[2] else 0
        neg_y = 1 if buttons[3] else 0
        pos_z = 1 if buttons[4] else 0
        neg_z = 1 if buttons[5] else 0

        dx = self.cartesian_step * (pos_x - neg_x)
        dy = self.cartesian_step * (pos_y - neg_y)
        dz = self.cartesian_step * (pos_z - neg_z)

        if dx or dy or dz:
            self.move_relative(dx, dy, dz)
            return True

        return False

    def handle_legacy_message(self, data: Joy) -> None:
        """保留原有手柄映射，兼容实体手柄."""
        dx = dy = dz = 0.0

        if len(data.axes) > 7:
            if data.axes[7] == 1.0:  # Left
                dy = self.cartesian_step
            elif data.axes[7] == -1.0:  # Right
                dy = -self.cartesian_step
            if data.axes[6] == -1.0:  # Up
                dx = self.cartesian_step
            elif data.axes[6] == 1.0:  # Down
                dx = -self.cartesian_step

        # A（按钮0）上升，B（按钮1）下降
        if len(data.buttons) > 0 and data.buttons[0]:
            dz = self.cartesian_step
        elif len(data.buttons) > 1 and data.buttons[1]:
            dz = -self.cartesian_step

        # X
        if len(data.buttons) > 2 and data.buttons[2]:
            self.move_to_named("X")
        # Y
        if len(data.buttons) > 3 and data.buttons[3]:
            self.move_to_named("stand")
        if len(data.buttons) > 4 and data.buttons[4]:  # LB
            self.move_to_named("S")

        if dx or dy or dz:
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

        rospy.loginfo(
            "Move executed: dx=%s, dy=%s, dz=%s -> success: %s",
            dx,
            dy,
            dz,
            success,
        )

    def move_to_named(self, target):
        self.group.set_named_target(target)
        success = self.group.go(wait=True)
        self.group.stop()
        self.group.clear_pose_targets()
        rospy.loginfo("Move to named target '%s' -> success: %s", target, success)


if __name__ == "__main__":
    try:
        JoyTeleopMoveIt()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass

