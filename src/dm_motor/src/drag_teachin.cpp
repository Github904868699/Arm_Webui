/**
 * 重力补偿、拖动示教功能库
 */
#include "dm_motor/drag_teachin.h"
#include <string>

void DragTeachInSet::write_init(string address_name)
{
    //打开或创建存储文件
    if(fout.is_open()==false)
    {
        fout.open(address_name);
    }    
}

void DragTeachInSet::write(float motor1_pos, float motor2_pos, float motor3_pos, float motor4_pos, float motor5_pos, float motor6_pos)
{
    fout << "data " << to_string(motor1_pos) << " " << to_string(motor2_pos) << " " << to_string(motor3_pos) << " " << to_string(motor4_pos) << " " << to_string(motor5_pos) <<  " " << to_string(motor6_pos) << endl;
}

void DragTeachInSet::write_close(void)
{
    if(fout.is_open()==true)
    {
        fout.close();
    }
}

void DragTeachInSet::read_init(string address_name)
{
    //打开存储文件
    if(fin.is_open()==false)
    {
        fin.open(address_name);
    }
}

void DragTeachInSet::read(void)
{
    getline(fin,teach_read_buffer);
    
    //定义字符串处理
    istringstream read_buffer(teach_read_buffer);
    string out;
    //判断数据头部数据
    read_buffer >> out;
    if(out == "data")
    {
        teach_read_flag = true;
        //正常数据归档
        read_buffer >> out;
        teach_motor1_pos = stof(out);
        read_buffer >> out;
        teach_motor2_pos = stof(out);
        read_buffer >> out;
        teach_motor3_pos = stof(out);
        read_buffer >> out;
        teach_motor4_pos = stof(out);
        read_buffer >> out;
        teach_motor5_pos = stof(out);
        read_buffer >> out;
        teach_motor6_pos = stof(out);

        // ROS_INFO("%f",teach_motor1_pos);
        // ROS_INFO("%f",teach_motor2_pos);
        // ROS_INFO("%f",teach_motor3_pos);
        // ROS_INFO("%f",teach_motor4_pos);
        // ROS_INFO("%f",teach_motor5_pos);
        // ROS_INFO("%f",teach_motor6_pos);

    }
    else
    {
        teach_read_flag = false;
    }
}

void DragTeachInSet::read_close(void)
{
    if(fin.is_open()==true)
    {
        fin.close();
    }
}