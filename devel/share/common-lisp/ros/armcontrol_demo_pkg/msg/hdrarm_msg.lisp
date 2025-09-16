; Auto-generated. Do not edit!


(cl:in-package armcontrol_demo_pkg-msg)


;//! \htmlinclude hdrarm_msg.msg.html

(cl:defclass <hdrarm_msg> (roslisp-msg-protocol:ros-message)
  ((motor_state
    :reader motor_state
    :initarg :motor_state
    :type cl:string
    :initform "")
   (arm_mode
    :reader arm_mode
    :initarg :arm_mode
    :type cl:string
    :initform "")
   (Emergency_Stop
    :reader Emergency_Stop
    :initarg :Emergency_Stop
    :type cl:boolean
    :initform cl:nil)
   (drag_teachin
    :reader drag_teachin
    :initarg :drag_teachin
    :type cl:string
    :initform "")
   (drag_teachin_name
    :reader drag_teachin_name
    :initarg :drag_teachin_name
    :type cl:string
    :initform "")
   (joint1_angle
    :reader joint1_angle
    :initarg :joint1_angle
    :type cl:float
    :initform 0.0)
   (joint2_angle
    :reader joint2_angle
    :initarg :joint2_angle
    :type cl:float
    :initform 0.0)
   (joint3_angle
    :reader joint3_angle
    :initarg :joint3_angle
    :type cl:float
    :initform 0.0)
   (joint4_angle
    :reader joint4_angle
    :initarg :joint4_angle
    :type cl:float
    :initform 0.0)
   (joint5_angle
    :reader joint5_angle
    :initarg :joint5_angle
    :type cl:float
    :initform 0.0)
   (joint6_angle
    :reader joint6_angle
    :initarg :joint6_angle
    :type cl:float
    :initform 0.0)
   (arm_position_x
    :reader arm_position_x
    :initarg :arm_position_x
    :type cl:float
    :initform 0.0)
   (arm_position_y
    :reader arm_position_y
    :initarg :arm_position_y
    :type cl:float
    :initform 0.0)
   (arm_position_z
    :reader arm_position_z
    :initarg :arm_position_z
    :type cl:float
    :initform 0.0)
   (arm_orientation_x
    :reader arm_orientation_x
    :initarg :arm_orientation_x
    :type cl:float
    :initform 0.0)
   (arm_orientation_y
    :reader arm_orientation_y
    :initarg :arm_orientation_y
    :type cl:float
    :initform 0.0)
   (arm_orientation_z
    :reader arm_orientation_z
    :initarg :arm_orientation_z
    :type cl:float
    :initform 0.0)
   (arm_orientation_w
    :reader arm_orientation_w
    :initarg :arm_orientation_w
    :type cl:float
    :initform 0.0))
)

