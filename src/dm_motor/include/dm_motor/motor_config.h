#ifndef _MOTOR_CONFIG_H_
#define _MOTOR_CONFIG_H_

#include <iostream>
#include "stdint.h"
#include "can_msgs/Frame.h"

using namespace std;

//DM电机 MIT控制协议限幅参数
#define KP_MAX 500
#define KP_MIN 0
#define KD_MAX 5
#define KD_MIN 0

//DM4310电机
#define DM4310_P_MAX  12.5
#define DM4310_P_MIN -12.5
#define DM4310_V_MAX  30.0
#define DM4310_V_MIN -30.0
#define DM4310_T_MAX  10.0
#define DM4310_T_MIN -10.0

//DM4340电机
#define DM4340_P_MAX  12.5
#define DM4340_P_MIN -12.5
#define DM4340_V_MAX  10.0
#define DM4340_V_MIN -10.0
#define DM4340_T_MAX  28.0
#define DM4340_T_MIN -28.0

//DM6006电机
#define DM6006_P_MAX  12.5
#define DM6006_P_MIN -12.5
#define DM6006_V_MAX  45.0
#define DM6006_V_MIN -45.0
#define DM6006_T_MAX  12.0
#define DM6006_T_MIN -12.0

//DM8006电机
#define DM8006_P_MAX  12.5
#define DM8006_P_MIN -12.5
#define DM8006_V_MAX  25.0
#define DM8006_V_MIN -25.0
#define DM8006_T_MAX  20.0
#define DM8006_T_MIN -20.0

//关节电机ID
#define MOTOR_1 0x01
#define MOTOR_2 0x02
#define MOTOR_3 0x03
#define MOTOR_4 0x04
#define MOTOR_5 0x05
#define MOTOR_6 0x06

//使能标志位
#define MOTOR_ENABLED 16

//关节偏置矫正系数
//ps:数学模型上的零位是竖直向上姿态
//ps:电机标定的零位是卧式姿态
#define MOTOR_2_OFFSET 0
#define MOTOR_3_OFFSET 0
#define MOTOR_4_OFFSET 0

//电机控制参数
#define MOTOR_1_kp 200
#define MOTOR_2_kp 280
#define MOTOR_3_kp 220
#define MOTOR_4_kp 50
#define MOTOR_5_kp 50
#define MOTOR_6_kp 10


#define MOTOR_1_kv 1.2
#define MOTOR_2_kv 1.8
#define MOTOR_3_kv 1.4
#define MOTOR_4_kv 0.4
#define MOTOR_5_kv 0.2
#define MOTOR_6_kv 0.1

//时间参数
#define ZERO_RETURN_TIME 1.2

//位置跟踪力矩限制
#define MOTOR_1_ENERGY_LIMIT 8
#define MOTOR_2_ENERGY_LIMIT 8
#define MOTOR_3_ENERGY_LIMIT 7
#define MOTOR_4_ENERGY_LIMIT 6
#define MOTOR_5_ENERGY_LIMIT 5
#define MOTOR_6_ENERGY_LIMIT 4

//电机转动角度限制
#define MOTOR_1_ANGLE_LIMIT 3.14
#define MOTOR_2_ANGLE_LIMIT 1.67
#define MOTOR_3_ANGLE_LIMIT 3.14
#define MOTOR_4_ANGLE_LIMIT 3.14
#define MOTOR_5_ANGLE_LIMIT 3.14
#define MOTOR_6_ANGLE_LIMIT 3.14

class MotorControlSet
{
    public:
        //电机属性
        uint8_t motor_id;
        string  motor_type;

        //电机属性参数
        float P_MAX;
        float P_MIN;
        float V_MAX;
        float V_MIN;
        float T_MAX;
        float T_MIN;

        //电机发送信息
        float pos_target = 0.0;
        float vel_target = 0.0;
        float kp = 0.0;
        float kv = 0.1;
        float t_target = 0.0;
        can_msgs::Frame cansendata;

        //电机反馈数据
        float pos;
        float vel;
        float t;

