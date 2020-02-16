#! /usr/bin/env python3

import numpy as np
import cv2

def get_projection_matrices():
    """
    p_left  : 3x4
    p_right : 3x4
    
    Camera P matrix. Contains both intrinsic and extrinsic parameters.
    NOTE: Please change the values of these matrices based on the parameters specific to your           camera.
    """
    
    p_left = np.array([[640.0,   0.0, 640.0, 2176.0], 
                       [  0.0, 480.0, 480.0,  552.0], 
                       [  0.0,   0.0,   1.0,    1.4]])
    
    p_right = np.array([[640.0,   0.0, 640.0, 2176.0], 
                       [   0.0, 480.0, 480.0,  792.0], 
                       [   0.0,   0.0,   1.0,    1.4]])
    return p_left, p_right

def read_left_image():
    return cv2.imread("stereo_set/left_image.png")[...,::-1]

def read_right_image():
    return cv2.imread("stereo_set/right_image.png")[...,::-1]

def get_obstacle_image():
    """
    Obstacle location has been provided to you. In real world practice this is replaced by \
    Object detectors and the detector's output is filtered by image segmentation output.
    """
    img_left_color = read_left_image()
    return img_left_color[479:509, 547:593, :]