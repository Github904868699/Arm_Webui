/**
 * 电机控制API
 */
#include <iostream>
#include <sstream>
#include <ros/ros.h>
#include <geometry_msgs/Twist.h>
#include <signal.h>
#include <chrono>
#include <memory>
#include <cmath>
#include <fstream>
#include <regex>
#include <ros/package.h>
#include "stdint.h"
#include "can_msgs/Frame.h"
#include "std_msgs/String.h"
#include "dm_motor/motor_config.h"
#include "dm_motor/drag_teachin.h"
#include "dm_motor/MotorFeedback.h"
#include "dm_motor/hdrarm_msg.h"
#include "sensor_msgs/JointState.h"
#include <moveit/move_group_interface/move_group_interface.h>

//声明变量
ros::Publisher can1_pub;
std::unique_ptr<moveit::planning_interface::MoveGroupInterface> arm;

//定义需要监看的时间点
clock_t t_enable_motor, t_disable_motor, t_now;

//电机软启动系数
float gravity_compensation_k = 0.0;

//拖动示教的上时刻状态，辅助关闭文件
string teachin_last_mode = "false";

//正常运动控制状态下的模式切换检测
string arm_mode_last = "arm_init_finish";

//关键保护，需要将急停置为1清除
bool key_protect = false;

//上电回零过程记录起始角度
float zero_start_pos[6] = {0};
bool zero_return_init = false;
//定义关节电机对象
MotorControlSet motor_1(MOTOR_1,"DM4340");
MotorControlSet motor_2(MOTOR_2,"DM4340");
MotorControlSet motor_3(MOTOR_3,"DM4340");
MotorControlSet motor_4(MOTOR_4,"DM4310");
MotorControlSet motor_5(MOTOR_5,"DM4310");
MotorControlSet motor_6(MOTOR_6,"DM4310");

//定义控制信息对象
HdrarmControlSet hdrarm_control;

//使用MoveIt让机械臂回到"stand"姿态
static void moveArmToStand()
{
    if(arm)
    {
        arm->setNamedTarget("stand");
        arm->move();
    }
}

//定义拖动示教文件目录及名称(暂时固定写入名)
//在命令行可使用pwd命令查看当前绝对路径
//DragTeachInSet teach_txt("/home/lyf/roboarm_ws/src/dm_motor/txt/drag_teachin_1.txt");
DragTeachInSet teach_txt;

