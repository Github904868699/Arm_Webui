;; Auto-generated. Do not edit!


(when (boundp 'armcontrol_demo_pkg::hdrarm_msg)
  (if (not (find-package "ARMCONTROL_DEMO_PKG"))
    (make-package "ARMCONTROL_DEMO_PKG"))
  (shadow 'hdrarm_msg (find-package "ARMCONTROL_DEMO_PKG")))
(unless (find-package "ARMCONTROL_DEMO_PKG::HDRARM_MSG")
  (make-package "ARMCONTROL_DEMO_PKG::HDRARM_MSG"))

(in-package "ROS")
;;//! \htmlinclude hdrarm_msg.msg.html


(defclass armcontrol_demo_pkg::hdrarm_msg
  :super ros::object
  :slots (_motor_state _arm_mode _Emergency_Stop _drag_teachin _drag_teachin_name _joint1_angle _joint2_angle _joint3_angle _joint4_angle _joint5_angle _joint6_angle _arm_position_x _arm_position_y _arm_position_z _arm_orientation_x _arm_orientation_y _arm_orientation_z _arm_orientation_w ))

(defmethod armcontrol_demo_pkg::hdrarm_msg
  (:init
   (&key
    ((:motor_state __motor_state) "")
    ((:arm_mode __arm_mode) "")
    ((:Emergency_Stop __Emergency_Stop) nil)
    ((:drag_teachin __drag_teachin) "")
    ((:drag_teachin_name __drag_teachin_name) "")
    ((:joint1_angle __joint1_angle) 0.0)
    ((:joint2_angle __joint2_angle) 0.0)
    ((:joint3_angle __joint3_angle) 0.0)
    ((:joint4_angle __joint4_angle) 0.0)
    ((:joint5_angle __joint5_angle) 0.0)
    ((:joint6_angle __joint6_angle) 0.0)
    ((:arm_position_x __arm_position_x) 0.0)
    ((:arm_position_y __arm_position_y) 0.0)
    ((:arm_position_z __arm_position_z) 0.0)
    ((:arm_orientation_x __arm_orientation_x) 0.0)
    ((:arm_orientation_y __arm_orientation_y) 0.0)
    ((:arm_orientation_z __arm_orientation_z) 0.0)
    ((:arm_orientation_w __arm_orientation_w) 0.0)
    )
   (send-super :init)
   (setq _motor_state (string __motor_state))
   (setq _arm_mode (string __arm_mode))
   (setq _Emergency_Stop __Emergency_Stop)
   (setq _drag_teachin (string __drag_teachin))
   (setq _drag_teachin_name (string __drag_teachin_name))
   (setq _joint1_angle (float __joint1_angle))
   (setq _joint2_angle (float __joint2_angle))
   (setq _joint3_angle (float __joint3_angle))
   (setq _joint4_angle (float __joint4_angle))
   (setq _joint5_angle (float __joint5_angle))
   (setq _joint6_angle (float __joint6_angle))
   (setq _arm_position_x (float __arm_position_x))
   (setq _arm_position_y (float __arm_position_y))
   (setq _arm_position_z (float __arm_position_z))
   (setq _arm_orientation_x (float __arm_orientation_x))
   (setq _arm_orientation_y (float __arm_orientation_y))
   (setq _arm_orientation_z (float __arm_orientation_z))
   (setq _arm_orientation_w (float __arm_orientation_w))
   self)
  (:motor_state
   (&optional __motor_state)
   (if __motor_state (setq _motor_state __motor_state)) _motor_state)
  (:arm_mode
   (&optional __arm_mode)
   (if __arm_mode (setq _arm_mode __arm_mode)) _arm_mode)
  (:Emergency_Stop
   (&optional (__Emergency_Stop :null))
   (if (not (eq __Emergency_Stop :null)) (setq _Emergency_Stop __Emergency_Stop)) _Emergency_Stop)
  (:drag_teachin
   (&optional __drag_teachin)
   (if __drag_teachin (setq _drag_teachin __drag_teachin)) _drag_teachin)
  (:drag_teachin_name
   (&optional __drag_teachin_name)
   (if __drag_teachin_name (setq _drag_teachin_name __drag_teachin_name)) _drag_teachin_name)
  (:joint1_angle
   (&optional __joint1_angle)
   (if __joint1_angle (setq _joint1_angle __joint1_angle)) _joint1_angle)
  (:joint2_angle
   (&optional __joint2_angle)
   (if __joint2_angle (setq _joint2_angle __joint2_angle)) _joint2_angle)
  (:joint3_angle
   (&optional __joint3_angle)
   (if __joint3_angle (setq _joint3_angle __joint3_angle)) _joint3_angle)
  (:joint4_angle
   (&optional __joint4_angle)
   (if __joint4_angle (setq _joint4_angle __joint4_angle)) _joint4_angle)
  (:joint5_angle
   (&optional __joint5_angle)
   (if __joint5_angle (setq _joint5_angle __joint5_angle)) _joint5_angle)
  (:joint6_angle
   (&optional __joint6_angle)
   (if __joint6_angle (setq _joint6_angle __joint6_angle)) _joint6_angle)
  (:arm_position_x
   (&optional __arm_position_x)
   (if __arm_position_x (setq _arm_position_x __arm_position_x)) _arm_position_x)
  (:arm_position_y
   (&optional __arm_position_y)
   (if __arm_position_y (setq _arm_position_y __arm_position_y)) _arm_position_y)
  (:arm_position_z
   (&optional __arm_position_z)
   (if __arm_position_z (setq _arm_position_z __arm_position_z)) _arm_position_z)
  (:arm_orientation_x
   (&optional __arm_orientation_x)
   (if __arm_orientation_x (setq _arm_orientation_x __arm_orientation_x)) _arm_orientation_x)
  (:arm_orientation_y
   (&optional __arm_orientation_y)
   (if __arm_orientation_y (setq _arm_orientation_y __arm_orientation_y)) _arm_orientation_y)
  (:arm_orientation_z
   (&optional __arm_orientation_z)
   (if __arm_orientation_z (setq _arm_orientation_z __arm_orientation_z)) _arm_orientation_z)
  (:arm_orientation_w
   (&optional __arm_orientation_w)
   (if __arm_orientation_w (setq _arm_orientation_w __arm_orientation_w)) _arm_orientation_w)
  (:serialization-length
   ()
   (+
    ;; string _motor_state
    4 (length _motor_state)
    ;; string _arm_mode
    4 (length _arm_mode)
    ;; bool _Emergency_Stop
    1
    ;; string _drag_teachin
    4 (length _drag_teachin)
    ;; string _drag_teachin_name
    4 (length _drag_teachin_name)
    ;; float64 _joint1_angle
    8
    ;; float64 _joint2_angle
    8
    ;; float64 _joint3_angle
    8
    ;; float64 _joint4_angle
    8
    ;; float64 _joint5_angle
    8
    ;; float64 _joint6_angle
    8
    ;; float64 _arm_position_x
    8
    ;; float64 _arm_position_y
    8
    ;; float64 _arm_position_z
    8
    ;; float64 _arm_orientation_x
    8
    ;; float64 _arm_orientation_y
    8
    ;; float64 _arm_orientation_z
    8
    ;; float64 _arm_orientation_w
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _motor_state
       (write-long (length _motor_state) s) (princ _motor_state s)
     ;; string _arm_mode
       (write-long (length _arm_mode) s) (princ _arm_mode s)
     ;; bool _Emergency_Stop
       (if _Emergency_Stop (write-byte -1 s) (write-byte 0 s))
     ;; string _drag_teachin
       (write-long (length _drag_teachin) s) (princ _drag_teachin s)
     ;; string _drag_teachin_name
       (write-long (length _drag_teachin_name) s) (princ _drag_teachin_name s)
     ;; float64 _joint1_angle
       (sys::poke _joint1_angle (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _joint2_angle
       (sys::poke _joint2_angle (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _joint3_angle
       (sys::poke _joint3_angle (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _joint4_angle
       (sys::poke _joint4_angle (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _joint5_angle
       (sys::poke _joint5_angle (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _joint6_angle
       (sys::poke _joint6_angle (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _arm_position_x
       (sys::poke _arm_position_x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _arm_position_y
       (sys::poke _arm_position_y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _arm_position_z
       (sys::poke _arm_position_z (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _arm_orientation_x
       (sys::poke _arm_orientation_x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _arm_orientation_y
       (sys::poke _arm_orientation_y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _arm_orientation_z
       (sys::poke _arm_orientation_z (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _arm_orientation_w
       (sys::poke _arm_orientation_w (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _motor_state
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _motor_state (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _arm_mode
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _arm_mode (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; bool _Emergency_Stop
     (setq _Emergency_Stop (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; string _drag_teachin
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _drag_teachin (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _drag_teachin_name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _drag_teachin_name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; float64 _joint1_angle
     (setq _joint1_angle (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _joint2_angle
     (setq _joint2_angle (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _joint3_angle
     (setq _joint3_angle (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _joint4_angle
     (setq _joint4_angle (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _joint5_angle
     (setq _joint5_angle (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _joint6_angle
     (setq _joint6_angle (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _arm_position_x
     (setq _arm_position_x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _arm_position_y
     (setq _arm_position_y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _arm_position_z
     (setq _arm_position_z (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _arm_orientation_x
     (setq _arm_orientation_x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _arm_orientation_y
     (setq _arm_orientation_y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _arm_orientation_z
     (setq _arm_orientation_z (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _arm_orientation_w
     (setq _arm_orientation_w (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get armcontrol_demo_pkg::hdrarm_msg :md5sum-) "5a62e58a22a17162b499a805b6b83bb9")
(setf (get armcontrol_demo_pkg::hdrarm_msg :datatype-) "armcontrol_demo_pkg/hdrarm_msg")
(setf (get armcontrol_demo_pkg::hdrarm_msg :definition-)
      "string motor_state      #电机状态   ps:enable/disable
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
")



(provide :armcontrol_demo_pkg/hdrarm_msg "5a62e58a22a17162b499a805b6b83bb9")


