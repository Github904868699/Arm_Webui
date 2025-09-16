#!/usr/bin/env python
# coding: utf-8
# filename: camera_configs.py
import cv2
import numpy as np

left_camera_matrix = np.array([[533.0936433788006, 0.0, 301.412956301103],
                                [0.0, 535.0498774459012, 262.001159552022],
                                [0.0, 0.0, 1.0]])

left_distortion = np.array([[-0.008033768106157003, 0.02104854895747246, 0.002858586736929647, -0.004188533574374423, 0.0]])

right_camera_matrix = left_camera_matrix    
right_distortion = left_distortion

om = np.array([0., 0., 0.]) # 旋转关系向量
R = cv2.Rodrigues(om)[0]  # 使用Rodrigues变换将om变换为R
T = np.array([-50., 0., -0.]) # 平移关系向量

size = (1280, 720) # 图像尺寸 (width, height)

# 进行立体更正
R1, R2, P1, P2, Q, validPixROI1, validPixROI2 = cv2.stereoRectify(left_camera_matrix, left_distortion,
                                                                  right_camera_matrix, right_distortion, size, R,
                                                                  T)
# 计算更正map
left_map1, left_map2 = cv2.initUndistortRectifyMap(left_camera_matrix, left_distortion, R1, P1, size, cv2.CV_16SC2)
right_map1, right_map2 = cv2.initUndistortRectifyMap(right_camera_matrix, right_distortion, R2, P2, size, cv2.CV_16SC2)


