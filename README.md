# This file currently only serves to mark the location of a catkin workspace for tool integration
ros 下机器人工作空间：roboarm3_ws： 中
文件夹（1）build和devel由编译生成
文件夹（2）logs为调试记录  
文件夹（3）src为机器人程序所在: 中
文件夹（一）003_moveit_config运动学求解配置
文件夹（二）dm_motor 下发关节指令数据以及接收规划指令数据
文件夹（三）robot_arm：机器人结构参数
文件夹（四）armcontrol_demo_pkg：机器人控制界面
终端运行指令：
roscore  //说明ros安装成功；ros启动
#在工作空间内右键选择打开终端
#配置文件
source ./devel/setup.bash  //调用ros 
#编译环境
catkin build                        
roslaunch 003_moveit_config combined_bringup.launch       //运行通信节点，仿真环境，UI界面
roslaunch 003_moveit_config 003_bringup_moveit.launch     //运行仿真环境
roslaunch armcontrol_demo_pkg armcontrol_demo.launch      // 运行UI界面

#查询串口设备，这里的*有可能是0、1、2...
ls /dev/ttyACM*

#将串口映射为can1，并设置波特率为1M
sudo slcand -o -c -s8 /dev/ttyACM* can1        //这里的*填的数字要和上面的一致
#启用can
sudo ifconfig can1 up
sudo ifconfig can1 txqueuelen 1000          //配置txqueuelen的传输数据缓冲区的存储长度

roslaunch dm_motor dm_motor.launch                             //运行通信节点

视觉
#插入摄像头，查看摄像头是否连接成功
ls /dev/video*
#如果识别到了我们需要的video2就可以继续
cd ~/roboarm3_ws/
source ./devel/setup.bash

#可编译可不编译
#catkin build

#打开摄像头画面监看
roslaunch usb_cam usb_cam-test.launch
#发布识别信息
roslaunch apriltag_ros continuous_detection.launch

#也可以通过rostopic监看话题
source ./devel/setup.bash
rostopic echo -c /tag_detections




#案例演示

#在机器人工作空间内打开终端
source ./devel/setup.bash  
cd ./src/003_moveit_config/scripts/mycode/demo1


#在第一个终端下启动继电器通信节点（要注意继电器串行端口并不一定每次都是ttyCH341USB0）
sudo chmod a+rw /dev/ttyCH341USB0     //权限不够无法访问时，修改串行设备端口权限
python3 jdq_subscriber.py 

#第二个终端

#流水线搬运编码示例
python3 demo1.py

# 打磨机打磨示例
python3 demo2.py

# 不断上料搬运示例
python3 demo3.py

#打螺丝示例
python3 demo4.py

#立体仓库填充示例
python3 demo5.py

#形状识别示例
python3 demo6.py

#颜色识别示例
python3 demo7.py

#流水线搬运编码示例2
python3 demo8.py

#二维码追踪示例
#需开启两个终端
python3 moveit_ik_demo_vision.py
python3 positions_publisher.py   （摄像头和发布识别的launch文件记得都打开）

#3d视觉抓取任务：
#需开启两个终端
在003_moveit_config/scripts/mycode/camera目录下
python3 catch.py
在yolov5-master目录下
conda env list                  //查看虚拟空间
conda activate vision           //进入虚拟空间
python3 detect.py               //要在该空间下才能运行该文件
系统将会循环运行以下功能：
1.拍照并保存。
2.对图片进行识别定位，若识别成功则计算物体坐标，并进行下一步。否则返回第一步
3.进行机械臂动作规划，抓取物体

