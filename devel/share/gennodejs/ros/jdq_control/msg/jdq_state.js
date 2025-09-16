// Auto-generated. Do not edit!

// (in-package jdq_control.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class jdq_state {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.USB1 = null;
      this.USB2 = null;
      this.USB3 = null;
      this.USB4 = null;
      this.USB5 = null;
      this.USB6 = null;
      this.USB7 = null;
      this.USB8 = null;
    }
    else {
      if (initObj.hasOwnProperty('USB1')) {
        this.USB1 = initObj.USB1
      }
      else {
        this.USB1 = '';
      }
      if (initObj.hasOwnProperty('USB2')) {
        this.USB2 = initObj.USB2
      }
      else {
        this.USB2 = '';
      }
      if (initObj.hasOwnProperty('USB3')) {
        this.USB3 = initObj.USB3
      }
      else {
        this.USB3 = '';
      }
      if (initObj.hasOwnProperty('USB4')) {
        this.USB4 = initObj.USB4
      }
      else {
        this.USB4 = '';
      }
      if (initObj.hasOwnProperty('USB5')) {
        this.USB5 = initObj.USB5
      }
      else {
        this.USB5 = '';
      }
      if (initObj.hasOwnProperty('USB6')) {
        this.USB6 = initObj.USB6
      }
      else {
        this.USB6 = '';
      }
      if (initObj.hasOwnProperty('USB7')) {
        this.USB7 = initObj.USB7
      }
      else {
        this.USB7 = '';
      }
      if (initObj.hasOwnProperty('USB8')) {
        this.USB8 = initObj.USB8
      }
      else {
        this.USB8 = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type jdq_state
    // Serialize message field [USB1]
    bufferOffset = _serializer.string(obj.USB1, buffer, bufferOffset);
    // Serialize message field [USB2]
    bufferOffset = _serializer.string(obj.USB2, buffer, bufferOffset);
    // Serialize message field [USB3]
    bufferOffset = _serializer.string(obj.USB3, buffer, bufferOffset);
    // Serialize message field [USB4]
    bufferOffset = _serializer.string(obj.USB4, buffer, bufferOffset);
    // Serialize message field [USB5]
    bufferOffset = _serializer.string(obj.USB5, buffer, bufferOffset);
    // Serialize message field [USB6]
    bufferOffset = _serializer.string(obj.USB6, buffer, bufferOffset);
    // Serialize message field [USB7]
    bufferOffset = _serializer.string(obj.USB7, buffer, bufferOffset);
    // Serialize message field [USB8]
    bufferOffset = _serializer.string(obj.USB8, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type jdq_state
    let len;
    let data = new jdq_state(null);
    // Deserialize message field [USB1]
    data.USB1 = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [USB2]
    data.USB2 = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [USB3]
    data.USB3 = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [USB4]
    data.USB4 = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [USB5]
    data.USB5 = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [USB6]
    data.USB6 = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [USB7]
    data.USB7 = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [USB8]
    data.USB8 = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += _getByteLength(object.USB1);
    length += _getByteLength(object.USB2);
    length += _getByteLength(object.USB3);
    length += _getByteLength(object.USB4);
    length += _getByteLength(object.USB5);
    length += _getByteLength(object.USB6);
    length += _getByteLength(object.USB7);
    length += _getByteLength(object.USB8);
    return length + 32;
  }

  static datatype() {
    // Returns string type for a message object
    return 'jdq_control/jdq_state';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'ce22d24026240afb77c18e56ea2ac5ba';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string USB1
    string USB2
    string USB3
    string USB4
    string USB5
    string USB6
    string USB7
    string USB8
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new jdq_state(null);
    if (msg.USB1 !== undefined) {
      resolved.USB1 = msg.USB1;
    }
    else {
      resolved.USB1 = ''
    }

    if (msg.USB2 !== undefined) {
      resolved.USB2 = msg.USB2;
    }
    else {
      resolved.USB2 = ''
    }

    if (msg.USB3 !== undefined) {
      resolved.USB3 = msg.USB3;
    }
    else {
      resolved.USB3 = ''
    }

    if (msg.USB4 !== undefined) {
      resolved.USB4 = msg.USB4;
    }
    else {
      resolved.USB4 = ''
    }

    if (msg.USB5 !== undefined) {
      resolved.USB5 = msg.USB5;
    }
    else {
      resolved.USB5 = ''
    }

    if (msg.USB6 !== undefined) {
      resolved.USB6 = msg.USB6;
    }
    else {
      resolved.USB6 = ''
    }

    if (msg.USB7 !== undefined) {
      resolved.USB7 = msg.USB7;
    }
    else {
      resolved.USB7 = ''
    }

    if (msg.USB8 !== undefined) {
      resolved.USB8 = msg.USB8;
    }
    else {
      resolved.USB8 = ''
    }

    return resolved;
    }
};

module.exports = jdq_state;
