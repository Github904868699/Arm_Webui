cmake_minimum_required(VERSION 3.0.2)
project(armcontrol_demo_pkg)

find_package(catkin REQUIRED
  COMPONENTS
  dynamic_reconfigure
  message_generation
  roscpp
  rospy
  std_msgs
)

 add_message_files(
   FILES
   hdrarm_msg.msg
 )
 
 generate_messages(
   DEPENDENCIES
   std_msgs
 )
 
 generate_dynamic_reconfigure_options(
   cfg/DynamicParam.cfg
 )
 
catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES armcontrol_demo_pkg
   CATKIN_DEPENDS
   dynamic_reconfigure
   message_generation
   roscpp rospy
   std_msgs
   message_runtime
)

include_directories(
include
  ${catkin_INCLUDE_DIRS}
)

add_executable(armcontrol_demo
  src/armcontrol_demo.cpp
)
add_dependencies(armcontrol_demo ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(armcontrol_demo
  ${catkin_LIBRARIES}
)

