cmake_minimum_required(VERSION 3.1.3)

project(003_moveit_config)

find_package(catkin REQUIRED COMPONENTS roscpp rospy message_generation std_msgs moveit_ros_planning_interface moveit_ros_move_group moveit_commander moveit_ros_planning_interface 
# apriltag_ros
)

add_message_files(
  FILES
  hdrarm_msg.msg)

catkin_package(
  CATKIN_DEPENDS
  message_runtime)

find_package(roslaunch)

install(DIRECTORY launch DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
  PATTERN "setup_assistant.launch" EXCLUDE)
install(DIRECTORY config DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})

include_directories( ${catkin_INCLUDE_DIRS})
add_executable(003_trajectory src/003_trajectory.cpp)
target_link_libraries(003_trajectory ${catkin_LIBRARIES})
# add_executable(tag_detection src/tag_detection.cpp)
# target_link_libraries(tag_detection ${catkin_LIBRARIES})

