// Auto-generated. Do not edit!

// (in-package dm_motor.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class hdrarm_msg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.motor_state = null;
      this.arm_mode = null;
      this.Emergency_Stop = null;
      this.drag_teachin = null;
      this.drag_teachin_name = null;
      this.joint1_angle = null;
      this.joint2_angle = null;
      this.joint3_angle = null;
      this.joint4_angle = null;
      this.joint5_angle = null;
      this.joint6_angle = null;
      this.arm_position_x = null;
      this.arm_position_y = null;
      this.arm_position_z = null;
      this.arm_orientation_x = null;
      this.arm_orientation_y = null;
      this.arm_orientation_z = null;
      this.arm_orientation_w = null;
    }
    else {
      if (initObj.hasOwnProperty('motor_state')) {
        this.motor_state = initObj.motor_state
      }
      else {
        this.motor_state = '';
      }
      if (initObj.hasOwnProperty('arm_mode')) {
        this.arm_mode = initObj.arm_mode
      }
      else {
        this.arm_mode = '';
      }
      if (initObj.hasOwnProperty('Emergency_Stop')) {
        this.Emergency_Stop = initObj.Emergency_Stop
      }
      else {
        this.Emergency_Stop = false;
      }
      if (initObj.hasOwnProperty('drag_teachin')) {
        this.drag_teachin = initObj.drag_teachin
      }
      else {
        this.drag_teachin = '';
      }
      if (initObj.hasOwnProperty('drag_teachin_name')) {
        this.drag_teachin_name = initObj.drag_teachin_name
      }
      else {
        this.drag_teachin_name = '';
      }
      if (initObj.hasOwnProperty('joint1_angle')) {
        this.joint1_angle = initObj.joint1_angle
      }
      else {
        this.joint1_angle = 0.0;
      }
      if (initObj.hasOwnProperty('joint2_angle')) {
        this.joint2_angle = initObj.joint2_angle
      }
      else {
        this.joint2_angle = 0.0;
      }
      if (initObj.hasOwnProperty('joint3_angle')) {
        this.joint3_angle = initObj.joint3_angle
      }
      else {
        this.joint3_angle = 0.0;
      }
      if (initObj.hasOwnProperty('joint4_angle')) {
        this.joint4_angle = initObj.joint4_angle
      }
      else {
        this.joint4_angle = 0.0;
      }
      if (initObj.hasOwnProperty('joint5_angle')) {
        this.joint5_angle = initObj.joint5_angle
      }
      else {
        this.joint5_angle = 0.0;
      }
      if (initObj.hasOwnProperty('joint6_angle')) {
        this.joint6_angle = initObj.joint6_angle
      }
      else {
        this.joint6_angle = 0.0;
      }
      if (initObj.hasOwnProperty('arm_position_x')) {
        this.arm_position_x = initObj.arm_position_x
      }
      else {
        this.arm_position_x = 0.0;
      }
      if (initObj.hasOwnProperty('arm_position_y')) {
        this.arm_position_y = initObj.arm_position_y
      }
      else {
        this.arm_position_y = 0.0;
      }
      if (initObj.hasOwnProperty('arm_position_z')) {
        this.arm_position_z = initObj.arm_position_z
      }
      else {
        this.arm_position_z = 0.0;
      }
      if (initObj.hasOwnProperty('arm_orientation_x')) {
        this.arm_orientation_x = initObj.arm_orientation_x
      }
      else {
        this.arm_orientation_x = 0.0;
      }
      if (initObj.hasOwnProperty('arm_orientation_y')) {
        this.arm_orientation_y = initObj.arm_orientation_y
      }
      else {
        this.arm_orientation_y = 0.0;
      }
      if (initObj.hasOwnProperty('arm_orientation_z')) {
        this.arm_orientation_z = initObj.arm_orientation_z
      }
      else {
        this.arm_orientation_z = 0.0;
      }
      if (initObj.hasOwnProperty('arm_orientation_w')) {
        this.arm_orientation_w = initObj.arm_orientation_w
      }
      else {
        this.arm_orientation_w = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type hdrarm_msg
    // Serialize message field [motor_state]
    bufferOffset = _serializer.string(obj.motor_state, buffer, bufferOffset);
    // Serialize message field [arm_mode]
    bufferOffset = _serializer.string(obj.arm_mode, buffer, bufferOffset);
    // Serialize message field [Emergency_Stop]
    bufferOffset = _serializer.bool(obj.Emergency_Stop, buffer, bufferOffset);
    // Serialize message field [drag_teachin]
    bufferOffset = _serializer.string(obj.drag_teachin, buffer, bufferOffset);
    // Serialize message field [drag_teachin_name]
    bufferOffset = _serializer.string(obj.drag_teachin_name, buffer, bufferOffset);
    // Serialize message field [joint1_angle]
    bufferOffset = _serializer.float64(obj.joint1_angle, buffer, bufferOffset);
    // Serialize message field [joint2_angle]
    bufferOffset = _serializer.float64(obj.joint2_angle, buffer, bufferOffset);
    // Serialize message field [joint3_angle]
    bufferOffset = _serializer.float64(obj.joint3_angle, buffer, bufferOffset);
    // Serialize message field [joint4_angle]
    bufferOffset = _serializer.float64(obj.joint4_angle, buffer, bufferOffset);
    // Serialize message field [joint5_angle]
    bufferOffset = _serializer.float64(obj.joint5_angle, buffer, bufferOffset);
    // Serialize message field [joint6_angle]
    bufferOffset = _serializer.float64(obj.joint6_angle, buffer, bufferOffset);
    // Serialize message field [arm_position_x]
    bufferOffset = _serializer.float64(obj.arm_position_x, buffer, bufferOffset);
    // Serialize message field [arm_position_y]
    bufferOffset = _serializer.float64(obj.arm_position_y, buffer, bufferOffset);
    // Serialize message field [arm_position_z]
    bufferOffset = _serializer.float64(obj.arm_position_z, buffer, bufferOffset);
    // Serialize message field [arm_orientation_x]
    bufferOffset = _serializer.float64(obj.arm_orientation_x, buffer, bufferOffset);
    // Serialize message field [arm_orientation_y]
    bufferOffset = _serializer.float64(obj.arm_orientation_y, buffer, bufferOffset);
    // Serialize message field [arm_orientation_z]
    bufferOffset = _serializer.float64(obj.arm_orientation_z, buffer, bufferOffset);
    // Serialize message field [arm_orientation_w]
    bufferOffset = _serializer.float64(obj.arm_orientation_w, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type hdrarm_msg
    let len;
    let data = new hdrarm_msg(null);
    // Deserialize message field [motor_state]
    data.motor_state = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [arm_mode]
    data.arm_mode = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [Emergency_Stop]
    data.Emergency_Stop = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [drag_teachin]
    data.drag_teachin = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [drag_teachin_name]
    data.drag_teachin_name = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [joint1_angle]
    data.joint1_angle = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [joint2_angle]
    data.joint2_angle = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [joint3_angle]
    data.joint3_angle = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [joint4_angle]
    data.joint4_angle = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [joint5_angle]
    data.joint5_angle = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [joint6_angle]
    data.joint6_angle = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [arm_position_x]
    data.arm_position_x = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [arm_position_y]
    data.arm_position_y = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [arm_position_z]
    data.arm_position_z = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [arm_orientation_x]
    data.arm_orientation_x = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [arm_orientation_y]
    data.arm_orientation_y = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [arm_orientation_z]
    data.arm_orientation_z = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [arm_orientation_w]
    data.arm_orientation_w = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += _getByteLength(object.motor_state);
    length += _getByteLength(object.arm_mode);
    length += _getByteLength(object.drag_teachin);
    length += _getByteLength(object.drag_teachin_name);
    return length + 121;
  }

  static datatype() {
    // Returns string type for a message object
    return 'dm_motor/hdrarm_msg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '5a62e58a22a17162b499a805b6b83bb9';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string motor_state      #电机状态   ps:enable/disable
    string arm_mode	 #机械臂模式	ps:arm_sleep/arm_control_demo/arm_control_moveit_fk/arm_control_moveit_ik
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new hdrarm_msg(null);
    if (msg.motor_state !== undefined) {
      resolved.motor_state = msg.motor_state;
    }
    else {
      resolved.motor_state = ''
    }

    if (msg.arm_mode !== undefined) {
      resolved.arm_mode = msg.arm_mode;
    }
    else {
      resolved.arm_mode = ''
    }

    if (msg.Emergency_Stop !== undefined) {
      resolved.Emergency_Stop = msg.Emergency_Stop;
    }
    else {
      resolved.Emergency_Stop = false
    }

    if (msg.drag_teachin !== undefined) {
      resolved.drag_teachin = msg.drag_teachin;
    }
    else {
      resolved.drag_teachin = ''
    }

    if (msg.drag_teachin_name !== undefined) {
      resolved.drag_teachin_name = msg.drag_teachin_name;
    }
    else {
      resolved.drag_teachin_name = ''
    }

    if (msg.joint1_angle !== undefined) {
      resolved.joint1_angle = msg.joint1_angle;
    }
    else {
      resolved.joint1_angle = 0.0
    }

    if (msg.joint2_angle !== undefined) {
      resolved.joint2_angle = msg.joint2_angle;
    }
    else {
      resolved.joint2_angle = 0.0
    }

    if (msg.joint3_angle !== undefined) {
      resolved.joint3_angle = msg.joint3_angle;
    }
    else {
      resolved.joint3_angle = 0.0
    }

    if (msg.joint4_angle !== undefined) {
      resolved.joint4_angle = msg.joint4_angle;
    }
    else {
      resolved.joint4_angle = 0.0
    }

    if (msg.joint5_angle !== undefined) {
      resolved.joint5_angle = msg.joint5_angle;
    }
    else {
      resolved.joint5_angle = 0.0
    }

    if (msg.joint6_angle !== undefined) {
      resolved.joint6_angle = msg.joint6_angle;
    }
    else {
      resolved.joint6_angle = 0.0
    }

    if (msg.arm_position_x !== undefined) {
      resolved.arm_position_x = msg.arm_position_x;
    }
    else {
      resolved.arm_position_x = 0.0
    }

    if (msg.arm_position_y !== undefined) {
      resolved.arm_position_y = msg.arm_position_y;
    }
    else {
      resolved.arm_position_y = 0.0
    }

    if (msg.arm_position_z !== undefined) {
      resolved.arm_position_z = msg.arm_position_z;
    }
    else {
      resolved.arm_position_z = 0.0
    }

    if (msg.arm_orientation_x !== undefined) {
      resolved.arm_orientation_x = msg.arm_orientation_x;
    }
    else {
      resolved.arm_orientation_x = 0.0
    }

    if (msg.arm_orientation_y !== undefined) {
      resolved.arm_orientation_y = msg.arm_orientation_y;
    }
    else {
      resolved.arm_orientation_y = 0.0
    }

    if (msg.arm_orientation_z !== undefined) {
      resolved.arm_orientation_z = msg.arm_orientation_z;
    }
    else {
      resolved.arm_orientation_z = 0.0
    }

    if (msg.arm_orientation_w !== undefined) {
      resolved.arm_orientation_w = msg.arm_orientation_w;
    }
    else {
      resolved.arm_orientation_w = 0.0
    }

    return resolved;
    }
};

module.exports = hdrarm_msg;