/********************************* sub回调函数 *********************************/
//电机反馈数据读取回调函数
void can1_rx_Callback(can_msgs::Frame msg)
{
    
    uint8_t  id_hex  = (uint8_t)(msg.data[0]);
    uint16_t pos_hex = (uint16_t)(msg.data[2] | (msg.data[1] << 8));
    uint16_t vel_hex = (uint16_t)(((msg.data[4] & 0xF0) >> 4) | (msg.data[3] << 4));
    uint16_t t_hex   = (uint16_t)((msg.data[5] | (msg.data[4] & 0x0F) << 8));

    //ROS_INFO("id=%d",id_hex);

    switch(id_hex){
        //这里的+MOTOR_ENABLED是指，电机使能后反馈id加了使能标志位，原本是1，使能后为17
        case MOTOR_1+MOTOR_ENABLED:
        {
            motor_1.pos = motor_1.Uint_to_float(pos_hex, motor_1.P_MIN, motor_1.P_MAX, 16);
            motor_1.vel = motor_1.Uint_to_float(vel_hex, motor_1.V_MIN, motor_1.V_MAX, 12);
            motor_1.t   = motor_1.Uint_to_float(t_hex  , motor_1.T_MIN, motor_1.T_MAX, 12);
            //ROS_INFO("id=%d pos=%0.2f vel=%0.2f   t=%0.2f",motor_1.motor_id, motor_1.pos, motor_1.vel, motor_1.t);
            break;
        }
        case MOTOR_2+MOTOR_ENABLED:
        {
            motor_2.pos = motor_2.Uint_to_float(pos_hex, motor_2.P_MIN, motor_2.P_MAX, 16) + MOTOR_2_OFFSET;
            motor_2.vel = motor_2.Uint_to_float(vel_hex, motor_2.V_MIN, motor_2.V_MAX, 12);
            motor_2.t   = motor_2.Uint_to_float(t_hex  , motor_2.T_MIN, motor_2.T_MAX, 12);
            //ROS_INFO("id=%d pos=%0.2f vel=%0.2f   t=%0.2f",motor_2.motor_id, motor_2.pos, motor_2.vel, motor_2.t);
            break;
        }
        case MOTOR_3+MOTOR_ENABLED:
        {
            motor_3.pos = motor_3.Uint_to_float(pos_hex, motor_3.P_MIN, motor_3.P_MAX, 16) + MOTOR_3_OFFSET;
            motor_3.vel = motor_3.Uint_to_float(vel_hex, motor_3.V_MIN, motor_3.V_MAX, 12);
            motor_3.t   = motor_3.Uint_to_float(t_hex  , motor_3.T_MIN, motor_3.T_MAX, 12);
            //ROS_INFO("id=%d pos=%0.2f vel=%0.2f   t=%0.2f",motor_3.motor_id, motor_3.pos, motor_3.vel, motor_3.t);   
            break;
        }
        case MOTOR_4+MOTOR_ENABLED:
        {
            motor_4.pos = motor_4.Uint_to_float(pos_hex, motor_4.P_MIN, motor_4.P_MAX, 16) + MOTOR_4_OFFSET;
            motor_4.vel = motor_4.Uint_to_float(vel_hex, motor_4.V_MIN, motor_4.V_MAX, 12);
            motor_4.t   = motor_4.Uint_to_float(t_hex  , motor_4.T_MIN, motor_4.T_MAX, 12);
            //ROS_INFO("id=%d pos=%0.2f vel=%0.2f   t=%0.2f",motor_4.motor_id, motor_4.pos, motor_4.vel, motor_4.t);  
            break;
        }
        case MOTOR_5+MOTOR_ENABLED:
        {
            motor_5.pos = motor_5.Uint_to_float(pos_hex, motor_5.P_MIN, motor_5.P_MAX, 16);
            motor_5.vel = motor_5.Uint_to_float(vel_hex, motor_5.V_MIN, motor_5.V_MAX, 12);
            motor_5.t   = motor_5.Uint_to_float(t_hex  , motor_5.T_MIN, motor_5.T_MAX, 12);
            //ROS_INFO("id=%d pos=%0.2f vel=%0.2f   t=%0.2f",motor_5.motor_id, motor_5.pos, motor_5.vel, motor_5.t);   
            break;
        }
        case MOTOR_6+MOTOR_ENABLED:
        {
            motor_6.pos = motor_6.Uint_to_float(pos_hex, motor_6.P_MIN, motor_6.P_MAX, 16);
            motor_6.vel = motor_6.Uint_to_float(vel_hex, motor_6.V_MIN, motor_6.V_MAX, 12);
            motor_6.t   = motor_6.Uint_to_float(t_hex  , motor_6.T_MIN, motor_6.T_MAX, 12);
            //ROS_INFO("id=%d pos=%0.2f vel=%0.2f   t=%0.2f",motor_6.motor_id, motor_6.pos, motor_6.vel, motor_6.t);   
            break;
        }
        default:
        {

        }
    }
}

//控制数据刷新
void armcontrol_rx_Callback(const dm_motor::hdrarm_msg hdrarm)
{
    hdrarm_control.motor_state          = hdrarm.motor_state;
    hdrarm_control.arm_mode             = hdrarm.arm_mode;
    hdrarm_control.Emergency_Stop       = hdrarm.Emergency_Stop;
    hdrarm_control.drag_teachin         = hdrarm.drag_teachin;
    hdrarm_control.drag_teachin_name    = hdrarm.drag_teachin_name;

    hdrarm_control.joint1_angle = hdrarm.joint1_angle;
    hdrarm_control.joint2_angle = hdrarm.joint2_angle;
    hdrarm_control.joint3_angle = hdrarm.joint3_angle;
    hdrarm_control.joint4_angle = hdrarm.joint4_angle;
    hdrarm_control.joint5_angle = hdrarm.joint5_angle;
    hdrarm_control.joint6_angle = hdrarm.joint6_angle;

    hdrarm_control.arm_position_x = hdrarm.arm_position_x;
    hdrarm_control.arm_position_y = hdrarm.arm_position_y;
    hdrarm_control.arm_position_z = hdrarm.arm_position_z;
    hdrarm_control.arm_orientation_x = hdrarm.arm_orientation_x;
    hdrarm_control.arm_orientation_y = hdrarm.arm_orientation_y;
    hdrarm_control.arm_orientation_z = hdrarm.arm_orientation_z;
    hdrarm_control.arm_orientation_w = hdrarm.arm_orientation_w;

    //关键保护清除检测
    if(hdrarm_control.Emergency_Stop == 1)
    {
        key_protect = 0;
    }
}

