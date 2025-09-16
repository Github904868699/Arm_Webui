// #include "ros/ros.h"
// #include "apriltag_ros/AprilTagDetectionArray.h"
// #include <iostream>
// class Localizer{

//     public:

//         ros::Subscriber ar_sub_;
//         apriltag_ros::AprilTagDetectionArray::ConstPtr last_msg_;
        
//         Localizer(ros::NodeHandle& nh) {
            
//             ar_sub_ = nh.subscribe<apriltag_ros::AprilTagDetectionArray>("tag_detections", 1, &Localizer::number_callback, this);
        
//         }

//         void number_callback(const apriltag_ros::AprilTagDetectionArray::ConstPtr& msg) {
            
//             last_msg_ = msg;
//             ROS_INFO_STREAM(last_msg_->detections[0].pose.pose.pose);

//         }

// };


// int main(int argc, char **argv)
// {
//     ros::init(argc, argv,"apriltag_detector_subscriber");
//     ros::NodeHandle node_obj;
//     Localizer localizer(node_obj);
//     //ros::Subscriber number_subscriber = node_obj.subscribe("tag_detections",1,number_callback);
//     ROS_INFO("1Vision node starting");
//     ros::spin();
//     //return 0;
// }