        //功能函数
        float Uint_to_float(int x_int, float x_min, float x_max, int bits);
        uint16_t float_to_uint(float x, float x_min, float x_max, int bits);
        void get_motor_ctrl_parameter(void);
        void motor_enable(void);
        void motor_disable(void);

        //构造函数
        MotorControlSet(uint8_t id,string type)
        {
            //反馈参数初始化
            pos = 0;
            vel = 0;
            t   = 0;

            //电机信息初始化
            motor_id = id;
            motor_type = type;

            //电机发送信息初始化
            cansendata.id = motor_id;
            cansendata.dlc = 8;
            cansendata.data[0] = 0xFF;
            cansendata.data[1] = 0xFF;
            cansendata.data[2] = 0xFF;
            cansendata.data[3] = 0xFF;
            cansendata.data[4] = 0xFF;
            cansendata.data[5] = 0xFF;
            cansendata.data[6] = 0xFF;
            cansendata.data[7] = 0xFC;

            //依据电机种类，赋不同的MIT控制限幅值
            if (!motor_type.compare("DM4310"))
            {
                P_MAX = DM4310_P_MAX;
                P_MIN = DM4310_P_MIN;
                V_MAX = DM4310_V_MAX;
                V_MIN = DM4310_V_MIN;
                T_MAX = DM4310_T_MAX;
                T_MIN = DM4310_T_MIN;
            }
            else if (!motor_type.compare("DM4340"))
            {
                P_MAX = DM4340_P_MAX;
                P_MIN = DM4340_P_MIN;
                V_MAX = DM4340_V_MAX;
                V_MIN = DM4340_V_MIN;
                T_MAX = DM4340_T_MAX;
                T_MIN = DM4340_T_MIN;
            }            else if (!motor_type.compare("DM6006"))
            {
                P_MAX = DM6006_P_MAX;
                P_MIN = DM6006_P_MIN;
                V_MAX = DM6006_V_MAX;
                V_MIN = DM6006_V_MIN;
                T_MAX = DM6006_T_MAX;
                T_MIN = DM6006_T_MIN;
            }
            else if (!motor_type.compare("DM8006"))
            {
                P_MAX = DM8006_P_MAX;
                P_MIN = DM8006_P_MIN;
                V_MAX = DM8006_V_MAX;
                V_MIN = DM8006_V_MIN;
                T_MAX = DM8006_T_MAX;
                T_MIN = DM8006_T_MIN;
            }
            else
            {
                P_MAX = 0;
                P_MIN = 0;
                V_MAX = 0;
                V_MIN = 0;
                T_MAX = 0;
                T_MIN = 0;
            }
        }

        //析构函数
        ~MotorControlSet(){

        }
};



class HdrarmControlSet
{
    public:
        //传递的控制参数
        string motor_state;
        string arm_mode;
        bool Emergency_Stop;
        string drag_teachin;
        string drag_teachin_name;
        float joint1_angle;
        float joint2_angle;
        float joint3_angle;
        float joint4_angle;
        float joint5_angle;
        float joint6_angle;
        float arm_position_x;
        float arm_position_y;
        float arm_position_z;
        float arm_orientation_x;
        float arm_orientation_y;
        float arm_orientation_z;
        float arm_orientation_w;


        //构造函数
        HdrarmControlSet()
        {
            motor_state = "disable";
            arm_mode = "arm_sleep";
            Emergency_Stop = 0;
            drag_teachin = "false";
            drag_teachin_name = "drag_teachin_1.txt";

            joint1_angle = 0.0;
            joint2_angle = 0.0;
            joint3_angle = 0.0;
            joint4_angle = 0.0;
            joint5_angle = 0.0;
            joint6_angle = 0.0;

            arm_position_x = 0.15;
            arm_position_y = 0.0;
            arm_position_z = 0.3;
            arm_orientation_x = 0.0;
            arm_orientation_y = 0.0;
            arm_orientation_z = 0.707;
            arm_orientation_w = 0.707;
        }
        //析构函数
        ~HdrarmControlSet(){

        }
};

//功能函数

#endif