//定义需要跟踪的角度数据
float motor1_gazebo_joints_position = 0.0;
float motor2_gazebo_joints_position = 0.0;
float motor3_gazebo_joints_position = 0.0;
float motor4_gazebo_joints_position = 0.0;
float motor5_gazebo_joints_position = 0.0;
float motor6_gazebo_joints_position = 0.0;

//gazebo下发仿真关节角度回调函数
void gazebo_joint_states_Callback(const sensor_msgs::JointStateConstPtr& joint_states)
{
    //读取角度值
    float gazebo_joints_position[6];
    gazebo_joints_position[0] = joint_states->position[0];
    gazebo_joints_position[1] = joint_states->position[1];
    gazebo_joints_position[2] = joint_states->position[2];
    gazebo_joints_position[3] = joint_states->position[3];
    gazebo_joints_position[4] = joint_states->position[4];
    gazebo_joints_position[5] = joint_states->position[5];
    // ROS_INFO("gazebo_joints_position_1 = %0.2f",gazebo_joints_position[0]);
    // ROS_INFO("gazebo_joints_position_2 = %0.2f",gazebo_joints_position[1]);
    // ROS_INFO("gazebo_joints_position_3 = %0.2f",gazebo_joints_position[2]);
    // ROS_INFO("gazebo_joints_position_4 = %0.2f",gazebo_joints_position[3]);
    // ROS_INFO("gazebo_joints_position_5 = %0.2f",gazebo_joints_position[4]);
    // ROS_INFO("gazebo_joints_position_6 = %0.2f",gazebo_joints_position[5]);

    //这里的系数是统一gazebo和真实机械臂的旋转正方向，将gazebo角度赋予真实机械臂
    motor1_gazebo_joints_position =  -1.0 * gazebo_joints_position[0];
    motor2_gazebo_joints_position =  -1.0 * (gazebo_joints_position[1] - MOTOR_2_OFFSET);
    motor3_gazebo_joints_position =   1.0 * (gazebo_joints_position[2] - MOTOR_3_OFFSET);
    motor4_gazebo_joints_position =   1.0 * (gazebo_joints_position[3] - MOTOR_4_OFFSET);
    motor5_gazebo_joints_position =   1.0 * gazebo_joints_position[4];
    motor6_gazebo_joints_position =   1.0 * gazebo_joints_position[5];

}

//这里主要进行退出前的数据保存、内存清理、告知其他节点等工作
void MySigintHandler(int sig)
{
	ROS_INFO("shutting down!");
	ros::shutdown();
}

/********************************* 功能函数 *********************************/

//失能所有电机
void disable_all_motor(void)
{
    motor_1.motor_disable();
    motor_2.motor_disable();
    motor_3.motor_disable();
    motor_4.motor_disable();
    motor_5.motor_disable();
    motor_6.motor_disable();

    //缓上电逻辑复位
    gravity_compensation_k = 0.0;

    //记录时间
    t_disable_motor = clock();
}

//使能所有电机
void enable_all_motor(void)
{
    motor_1.motor_enable();
    motor_2.motor_enable();
    motor_3.motor_enable();
    motor_4.motor_enable();
    motor_5.motor_enable();
    motor_6.motor_enable();

    //记录时间
    t_enable_motor = clock();
}

//零位参数
void zero_para_motor(void)
{
    motor_1.kv = 0.3;
    motor_2.kv = 0.3;
    motor_3.kv = 0.3;
    motor_4.kv = 0.3;
    motor_5.kv = 0.2;
    motor_6.kv = 0.1;
    motor_1.kp = 0.0;
    motor_2.kp = 0.0;
    motor_3.kp = 0.0;
    motor_4.kp = 0.0;
    motor_5.kp = 0.0;
    motor_6.kp = 0.0;    
    motor_1.vel_target = 0;
    motor_2.vel_target = 0;
    motor_3.vel_target = 0;
    motor_4.vel_target = 0;
    motor_5.vel_target = 0;
    motor_6.vel_target = 0;
    motor_1.pos_target = 0;
    motor_2.pos_target = 0;
    motor_3.pos_target = 0;
    motor_4.pos_target = 0;
    motor_5.pos_target = 0;
    motor_6.pos_target = 0;
    motor_1.t_target = 0;
    motor_2.t_target = 0;
    motor_3.t_target = 0;
    motor_4.t_target = 0;
    motor_5.t_target = 0;
    motor_6.t_target = 0;
}

