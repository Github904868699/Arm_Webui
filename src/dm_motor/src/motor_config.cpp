#include "dm_motor/motor_config.h"

float MotorControlSet::Uint_to_float(int x_int, float x_min, float x_max, int bits)
{
    /// converts unsigned int to float, given range and number of bits ///
    float span = x_max - x_min;
    float offset = x_min;
    return ((float)x_int) * span / ((float)((1 << bits) - 1)) + offset;
}

uint16_t MotorControlSet::float_to_uint(float x, float x_min, float x_max, int bits)
{
    // Converts a float to an unsigned int, given range and number of bits ///
    float span = x_max - x_min;
    float offset = x_min;
    return (uint16_t)((x - offset) * ((float)((1 << bits) - 1)) / span);
}

void MotorControlSet::get_motor_ctrl_parameter(void)
{
    uint16_t pos_tmp, vel_tmp, kp_tmp, kd_tmp, tor_tmp;

    pos_tmp = float_to_uint(pos_target, P_MIN,  P_MAX,  16);
    vel_tmp = float_to_uint(vel_target, V_MIN,  V_MAX,  12);
    kp_tmp  = float_to_uint(kp,         KP_MIN, KP_MAX, 12);
    kd_tmp  = float_to_uint(kv,         KD_MIN, KD_MAX, 12);
    tor_tmp = float_to_uint(t_target,   T_MIN,  T_MAX,  12);

    cansendata.id = motor_id;
    cansendata.dlc = 8;
    cansendata.data[0] = (pos_tmp >> 8);
    cansendata.data[1] = (pos_tmp & 0xFF);
    cansendata.data[2] = ((vel_tmp >> 4) & 0xFF);
    cansendata.data[3] = ((((vel_tmp & 0xF) << 4) & 0xFF) | ((kp_tmp >> 8) & 0xFF));
    cansendata.data[4] = (kp_tmp & 0xFF);
    cansendata.data[5] = ((kd_tmp >> 4) & 0xFF);
    cansendata.data[6] = ((((kd_tmp & 0xF) << 4) & 0xFF) | ((tor_tmp >> 8) & 0xFF));
    cansendata.data[7] = (tor_tmp & 0xFF);

}

void MotorControlSet::motor_enable(void)
{
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
}

void MotorControlSet::motor_disable(void)
{
    cansendata.id = motor_id;
    cansendata.dlc = 8;
    cansendata.data[0] = 0xFF;
    cansendata.data[1] = 0xFF;
    cansendata.data[2] = 0xFF;
    cansendata.data[3] = 0xFF;
    cansendata.data[4] = 0xFF;
    cansendata.data[5] = 0xFF;
    cansendata.data[6] = 0xFF;
    cansendata.data[7] = 0xFD;
}

/**功能函数**/
