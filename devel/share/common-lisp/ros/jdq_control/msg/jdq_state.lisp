; Auto-generated. Do not edit!


(cl:in-package jdq_control-msg)


;//! \htmlinclude jdq_state.msg.html

(cl:defclass <jdq_state> (roslisp-msg-protocol:ros-message)
  ((USB1
    :reader USB1
    :initarg :USB1
    :type cl:string
    :initform "")
   (USB2
    :reader USB2
    :initarg :USB2
    :type cl:string
    :initform "")
   (USB3
    :reader USB3
    :initarg :USB3
    :type cl:string
    :initform "")
   (USB4
    :reader USB4
    :initarg :USB4
    :type cl:string
    :initform "")
   (USB5
    :reader USB5
    :initarg :USB5
    :type cl:string
    :initform "")
   (USB6
    :reader USB6
    :initarg :USB6
    :type cl:string
    :initform "")
   (USB7
    :reader USB7
    :initarg :USB7
    :type cl:string
    :initform "")
   (USB8
    :reader USB8
    :initarg :USB8
    :type cl:string
    :initform ""))
)

(cl:defclass jdq_state (<jdq_state>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <jdq_state>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'jdq_state)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name jdq_control-msg:<jdq_state> is deprecated: use jdq_control-msg:jdq_state instead.")))

(cl:ensure-generic-function 'USB1-val :lambda-list '(m))
(cl:defmethod USB1-val ((m <jdq_state>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader jdq_control-msg:USB1-val is deprecated.  Use jdq_control-msg:USB1 instead.")
  (USB1 m))

(cl:ensure-generic-function 'USB2-val :lambda-list '(m))
(cl:defmethod USB2-val ((m <jdq_state>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader jdq_control-msg:USB2-val is deprecated.  Use jdq_control-msg:USB2 instead.")
  (USB2 m))

(cl:ensure-generic-function 'USB3-val :lambda-list '(m))
(cl:defmethod USB3-val ((m <jdq_state>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader jdq_control-msg:USB3-val is deprecated.  Use jdq_control-msg:USB3 instead.")
  (USB3 m))

(cl:ensure-generic-function 'USB4-val :lambda-list '(m))
(cl:defmethod USB4-val ((m <jdq_state>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader jdq_control-msg:USB4-val is deprecated.  Use jdq_control-msg:USB4 instead.")
  (USB4 m))

(cl:ensure-generic-function 'USB5-val :lambda-list '(m))
(cl:defmethod USB5-val ((m <jdq_state>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader jdq_control-msg:USB5-val is deprecated.  Use jdq_control-msg:USB5 instead.")
  (USB5 m))

(cl:ensure-generic-function 'USB6-val :lambda-list '(m))
(cl:defmethod USB6-val ((m <jdq_state>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader jdq_control-msg:USB6-val is deprecated.  Use jdq_control-msg:USB6 instead.")
  (USB6 m))

(cl:ensure-generic-function 'USB7-val :lambda-list '(m))
(cl:defmethod USB7-val ((m <jdq_state>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader jdq_control-msg:USB7-val is deprecated.  Use jdq_control-msg:USB7 instead.")
  (USB7 m))

(cl:ensure-generic-function 'USB8-val :lambda-list '(m))
(cl:defmethod USB8-val ((m <jdq_state>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader jdq_control-msg:USB8-val is deprecated.  Use jdq_control-msg:USB8 instead.")
  (USB8 m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <jdq_state>) ostream)
  "Serializes a message object of type '<jdq_state>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'USB1))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'USB1))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'USB2))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'USB2))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'USB3))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'USB3))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'USB4))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'USB4))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'USB5))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'USB5))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'USB6))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'USB6))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'USB7))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'USB7))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'USB8))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'USB8))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <jdq_state>) istream)
  "Deserializes a message object of type '<jdq_state>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'USB1) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'USB1) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'USB2) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'USB2) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'USB3) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'USB3) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'USB4) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'USB4) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'USB5) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'USB5) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'USB6) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'USB6) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'USB7) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'USB7) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'USB8) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'USB8) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<jdq_state>)))
  "Returns string type for a message object of type '<jdq_state>"
  "jdq_control/jdq_state")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'jdq_state)))
  "Returns string type for a message object of type 'jdq_state"
  "jdq_control/jdq_state")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<jdq_state>)))
  "Returns md5sum for a message object of type '<jdq_state>"
  "ce22d24026240afb77c18e56ea2ac5ba")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'jdq_state)))
  "Returns md5sum for a message object of type 'jdq_state"
  "ce22d24026240afb77c18e56ea2ac5ba")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<jdq_state>)))
  "Returns full string definition for message of type '<jdq_state>"
  (cl:format cl:nil "string USB1~%string USB2~%string USB3~%string USB4~%string USB5~%string USB6~%string USB7~%string USB8~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'jdq_state)))
  "Returns full string definition for message of type 'jdq_state"
  (cl:format cl:nil "string USB1~%string USB2~%string USB3~%string USB4~%string USB5~%string USB6~%string USB7~%string USB8~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <jdq_state>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'USB1))
     4 (cl:length (cl:slot-value msg 'USB2))
     4 (cl:length (cl:slot-value msg 'USB3))
     4 (cl:length (cl:slot-value msg 'USB4))
     4 (cl:length (cl:slot-value msg 'USB5))
     4 (cl:length (cl:slot-value msg 'USB6))
     4 (cl:length (cl:slot-value msg 'USB7))
     4 (cl:length (cl:slot-value msg 'USB8))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <jdq_state>))
  "Converts a ROS message object to a list"
  (cl:list 'jdq_state
    (cl:cons ':USB1 (USB1 msg))
    (cl:cons ':USB2 (USB2 msg))
    (cl:cons ':USB3 (USB3 msg))
    (cl:cons ':USB4 (USB4 msg))
    (cl:cons ':USB5 (USB5 msg))
    (cl:cons ':USB6 (USB6 msg))
    (cl:cons ':USB7 (USB7 msg))
    (cl:cons ':USB8 (USB8 msg))
))
