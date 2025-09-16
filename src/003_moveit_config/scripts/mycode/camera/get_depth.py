import numpy as np
import cv2
import rospy
import time
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
bridge = CvBridge()
import camera_configs

cv2.namedWindow("left")
cv2.namedWindow("right")
cv2.namedWindow("depth")
cv2.moveWindow("left", 0, 0)
cv2.moveWindow("right", 700, 0)
cv2.moveWindow("depth", 500, 500)
cv2.createTrackbar("num", "depth", 0, 10, lambda x: None)
cv2.createTrackbar("blockSize", "depth", 5, 255, lambda x: None)

rospy.init_node("camera_listener")

leftCameraTopicName = "/left"
rightCameraTopicName = "/right"

# camera1 = cv2.VideoCapture(0)
# camera2 = cv2.VideoCapture(1)

# 添加点击事件，打印当前点的距离
def callbackFunc(e, x, y, f, p):
    if e == cv2.EVENT_LBUTTONDOWN:        
        print(threeD[y][x])

cv2.setMouseCallback("depth", callbackFunc, None)


def getFrame(topicName, timeout=None):
    '''
    获取一帧数据

    获取指定话题的一帧数据
    '''
    return rospy.wait_for_message(topicName, Image, timeout=timeout)

while True:
    
    left_frame = getFrame(leftCameraTopicName, 1)
    right_frame = getFrame(rightCameraTopicName, 1)
    
    left_frame = bridge.imgmsg_to_cv2(left_frame, "bgr8")
    right_frame = bridge.imgmsg_to_cv2(right_frame, "bgr8")

    
    # 根据更正map对图片进行重构
    img1_rectified = cv2.remap(left_frame, camera_configs.left_map1, camera_configs.left_map2, cv2.INTER_LINEAR)
    img2_rectified = cv2.remap(right_frame, camera_configs.right_map1, camera_configs.right_map2, cv2.INTER_LINEAR)

    # 将图片置为灰度图，为StereoBM作准备
    imgL = cv2.cvtColor(img1_rectified, cv2.COLOR_BGR2GRAY)
    imgR = cv2.cvtColor(img2_rectified, cv2.COLOR_BGR2GRAY)

    # 两个trackbar用来调节不同的参数查看效果
    num = cv2.getTrackbarPos("num", "depth")
    blockSize = cv2.getTrackbarPos("blockSize", "depth")
    if blockSize % 2 == 0:
        blockSize += 1
    if blockSize < 5:
        blockSize = 5

    # 根据Block Maching方法生成差异图（opencv里也提供了SGBM/Semi-Global Block Matching算法，有兴趣可以试试）
    stereo = cv2.StereoBM_create(numDisparities=16*num, blockSize=blockSize)
    disparity = stereo.compute(imgL, imgR)

    disp = cv2.normalize(disparity, disparity, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    # 将图片扩展至3d空间中，其z方向的值则为当前的距离
    threeD = cv2.reprojectImageTo3D(disparity.astype(np.float32)/16., camera_configs.Q)
    
    cv2.imshow("left", img1_rectified)
    cv2.imshow("right", img2_rectified)
    cv2.imshow("depth", disp)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break
    elif key == ord("s"):
        cv2.imwrite("/home/arm003/roboarm3_ws/src/003_moveit_config/scripts/mycode/img/BM_left.jpg", imgL)
        cv2.imwrite("/home/arm003/roboarm3_ws/src/003_moveit_config/scripts/mycode/img/BM_right.jpg", imgR)
        cv2.imwrite("/home/arm003/roboarm3_ws/src/003_moveit_config/scripts/mycode/img/BM_depth.jpg", disp)

# camera1.release()
# camera2.release()
cv2.destroyAllWindows()
