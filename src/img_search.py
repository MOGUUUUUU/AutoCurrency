 
import pyautogui
import cv2
import numpy as np

# Load the target image
target_image = cv2.imread('target_image.png')

# Get the screen resolution
screen_width, screen_height = pyautogui.size()

# Take a screenshot of the screen
screenshot = pyautogui.screenshot()

# Convert the screenshot to a numpy array
screenshot = np.array(screenshot)

# Convert the color space of the target image and the screenshot to grayscale
target_image_gray = cv2.cvtColor(target_image, cv2.COLOR_BGR2GRAY)
screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

# Find the target image in the screenshot using template matching
result = cv2.matchTemplate(screenshot_gray, target_image_gray, cv2.TM_CCOEFF_NORMED)

# Get the location of the target image in the screenshot
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
target_x, target_y = max_loc

# Move the mouse to the location of the target image
pyautogui.moveTo(target_x, target_y)

 
# -*- coding: utf-8 -*-
# 生成中文注释
# 找到目标图像在屏幕截图中的位置，并将鼠标移动到该位置

