import numpy as np
import cv2
import time
import win32gui
import pyautogui
import random

def r():
    return random.uniform(0.2,0.3)

def get_img():
    pyautogui.moveTo(1900,1060,duration=r())
    img = pyautogui.screenshot()
    img = cv2.cvtColor(np.asarray(img),cv2.COLOR_RGB2BGR)
    return img

def next_page():
    pyautogui.moveTo(random.randint(477,588),random.randint(165,185),duration=r())
    pyautogui.click(button='left')
    time.sleep(2)
    
def confirm_price():
    pyautogui.moveTo(288,237,duration=r())
    pyautogui.moveTo(311,744,duration=0.5+r())
    pyautogui.moveTo(random.randint(115,185),random.randint(564,576),duration=r())
    time.sleep(r())
    pyautogui.click(button='left')
    time.sleep(0.5+r())
    pyautogui.moveTo(random.randint(290,323),random.randint(259,285),duration=r())
    time.sleep(1+r())
    pyautogui.keyDown('ctrl')
    pyautogui.click(button='left',clicks=10)
    time.sleep(r())
    pyautogui.keyUp('ctrl')
    pyautogui.moveTo(random.randint(477,535),random.randint(568,576),duration=r())
    pyautogui.click(button='left')

def purchase_item(pos):
    posx, posy = pos
    pyautogui.moveTo(posx+random.randint(-3,3),posy+random.randint(-3,3),duration=0.1+r())
    time.sleep(r())
    pyautogui.click(button='left')
    pyautogui.move(random.randint(51,134),random.randint(26,35),duration=0.1+r())
    time.sleep(r())
    pyautogui.click(button='left')
    confirm_price()
    init_purchase()
    
    
    
def init_purchase():
    pyautogui.press('/')
    time.sleep(0.2+r())
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
# (54,248)
# (610,804)
def get_img_slice(img,w=1,h=1,unit_w=46.33,unit_h=46.33):
    startx, starty = 54, 248
    endx, endy = 610, 804
    width = w * unit_w
    height = h * unit_h
    img_slice = []
    last_posx, last_posy = startx, starty
    posx, posy = last_posx+width, last_posy+height
    while(posy <= endy):
        while(posx <= endx):
            data = img[round(last_posy):round(posy),round(last_posx):round(posx)]
            pos = ((posx+last_posx)*0.5,(posy+last_posy)*0.5)
            gray_value = cal_gray_value(data)
            img_slice.append({'data': data,
                              'pos': pos,
                              'gray_value': gray_value})
            last_posx = posx
            posx += width
        posx = width + startx
        last_posx = startx
        last_posy = posy
        posy += height
    return img_slice
    
def check_slice(img_slice, limit=2800):
    if img_slice['gray_value'] > limit:
        return True
    return False
        
def auto_shopping():
    img = get_img()
    img_slice = get_img_slice(img)
    count = 0
    for slice in img_slice:
        if check_slice(slice):
            count += 1
            pyautogui.moveTo(slice['pos'],duration=r())
            print(f"pos is {slice['pos']}")
            print(slice['gray_value'])
            purchase_item(slice['pos'])  
            time.sleep(0.1+r())
    return count
    
    
def main():
    hld = win32gui.FindWindow(None,u"Path of Exile")
    win32gui.SetForegroundWindow(hld)
    time.sleep(1)
    pages = 100
    count = 0
    for i in range(pages):
        count += auto_shopping()
        next_page()
    print(f'bought {count} items')
    

if __name__ == '__main__':
    main()