; Auto-generated. Do not edit!


(cl:in-package dm_motor-msg)


;//! \htmlinclude MotorFeedback.msg.html

(cl:defclass <MotorFeedback> (roslisp-msg-protocol:ros-message)
  ((pos
    :reader pos
    :initarg :pos
    :type cl:float
    :initform 0.0)
   (vel
    :reader vel
    :initarg :vel
    :type cl:float
    :initform 0.0)
   (t
    :reader t
    :initarg :t
    :type cl:float
    :initform 0.0))
)

(cl:defclass MotorFeedback (<MotorFeedback>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <MotorFeedback>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'MotorFeedback)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name dm_motor-msg:<MotorFeedback> is deprecated: use dm_motor-msg:MotorFeedback instead.")))

(cl:ensure-generic-function 'pos-val :lambda-list '(m))
(cl:defmethod pos-val ((m <MotorFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader dm_motor-msg:pos-val is deprecated.  Use dm_motor-msg:pos instead.")
  (pos m))

(cl:ensure-generic-function 'vel-val :lambda-list '(m))
(cl:defmethod vel-val ((m <MotorFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader dm_motor-msg:vel-val is deprecated.  Use dm_motor-msg:vel instead.")
  (vel m))

(cl:ensure-generic-function 't-val :lambda-list '(m))
(cl:defmethod t-val ((m <MotorFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader dm_motor-msg:t-val is deprecated.  Use dm_motor-msg:t instead.")
  (t m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <MotorFeedback>) ostream)
  "Serializes a message object of type '<MotorFeedback>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'pos))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'vel))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 't))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <MotorFeedback>) istream)
  "Deserializes a message object of type '<MotorFeedback>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'pos) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'vel) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 't) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<MotorFeedback>)))
  "Returns string type for a message object of type '<MotorFeedback>"
  "dm_motor/MotorFeedback")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MotorFeedback)))
  "Returns string type for a message object of type 'MotorFeedback"
  "dm_motor/MotorFeedback")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<MotorFeedback>)))
  "Returns md5sum for a message object of type '<MotorFeedback>"
  "cd635028afaa0f6aed3ef11a40a1d7e5")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'MotorFeedback)))
  "Returns md5sum for a message object of type 'MotorFeedback"
  "cd635028afaa0f6aed3ef11a40a1d7e5")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<MotorFeedback>)))
  "Returns full string definition for message of type '<MotorFeedback>"
  (cl:format cl:nil "float32 pos~%float32 vel~%float32 t~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'MotorFeedback)))
  "Returns full string definition for message of type 'MotorFeedback"
  (cl:format cl:nil "float32 pos~%float32 vel~%float32 t~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <MotorFeedback>))
  (cl:+ 0
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <MotorFeedback>))
  "Converts a ROS message object to a list"
  (cl:list 'MotorFeedback
    (cl:cons ':pos (pos msg))
    (cl:cons ':vel (vel msg))
    (cl:cons ':t (t msg))
))
