#include "ros/ros.h"
#include <tf/tf.h>
#include "dynamic_reconfigure/server.h"
#include "armcontrol_demo_pkg/DynamicParamConfig.h"
#include "armcontrol_demo_pkg/hdrarm_msg.h"

//命令初始值(初始姿态)
armcontrol_demo_pkg::hdrarm_msg msg;
//欧拉角转四元数
geometry_msgs::Quaternion q;

//动态调参回调函数
void paramCallback(armcontrol_demo_pkg::DynamicParamConfig& config,uint32_t level)
{
    //数据更新
    msg.motor_state = config.motor_state.c_str();
    msg.arm_mode = config.arm_mode.c_str();
    msg.Emergency_Stop = config.Emergency_Stop;
    msg.drag_teachin = config.drag_teachin.c_str();
    msg.drag_teachin_name = config.drag_teachin_name.c_str();

    msg.joint1_angle = config.joint1_angle;
    msg.joint2_angle = config.joint2_angle;
    msg.joint3_angle = config.joint3_angle;
    msg.joint4_angle = config.joint4_angle;
    msg.joint5_angle = config.joint5_angle;
    msg.joint6_angle = config.joint6_angle;

    msg.arm_position_x = config.arm_position_x;
    msg.arm_position_y = config.arm_position_y;
    msg.arm_position_z = config.arm_position_z;
    q=tf::createQuaternionMsgFromRollPitchYaw(config.arm_orientation_roll,config.arm_orientation_pitch,config.arm_orientation_yaw);
    msg.arm_orientation_x = q.x;
    msg.arm_orientation_y = q.y;
    msg.arm_orientation_z = q.z;
    msg.arm_orientation_w = q.w;

/*     ROS_INFO("Request: %s %0.3f %0.3f %0.3f %0.3f %0.3f %0.3f %s %0.3f",
                config.arm_mode.c_str(),
                config.arm_position_x,
                config.arm_position_y,
                config.arm_position_z,
                config.arm_orientation_roll,
                config.arm_orientation_pitch,
                config.arm_orientation_yaw,
                config.gripper_mode.c_str(),
                config.gripper_effort); */

}

int main(int argc, char** argv)
{
    //初始化节点
    ros::init(argc,argv,"armcontrol_demo_node");
    // 创建节点句柄
    ros::NodeHandle n;
    //创建动态调参节点
    dynamic_reconfigure::Server<armcontrol_demo_pkg::DynamicParamConfig> server;
    dynamic_reconfigure::Server<armcontrol_demo_pkg::DynamicParamConfig>::CallbackType f;
    f = boost::bind(&paramCallback,_1,_2);
    server.setCallback(f);

    // 创建Publisher
    ros::Publisher armcontrol_pub = n.advertise<armcontrol_demo_pkg::hdrarm_msg>("/armcontrol_Info", 100);
    // 设置循环的频率（单位Hz）
    ros::Rate loop_rate(10);

    //初始化位姿参数
    msg.motor_state = "disable";
    msg.arm_mode = "arm_sleep";
    msg.Emergency_Stop = false;
    msg.drag_teachin = "false";
    msg.drag_teachin_name = "drag_teachin_1.txt";

    msg.joint1_angle = 0.0;
    msg.joint2_angle = 0.0;
    msg.joint3_angle = 0.0;
    msg.joint4_angle = 0.0;
    msg.joint5_angle = 0.0;
    msg.joint6_angle = 0.0;

    msg.arm_position_x = 0.2;
    msg.arm_position_y = 0.0;
    msg.arm_position_z = 0.3;
    msg.arm_orientation_x = 0.0;
    msg.arm_orientation_y = 0.0;
    msg.arm_orientation_z = 0.0;
    msg.arm_orientation_w = 1.0;

    while (ros::ok())
    {
        //发布控制信息
        armcontrol_pub.publish(msg);

        // 循环等待回调函数
        ros::spinOnce();
        ROS_INFO("HDR_Arm control information is being released");

        // 按照循环频率延时
        loop_rate.sleep();
    }

    return 0;
}