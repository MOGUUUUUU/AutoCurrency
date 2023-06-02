import numpy as np
import cv2
import time
import win32gui
import pyautogui
import random

def r():
    return random.uniform(0.2,0.5)

def get_img():
    pass

def next_page():
    pass

def purchase_item(pos):
    pyautogui.moveTo(pos,duration=r())
    pyautogui.click(button='left')
    pass
    
def init_purchase():
    pyautogui.press('/')
    time.sleep(1+r())
    pyautogui.press('/')    
    
def cal_gray_value(img):
    r, g, b = cv2.split(img)
    r = np.asarray(r, np.intc)
    g = np.asarray(g, np.intc)
    b = np.asarray(b, np.intc)
    
    diff1 = (r-g).var()
    diff2 = (r-b).var()
    diff3 = (g-b).var()
    diff = (diff1 + diff2 + diff3) * 0.33
    return diff

def get_img_slice(img,w=1,h=1,unit_w=28,unit_h=28):
    width = w * unit_w
    height = h * unit_h
    img_slice = []
    last_posx, last_posy = 0, 0
    posx, posy = width, height
    while(posy <= img.shape[0]):
        while(posx <= img.shape[1]):
            data = img[last_posy:posy,last_posx:posx]
            gray_value = cal_gray_value(data)
            img_slice.append({'data': data,
                              'pos': ((posx+last_posx)*0.5+random.randint(-3,3),(posy+last_posy)*0.5+random.randint(-3,3)),
                              'gray_value': gray_value})
            last_posx = posx
            posx += width
        posx = width
        last_posx = 0
        last_posy = posy
        posy += height
    return img_slice
    
def check_slice(img_slice, limit=1500):
    if img_slice['gray_value'] > limit:
        return True
    return False
        
def auto_shopping():
    img = get_img()
    pos_list = []
    img_slice = get_img_slice(img)
    for slice in img_slice:
        if check_slice(slice):
            pos_list.append(slice['pos'])
    count = 0
    init_purchase()
    for pos in pos_list:
        if count >=5 :
            init_purchase()
            count = 0
        purchase_item(pos)
        count += 1
    next_page()
    return len(pos_list)
    
    
    
def main():
    hld = win32gui.FindWindow(None,u"Path of Exile")
    win32gui.SetForegroundWindow(hld)
    times = 5
    count = 0
    for i in range(times):
        count += auto_shopping()
    print(f'bought {count} items')
    
