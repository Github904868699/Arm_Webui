string motor_state      #电机状态   ps:enable/disable
string arm_mode		    #机械臂模式	ps:arm_sleep/arm_control_demo/arm_control_moveit_fk/arm_control_moveit_ik
bool Emergency_Stop     #急停
string drag_teachin     #拖动示教   ps:false/write/read
string drag_teachin_name#拖动示教存储文件名
float64 joint1_angle    #moveit正解使用
float64 joint2_angle    #moveit正解使用
float64 joint3_angle    #moveit正解使用
float64 joint4_angle    #moveit正解使用
float64 joint5_angle    #moveit正解使用
float64 joint6_angle    #moveit正解使用
float64 arm_position_x		#moveit逆解使用
float64 arm_position_y		#moveit逆解使用
float64 arm_position_z		#moveit逆解使用
float64 arm_orientation_x	#moveit逆解使用
float64 arm_orientation_y	#moveit逆解使用
float64 arm_orientation_z	#moveit逆解使用
float64 arm_orientation_w	#moveit逆解使用