#ifndef _DRAG_TEACHIN_
#define _DRAG_TEACHIN_

#include <string>
#include <fstream>
#include <iostream>
#include "stdint.h"
#include "dm_motor/motor_config.h"

using namespace std;

//每次部署都需要将此文件夹设定为拖动数据默认存储位置
string TEACHIN_INIT_ADDRESS = "/home/arm003/roboarm_ws/src/dm_motor/txt/drag_teachin_1.txt";

class DragTeachInSet
{
    public:
        //创建文件对象
        ifstream fin;
        ofstream fout;

        //读取数据
        string teach_read_buffer;
        bool  teach_read_flag = 0;
        float teach_motor1_pos = 0.0;
        float teach_motor2_pos = 0.0;
        float teach_motor3_pos = 0.0;
        float teach_motor4_pos = 0.0;
        float teach_motor5_pos = 0.0;
        float teach_motor6_pos = 0.0;

        //功能函数（写拖动示教文件）
        void write_init(string address_name);
        void write(float motor1_pos, float motor2_pos, float motor3_pos, float motor4_pos, float motor5_pos, float motor6_pos);
        void write_close(void);
        

        //功能函数（读拖动示教文件）
        void read_init(string address_name);
        void read(void);
        void read_close(void);

        //构造函数
        DragTeachInSet(void)
        {
            //记录文件地址及名称
            //address_name = address_name_w;
        }

};




#endif