//重力补偿
void gravity_compensation(void)
{
    float theta2 = -motor_2.pos;                             //二轴重力数学模型等效角度
    float theta3 = -motor_2.pos + motor_3.pos;               //三轴重力数学模型等效角度
    float theta4 = -motor_2.pos + motor_3.pos - motor_4.pos; //四轴重力数学模型等效角度
    //ROS_INFO("theta1=%.2f theta2=%0.2f theta3=%0.2f",theta1, theta2, theta3);
    motor_4.t_target = 0.65*sin(theta4);
    motor_3.t_target = -motor_4.t_target - 3.6*sin(theta3);
    motor_2.t_target = -motor_3.t_target + 7.2*sin(theta2);

    motor_1.t_target = 0;
    motor_5.t_target = 0;
    motor_6.t_target = 0;
}

//机械臂零位到达检测
bool arm_zeroposition_check(void)
{
    if(abs(motor_1.pos)<0.02 && abs(motor_2.pos)<0.02 && abs(motor_3.pos)<0.02 && abs(motor_4.pos)<0.02 && abs(motor_5.pos)<0.02 && abs(motor_6.pos)<0.02)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

//这里实际上是机械臂经常会遇到的一种情况，即关节控制角度反馈与期望差异很大，直接运动会产生很大的阶跃
//产生阶跃的原因是pos_target与pos差异过大，引起mit模式计算的电流很大，产生很大力矩，很大力矩使得速度很快，进而存储动能造成伤害
//因此这里的逻辑应该是，限制MIT协议中位置分量的计算结果
//核心逻辑是，限制kp(pos_target-pos)到一个合理范围

//位置跟踪力矩限制(一般保护)
void motor_energy_limit(float motor1_limit,float motor2_limit,float motor3_limit,float motor4_limit,float motor5_limit,float motor6_limit)
{
    float motor_move_energy;

    motor_move_energy = motor_1.kp*(motor_1.pos_target-motor_1.pos);
    if(motor_move_energy>motor1_limit)
    {
        motor_1.pos_target = (motor1_limit/motor_1.kp) + motor_1.pos;
    }
    else if(motor_move_energy<(-1.0*motor1_limit))
    {
        motor_1.pos_target = (-1.0)*(motor1_limit/motor_1.kp) + motor_1.pos;
    }

    motor_move_energy = motor_2.kp*(motor_2.pos_target-motor_2.pos);
    if(motor_move_energy>motor2_limit)
    {
        motor_2.pos_target = (motor2_limit/motor_2.kp) + motor_2.pos;
    }
    else if(motor_move_energy<(-1.0*motor2_limit))
    {
        motor_2.pos_target = (-1.0)*(motor2_limit/motor_2.kp) + motor_2.pos;
    }

    motor_move_energy = motor_3.kp*(motor_3.pos_target-motor_3.pos);
    if(motor_move_energy>motor3_limit)
    {
        motor_3.pos_target = (motor3_limit/motor_3.kp) + motor_3.pos;
    }
    else if(motor_move_energy<(-1.0*motor3_limit))
    {
        motor_3.pos_target = (-1.0)*(motor3_limit/motor_3.kp) + motor_3.pos;
    }

    motor_move_energy = motor_4.kp*(motor_4.pos_target-motor_4.pos);
    if(motor_move_energy>motor4_limit)
    {
        motor_4.pos_target = (motor4_limit/motor_4.kp) + motor_4.pos;
    }
    else if(motor_move_energy<(-1.0*motor4_limit))
    {
        motor_4.pos_target = (-1.0)*(motor4_limit/motor_4.kp) + motor_4.pos;
    }

    motor_move_energy = motor_5.kp*(motor_5.pos_target-motor_5.pos);
    if(motor_move_energy>motor5_limit)
    {
        motor_5.pos_target = (motor5_limit/motor_5.kp) + motor_5.pos;
    }
    else if(motor_move_energy<(-1.0*motor5_limit))
    {
        motor_5.pos_target = (-1.0)*(motor5_limit/motor_5.kp) + motor_5.pos;
    }

    motor_move_energy = motor_6.kp*(motor_6.pos_target-motor_6.pos);
    if(motor_move_energy>motor6_limit)
    {
        motor_6.pos_target = (motor6_limit/motor_6.kp) + motor_6.pos;
    }
    else if(motor_move_energy<(-1.0*motor6_limit))
    {
        motor_6.pos_target = (-1.0)*(motor6_limit/motor_6.kp) + motor_6.pos;
    }
}

//电机极限角度限制(关键保护，需要进2次急停状态消除)
void motor_angle_limit(float angle1_limit,float angle2_limit,float angle3_limit,float angle4_limit,float angle5_limit,float angle6_limit)
{
    (abs(motor_1.pos) > angle1_limit) ? key_protect = 1 : angle1_limit=angle1_limit ;
    (abs(motor_2.pos) > angle2_limit) ? key_protect = 1 : angle2_limit=angle2_limit ;
    (abs(motor_3.pos) > angle3_limit) ? key_protect = 1 : angle3_limit=angle3_limit ;
    (abs(motor_4.pos) > angle4_limit) ? key_protect = 1 : angle4_limit=angle4_limit ;
    (abs(motor_5.pos) > angle5_limit) ? key_protect = 1 : angle5_limit=angle5_limit ;
   //(abs(motor_6.pos) > angle6_limit) ? key_protect = 1 : angle6_limit=angle6_limit ;
}

//机械臂连贯运动处理(给出连续的pos_target)
void motor_control_continue(void)
{
    //先给出希望到达的关节角度
    if(hdrarm_control.arm_mode=="arm_sleep")
    {
        motor_1.pos_target = 0;
        motor_2.pos_target = 0;
        motor_3.pos_target = 0;
        motor_4.pos_target = 0;
        motor_5.pos_target = 0;
        motor_6.pos_target = 0;  
    }
    else if(hdrarm_control.arm_mode=="arm_control_demo")
    {
        //此模式下可以进行拖动示教
        if(hdrarm_control.drag_teachin=="false")
        {
            teach_txt.write_close();
            teach_txt.read_close();
            moveArmToStand();
        }
        else if(hdrarm_control.drag_teachin=="write")
        {
            //冗余设计，避免在fin时发出fout请求
            if(teachin_last_mode == "read")
            {
                teach_txt.read_close();
            }
            //尝试写入
            if(teach_txt.fout.is_open() == true)
            {
                teach_txt.write(motor_1.pos,motor_2.pos-MOTOR_2_OFFSET,motor_3.pos-MOTOR_3_OFFSET,motor_4.pos-MOTOR_4_OFFSET,motor_5.pos,motor_6.pos);
                ROS_INFO("teachin writing");
            }
            else
            {
                //尝试失败，打开写入权限
                teach_txt.read_close();
                teach_txt.write_init(hdrarm_control.drag_teachin_name);
                //如果传入的文件名不符合要求，则写入到默认地址
                if(teach_txt.fout.is_open() == false)
                {
                    teach_txt.write_init(TEACHIN_INIT_ADDRESS);
                    ROS_INFO("drag_teachin_name error!");
                }
                else
                {
                    ROS_INFO("drag_teachin write start!");
                }
            }
            motor_1.pos_target = 0;
            motor_2.pos_target = 0;
            motor_3.pos_target = 0;
            motor_4.pos_target = 0;
            motor_5.pos_target = 0;
            motor_6.pos_target = 0;
            //使其可以拖动
            motor_1.kp = 0;
            motor_2.kp = 0;
            motor_3.kp = 0;
            motor_4.kp = 0;
            motor_5.kp = 0;
            motor_6.kp = 0;
        }
        else if(hdrarm_control.drag_teachin=="read")
        {
            //冗余设计，避免在fout时发出fin请求
            if(teachin_last_mode == "write")
            {
                teach_txt.write_close();
            }
            //尝试读出
            if(teach_txt.fin.is_open() == true)
            {
                teach_txt.read();
                //ROS_INFO("%s\n",teach_txt.teach_read_buffer.c_str());
                if(teach_txt.teach_read_flag == true)
                {
                    ROS_INFO("waining! waining! waining! teachin working!");
                    //读出了有效数据，传给电机
                    motor_1.pos_target = teach_txt.teach_motor1_pos;
                    motor_2.pos_target = teach_txt.teach_motor2_pos;
                    motor_3.pos_target = teach_txt.teach_motor3_pos;
                    motor_4.pos_target = teach_txt.teach_motor4_pos;
                    motor_5.pos_target = teach_txt.teach_motor5_pos;
                    motor_6.pos_target = teach_txt.teach_motor6_pos;
                }
                else
                {
                    ROS_INFO("teachin reading finished");
                    //有效数据读取结束，本轮让电机锁定在原地
                    motor_1.pos_target = motor_1.pos;
                    motor_2.pos_target = motor_2.pos;
                    motor_3.pos_target = motor_3.pos;
                    motor_4.pos_target = motor_4.pos;
                    motor_5.pos_target = motor_5.pos;
                    motor_6.pos_target = motor_6.pos;
                    //接下来关闭文件再打开，实现重复读取
                    teach_txt.read_close();
                }
            }
            else
            {
                //读出失败，打开读出权限
                teach_txt.write_close();
                teach_txt.read_init(hdrarm_control.drag_teachin_name);
                //如果传入的文件名不符合要求，则写入到默认地址
                if(teach_txt.fin.is_open() == false)
                {
                    teach_txt.read_init(TEACHIN_INIT_ADDRESS);
                    ROS_INFO("drag_teachin_name error!");
                }
                else
                {
                    ROS_INFO("drag_teachin read start!");
                }
                motor_1.pos_target = 0;
                motor_2.pos_target = 0;
                motor_3.pos_target = 0;
                motor_4.pos_target = 0;
                motor_5.pos_target = 0;
                motor_6.pos_target = 0;
            }
        }
        //记录上一次拖动示教的状态
        teachin_last_mode = hdrarm_control.drag_teachin;
    }
    else if(hdrarm_control.arm_mode=="arm_control_moveit_fk")
    {
        motor_1.pos_target = motor1_gazebo_joints_position;
        motor_2.pos_target = motor2_gazebo_joints_position;
        motor_3.pos_target = motor3_gazebo_joints_position;
        motor_4.pos_target = motor4_gazebo_joints_position;
        motor_5.pos_target = motor5_gazebo_joints_position;
        motor_6.pos_target = motor6_gazebo_joints_position;


    //低通滤波平滑gazebo目标角度(可能需要给一下vel_target，但要注意与motor_energy_limit冲突)
    // motor_1.pos_target = motor_1.pos_target + 0.008*(motor1_gazebo_joints_position-motor_1.pos_target);
    // motor_2.pos_target = motor_2.pos_target + 0.008*(motor2_gazebo_joints_position-motor_2.pos_target);
    // motor_3.pos_target = motor_3.pos_target + 0.008*(motor3_gazebo_joints_position-motor_3.pos_target);
    // motor_4.pos_target = motor_4.pos_target + 0.008*(motor4_gazebo_joints_position-motor_4.pos_target);
    // motor_5.pos_target = motor_5.pos_target + 0.008*(motor5_gazebo_joints_position-motor_5.pos_target);
    // motor_6.pos_target = motor_6.pos_target + 0.008*(motor6_gazebo_joints_position-motor_6.pos_target);

    }
    else if(hdrarm_control.arm_mode=="arm_control_moveit_ik")
    {
        motor_1.pos_target = motor1_gazebo_joints_position;
        motor_2.pos_target = motor2_gazebo_joints_position;
        motor_3.pos_target = motor3_gazebo_joints_position;
        motor_4.pos_target = motor4_gazebo_joints_position;
        motor_5.pos_target = motor5_gazebo_joints_position;
        motor_6.pos_target = motor6_gazebo_joints_position;


    //低通滤波平滑gazebo目标角度(可能需要给一下vel_target，但要注意与motor_energy_limit冲突)
    // motor_1.pos_target = motor_1.pos_target + 0.008*(motor1_gazebo_joints_position-motor_1.pos_target);
    // motor_2.pos_target = motor_2.pos_target + 0.008*(motor2_gazebo_joints_position-motor_2.pos_target);
    // motor_3.pos_target = motor_3.pos_target + 0.008*(motor3_gazebo_joints_position-motor_3.pos_target);
    // motor_4.pos_target = motor_4.pos_target + 0.008*(motor4_gazebo_joints_position-motor_4.pos_target);
    // motor_5.pos_target = motor_5.pos_target + 0.008*(motor5_gazebo_joints_position-motor_5.pos_target);
    // motor_6.pos_target = motor_6.pos_target + 0.008*(motor6_gazebo_joints_position-motor_6.pos_target);

    }
    else
    {
        motor_1.pos_target = 0;
        motor_2.pos_target = 0;
        motor_3.pos_target = 0;
        motor_4.pos_target = 0;
        motor_5.pos_target = 0;
        motor_6.pos_target = 0; 
    }

    //如果希望的关节角度偏差较大，那么就需要做一个差补去追赶
    //如果motor_control_limit()好用就不需要了

}

//电机控制指令计算
void motor_control_calculator(void)
{
    //速度控制参数（不受算法影响，因此放在最前端）
    motor_1.kv = MOTOR_1_kv;
    motor_2.kv = MOTOR_2_kv;
    motor_3.kv = MOTOR_3_kv;
    motor_4.kv = MOTOR_4_kv;
    motor_5.kv = MOTOR_5_kv;
    motor_6.kv = MOTOR_6_kv;
    motor_1.vel_target = 0;
    motor_2.vel_target = 0;
    motor_3.vel_target = 0;
    motor_4.vel_target = 0;
    motor_5.vel_target = 0;
    motor_6.vel_target = 0;

    //重力补偿计算(此处赋重力补偿的t_tartget，也可以修改kp)
    gravity_compensation();

    //机械臂电机使能后的过渡状态，避免阶跃
    t_now = clock();
    float t_enable2now=((double)(t_now - t_enable_motor))/CLOCKS_PER_SEC;
    if(t_enable2now>=0.0 && t_enable2now<=0.1)//第一阶段，用0.1秒时间线性加入重力补偿
    {
        //这里是一种平滑策略，防止原本的k实际很小，在这里直接赋值的话会带来阶跃
        float gravity_compensation_k_param = (t_enable2now - 0.0)/(0.1 - 0.0);
        if(gravity_compensation_k < gravity_compensation_k_param)
        {
            gravity_compensation_k = gravity_compensation_k_param;
        }
        //给只有重力补偿的控制参数
        motor_1.kp = 0;
        motor_2.kp = 0;
        motor_3.kp = 0;
        motor_4.kp = 0;
        motor_5.kp = 0;
        motor_6.kp = 0;
        motor_1.pos_target = motor_1.pos;
        motor_2.pos_target = motor_2.pos;
        motor_3.pos_target = motor_3.pos;
        motor_4.pos_target = motor_4.pos;
        motor_5.pos_target = motor_5.pos;
        motor_6.pos_target = motor_6.pos;
        motor_1.t_target = 0;
        motor_2.t_target = gravity_compensation_k * motor_2.t_target;
        motor_3.t_target = gravity_compensation_k * motor_3.t_target;
        motor_4.t_target = gravity_compensation_k * motor_4.t_target;
        motor_5.t_target = 0;
        motor_6.t_target = 0;
        
        arm_mode_last = "arm_init_finish_1";
        zero_return_init = false;
    }
    else if(t_enable2now>0.1 && arm_mode_last=="arm_init_finish_1")//第二阶段，规划回零
    {
        if(!zero_return_init)
        {
            zero_start_pos[0] = motor_1.pos;
            zero_start_pos[1] = motor_2.pos;
            zero_start_pos[2] = motor_3.pos;
            zero_start_pos[3] = motor_4.pos;
            zero_start_pos[4] = motor_5.pos;
            zero_start_pos[5] = motor_6.pos;
            zero_return_init = true;
        }
        float progress = (t_enable2now-0.1)/ZERO_RETURN_TIME;
        if(progress > 1.0) progress = 1.0;
        motor_1.kp = MOTOR_1_kp;
        motor_2.kp = MOTOR_2_kp;
        motor_3.kp = MOTOR_3_kp;
        motor_4.kp = MOTOR_4_kp;
        motor_5.kp = MOTOR_5_kp;
        motor_6.kp = MOTOR_6_kp;
        motor_1.pos_target = zero_start_pos[0]*(1-progress);
        motor_2.pos_target = zero_start_pos[1]*(1-progress);
        motor_3.pos_target = zero_start_pos[2]*(1-progress);
        motor_4.pos_target = zero_start_pos[3]*(1-progress);
        motor_5.pos_target = zero_start_pos[4]*(1-progress);
        motor_6.pos_target = zero_start_pos[5]*(1-progress);
        if(progress>=1.0 || arm_zeroposition_check())
        {
            arm_mode_last = "arm_init_finish";
        }
    }
    else//第三阶段，正常控制
    {
        motor_1.kp = MOTOR_1_kp;
        motor_2.kp = MOTOR_2_kp;
        motor_3.kp = MOTOR_3_kp;
        motor_4.kp = MOTOR_4_kp;
        motor_5.kp = MOTOR_5_kp;
        motor_6.kp = MOTOR_6_kp;

        //状态机注释
        //若本次机械臂模式与arm_mode_last不同，有两种可能
        //1、机械臂刚经历了缓回零，但机械臂模式不在arm_sleep，此时检测位于零点后即可依据当前模式运动
        //2、机械臂已经在第三阶段正常工作了一段时间，需要切换状态，每次切换状态都希望回到零点后再开始
        //若本次机械臂模式与arm_mode_last相同，有三种可能
        //1、机械臂刚经历缓回零，同时机械臂模式处于arm_sleep，此时希望机械臂保持在零位
        //2、机械臂保持工作状态不变，此时希望连续控制

        if(arm_mode_last!="arm_init_finish" && hdrarm_control.arm_mode==arm_mode_last)
        {
            //希望连续控制状态（给出连续的pos_target，也可以修改kp)
            motor_control_continue();
        }
        else if(arm_mode_last=="arm_init_finish")
        {
            //刚经历了缓回零状态，检测当前在零点即可正常运动,否则就要重新缓回零
            if(abs(motor_1.pos)<0.3 && abs(motor_2.pos)<0.3 && abs(motor_3.pos)<0.3 && abs(motor_4.pos)<0.3 && abs(motor_5.pos)<0.3 && abs(motor_6.pos)<0.3)
            {
                //希望连续控制状态（给出连续的pos_target，也可以修改kp）
                motor_control_continue();
            }
            else
            {
                //重新刷新使能时间，开始重新回零
                t_enable_motor = clock();
            }
        }
        else
        {
            //正常工作一段时间后的切换状态，认为需要重新经过3s的缓回零使其归位
            t_enable_motor = clock();
        }

        //记录上一次运算的机械臂模式
        arm_mode_last = hdrarm_control.arm_mode;
    }

}


int main(int argc, char **argv)
{
    // ROS节点初始化
    ros::init(argc, argv, "motor_control");

    // 创建节点句柄
    ros::NodeHandle n;

    ros::AsyncSpinner spinner(1);
    spinner.start();
    arm.reset(new moveit::planning_interface::MoveGroupInterface("arm"));

    // 创建subscriber
    ros::Subscriber can1_rev = n.subscribe("/can1_rx", 500, can1_rx_Callback);
    ros::Subscriber armcontrol_rev = n.subscribe("/armcontrol_Info", 1, armcontrol_rx_Callback);
    ros::Subscriber joint_states_rev = n.subscribe("/joint_states", 500, gazebo_joint_states_Callback);

    // 创建Publisher
    ros::Publisher can1_pub = n.advertise<can_msgs::Frame>("/can1_tx", 1000);

    //覆盖原来的Ctrl+C中断函数，原来的只会调用ros::shutdown()
    signal(SIGINT, MySigintHandler);

    // 设置循环的频率（单位Hz）
    ros::Rate loop_rate(500);

    //采集一次时间
    t_disable_motor = clock();
    t_enable_motor = clock();

    //延时等待ROS启动
    ros::Duration(1).sleep();

    //失能所有电机，保证每次启始状态一致
    disable_all_motor();

    while (ros::ok())
    {
        //状态机
        if(hdrarm_control.motor_state == "disable" || hdrarm_control.Emergency_Stop == 1 || key_protect == 1)//安全保护放在第一位
        {
            disable_all_motor();
        }
        else
        {
            //通过t_enable_motor和t_disable_motor的大小（大代表时刻靠后）判定所属状态
            if(t_disable_motor>=t_enable_motor)//此刻处于电机失能状态，且开启了电机控制模式，发送一次电机使能指令
            {
                enable_all_motor();
            }
            else if(t_enable_motor>t_disable_motor && hdrarm_control.motor_state=="enable" && hdrarm_control.Emergency_Stop==0)//此时方为可控状态
            {
                //电机控制指令计算
                motor_control_calculator();

                //位置跟踪力矩限制(一般保护)
                motor_energy_limit(MOTOR_1_ENERGY_LIMIT,MOTOR_2_ENERGY_LIMIT,MOTOR_3_ENERGY_LIMIT,MOTOR_4_ENERGY_LIMIT,MOTOR_5_ENERGY_LIMIT,MOTOR_6_ENERGY_LIMIT);

                //电机极限角度限制(关键保护，需要进急停状态消除)
                motor_angle_limit(MOTOR_1_ANGLE_LIMIT,MOTOR_2_ANGLE_LIMIT,MOTOR_3_ANGLE_LIMIT,MOTOR_4_ANGLE_LIMIT,MOTOR_5_ANGLE_LIMIT,MOTOR_6_ANGLE_LIMIT);

                //发送正常可控状态下的控制信息
                motor_1.get_motor_ctrl_parameter();
                motor_2.get_motor_ctrl_parameter();
                motor_3.get_motor_ctrl_parameter();
                motor_4.get_motor_ctrl_parameter();
                motor_5.get_motor_ctrl_parameter();
                motor_6.get_motor_ctrl_parameter();
            }
            else//不应该进入此状态
            {
                disable_all_motor();
            }
        }

        //发送控制信息（所有状态都赋了待发送can数据）
        can1_pub.publish(motor_1.cansendata);
        can1_pub.publish(motor_2.cansendata);
        can1_pub.publish(motor_3.cansendata);
        can1_pub.publish(motor_4.cansendata);
        can1_pub.publish(motor_5.cansendata);
        can1_pub.publish(motor_6.cansendata);

        //ROS_INFO("data send success");
        
        // 循环等待回调函数
        ros::spinOnce();

        // 按照循环频率延时
        loop_rate.sleep();
    }

    return 0;
}