(cl:defclass hdrarm_msg (<hdrarm_msg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <hdrarm_msg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'hdrarm_msg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name armcontrol_demo_pkg-msg:<hdrarm_msg> is deprecated: use armcontrol_demo_pkg-msg:hdrarm_msg instead.")))

(cl:ensure-generic-function 'motor_state-val :lambda-list '(m))
(cl:defmethod motor_state-val ((m <hdrarm_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader armcontrol_demo_pkg-msg:motor_state-val is deprecated.  Use armcontrol_demo_pkg-msg:motor_state instead.")
  (motor_state m))

(cl:ensure-generic-function 'arm_mode-val :lambda-list '(m))
(cl:defmethod arm_mode-val ((m <hdrarm_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader armcontrol_demo_pkg-msg:arm_mode-val is deprecated.  Use armcontrol_demo_pkg-msg:arm_mode instead.")
  (arm_mode m))

(cl:ensure-generic-function 'Emergency_Stop-val :lambda-list '(m))
(cl:defmethod Emergency_Stop-val ((m <hdrarm_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader armcontrol_demo_pkg-msg:Emergency_Stop-val is deprecated.  Use armcontrol_demo_pkg-msg:Emergency_Stop instead.")
  (Emergency_Stop m))

(cl:ensure-generic-function 'drag_teachin-val :lambda-list '(m))
(cl:defmethod drag_teachin-val ((m <hdrarm_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader armcontrol_demo_pkg-msg:drag_teachin-val is deprecated.  Use armcontrol_demo_pkg-msg:drag_teachin instead.")
  (drag_teachin m))

(cl:ensure-generic-function 'drag_teachin_name-val :lambda-list '(m))
(cl:defmethod drag_teachin_name-val ((m <hdrarm_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader armcontrol_demo_pkg-msg:drag_teachin_name-val is deprecated.  Use armcontrol_demo_pkg-msg:drag_teachin_name instead.")
  (drag_teachin_name m))

(cl:ensure-generic-function 'joint1_angle-val :lambda-list '(m))
(cl:defmethod joint1_angle-val ((m <hdrarm_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader armcontrol_demo_pkg-msg:joint1_angle-val is deprecated.  Use armcontrol_demo_pkg-msg:joint1_angle instead.")
  (joint1_angle m))

(cl:ensure-generic-function 'joint2_angle-val :lambda-list '(m))
(cl:defmethod joint2_angle-val ((m <hdrarm_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader armcontrol_demo_pkg-msg:joint2_angle-val is deprecated.  Use armcontrol_demo_pkg-msg:joint2_angle instead.")
  (joint2_angle m))

(cl:ensure-generic-function 'joint3_angle-val :lambda-list '(m))
(cl:defmethod joint3_angle-val ((m <hdrarm_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader armcontrol_demo_pkg-msg:joint3_angle-val is deprecated.  Use armcontrol_demo_pkg-msg:joint3_angle instead.")
  (joint3_angle m))

(cl:ensure-generic-function 'joint4_angle-val :lambda-list '(m))
(cl:defmethod joint4_angle-val ((m <hdrarm_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader armcontrol_demo_pkg-msg:joint4_angle-val is deprecated.  Use armcontrol_demo_pkg-msg:joint4_angle instead.")
  (joint4_angle m))

(cl:ensure-generic-function 'joint5_angle-val :lambda-list '(m))
(cl:defmethod joint5_angle-val ((m <hdrarm_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader armcontrol_demo_pkg-msg:joint5_angle-val is deprecated.  Use armcontrol_demo_pkg-msg:joint5_angle instead.")
  (joint5_angle m))

(cl:ensure-generic-function 'joint6_angle-val :lambda-list '(m))
(cl:defmethod joint6_angle-val ((m <hdrarm_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader armcontrol_demo_pkg-msg:joint6_angle-val is deprecated.  Use armcontrol_demo_pkg-msg:joint6_angle instead.")
  (joint6_angle m))

(cl:ensure-generic-function 'arm_position_x-val :lambda-list '(m))
(cl:defmethod arm_position_x-val ((m <hdrarm_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader armcontrol_demo_pkg-msg:arm_position_x-val is deprecated.  Use armcontrol_demo_pkg-msg:arm_position_x instead.")
  (arm_position_x m))

(cl:ensure-generic-function 'arm_position_y-val :lambda-list '(m))
(cl:defmethod arm_position_y-val ((m <hdrarm_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader armcontrol_demo_pkg-msg:arm_position_y-val is deprecated.  Use armcontrol_demo_pkg-msg:arm_position_y instead.")
  (arm_position_y m))

(cl:ensure-generic-function 'arm_position_z-val :lambda-list '(m))
(cl:defmethod arm_position_z-val ((m <hdrarm_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader armcontrol_demo_pkg-msg:arm_position_z-val is deprecated.  Use armcontrol_demo_pkg-msg:arm_position_z instead.")
  (arm_position_z m))

(cl:ensure-generic-function 'arm_orientation_x-val :lambda-list '(m))
(cl:defmethod arm_orientation_x-val ((m <hdrarm_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader armcontrol_demo_pkg-msg:arm_orientation_x-val is deprecated.  Use armcontrol_demo_pkg-msg:arm_orientation_x instead.")
  (arm_orientation_x m))

(cl:ensure-generic-function 'arm_orientation_y-val :lambda-list '(m))
(cl:defmethod arm_orientation_y-val ((m <hdrarm_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader armcontrol_demo_pkg-msg:arm_orientation_y-val is deprecated.  Use armcontrol_demo_pkg-msg:arm_orientation_y instead.")
  (arm_orientation_y m))

(cl:ensure-generic-function 'arm_orientation_z-val :lambda-list '(m))
(cl:defmethod arm_orientation_z-val ((m <hdrarm_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader armcontrol_demo_pkg-msg:arm_orientation_z-val is deprecated.  Use armcontrol_demo_pkg-msg:arm_orientation_z instead.")
  (arm_orientation_z m))

(cl:ensure-generic-function 'arm_orientation_w-val :lambda-list '(m))
(cl:defmethod arm_orientation_w-val ((m <hdrarm_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader armcontrol_demo_pkg-msg:arm_orientation_w-val is deprecated.  Use armcontrol_demo_pkg-msg:arm_orientation_w instead.")
  (arm_orientation_w m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <hdrarm_msg>) ostream)
  "Serializes a message object of type '<hdrarm_msg>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'motor_state))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'motor_state))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'arm_mode))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'arm_mode))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'Emergency_Stop) 1 0)) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'drag_teachin))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'drag_teachin))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'drag_teachin_name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'drag_teachin_name))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'joint1_angle))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'joint2_angle))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'joint3_angle))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'joint4_angle))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'joint5_angle))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'joint6_angle))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'arm_position_x))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'arm_position_y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'arm_position_z))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'arm_orientation_x))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'arm_orientation_y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'arm_orientation_z))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'arm_orientation_w))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <hdrarm_msg>) istream)
  "Deserializes a message object of type '<hdrarm_msg>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'motor_state) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'motor_state) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'arm_mode) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'arm_mode) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:setf (cl:slot-value msg 'Emergency_Stop) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'drag_teachin) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'drag_teachin) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'drag_teachin_name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'drag_teachin_name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'joint1_angle) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'joint2_angle) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'joint3_angle) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'joint4_angle) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'joint5_angle) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'joint6_angle) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'arm_position_x) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'arm_position_y) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'arm_position_z) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'arm_orientation_x) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'arm_orientation_y) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'arm_orientation_z) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'arm_orientation_w) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<hdrarm_msg>)))
  "Returns string type for a message object of type '<hdrarm_msg>"
  "armcontrol_demo_pkg/hdrarm_msg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'hdrarm_msg)))
  "Returns string type for a message object of type 'hdrarm_msg"
  "armcontrol_demo_pkg/hdrarm_msg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<hdrarm_msg>)))
  "Returns md5sum for a message object of type '<hdrarm_msg>"
  "5a62e58a22a17162b499a805b6b83bb9")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'hdrarm_msg)))
  "Returns md5sum for a message object of type 'hdrarm_msg"
  "5a62e58a22a17162b499a805b6b83bb9")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<hdrarm_msg>)))
  "Returns full string definition for message of type '<hdrarm_msg>"
  (cl:format cl:nil "string motor_state      #电机状态   ps:enable/disable~%string arm_mode		    #机械臂模式	ps:arm_sleep/arm_control_demo/arm_control_moveit_fk/arm_control_moveit_ik~%bool Emergency_Stop     #急停~%string drag_teachin     #拖动示教   ps:false/write/read~%string drag_teachin_name#拖动示教存储文件名~%float64 joint1_angle    #moveit正解使用~%float64 joint2_angle    #moveit正解使用~%float64 joint3_angle    #moveit正解使用~%float64 joint4_angle    #moveit正解使用~%float64 joint5_angle    #moveit正解使用~%float64 joint6_angle    #moveit正解使用~%float64 arm_position_x		#moveit逆解使用~%float64 arm_position_y		#moveit逆解使用~%float64 arm_position_z		#moveit逆解使用~%float64 arm_orientation_x	#moveit逆解使用~%float64 arm_orientation_y	#moveit逆解使用~%float64 arm_orientation_z	#moveit逆解使用~%float64 arm_orientation_w	#moveit逆解使用~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'hdrarm_msg)))
  "Returns full string definition for message of type 'hdrarm_msg"
  (cl:format cl:nil "string motor_state      #电机状态   ps:enable/disable~%string arm_mode		    #机械臂模式	ps:arm_sleep/arm_control_demo/arm_control_moveit_fk/arm_control_moveit_ik~%bool Emergency_Stop     #急停~%string drag_teachin     #拖动示教   ps:false/write/read~%string drag_teachin_name#拖动示教存储文件名~%float64 joint1_angle    #moveit正解使用~%float64 joint2_angle    #moveit正解使用~%float64 joint3_angle    #moveit正解使用~%float64 joint4_angle    #moveit正解使用~%float64 joint5_angle    #moveit正解使用~%float64 joint6_angle    #moveit正解使用~%float64 arm_position_x		#moveit逆解使用~%float64 arm_position_y		#moveit逆解使用~%float64 arm_position_z		#moveit逆解使用~%float64 arm_orientation_x	#moveit逆解使用~%float64 arm_orientation_y	#moveit逆解使用~%float64 arm_orientation_z	#moveit逆解使用~%float64 arm_orientation_w	#moveit逆解使用~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <hdrarm_msg>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'motor_state))
     4 (cl:length (cl:slot-value msg 'arm_mode))
     1
     4 (cl:length (cl:slot-value msg 'drag_teachin))
     4 (cl:length (cl:slot-value msg 'drag_teachin_name))
     8
     8
     8
     8
     8
     8
     8
     8
     8
     8
     8
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <hdrarm_msg>))
  "Converts a ROS message object to a list"
  (cl:list 'hdrarm_msg
    (cl:cons ':motor_state (motor_state msg))
    (cl:cons ':arm_mode (arm_mode msg))
    (cl:cons ':Emergency_Stop (Emergency_Stop msg))
    (cl:cons ':drag_teachin (drag_teachin msg))
    (cl:cons ':drag_teachin_name (drag_teachin_name msg))
    (cl:cons ':joint1_angle (joint1_angle msg))
    (cl:cons ':joint2_angle (joint2_angle msg))
    (cl:cons ':joint3_angle (joint3_angle msg))
    (cl:cons ':joint4_angle (joint4_angle msg))
    (cl:cons ':joint5_angle (joint5_angle msg))
    (cl:cons ':joint6_angle (joint6_angle msg))
    (cl:cons ':arm_position_x (arm_position_x msg))
    (cl:cons ':arm_position_y (arm_position_y msg))
    (cl:cons ':arm_position_z (arm_position_z msg))
    (cl:cons ':arm_orientation_x (arm_orientation_x msg))
    (cl:cons ':arm_orientation_y (arm_orientation_y msg))
    (cl:cons ':arm_orientation_z (arm_orientation_z msg))
    (cl:cons ':arm_orientation_w (arm_orientation_w msg))
))
