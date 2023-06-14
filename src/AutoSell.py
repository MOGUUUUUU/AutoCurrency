import os
import win32gui
import pyautogui
import random
import pyperclip
import time

def r_pos(pos, range=1):
    return (pos[0] + random.randint(-range,range),pos[1] + random.randint(-range,range))

def r():
    return random.uniform(0.05, 0.06)

def get_pos_list(start, end):
    avr_x = (end[0] - start[0])/12
    avr_y = (end[1] - start[1])/5
    pos_list = []
    pos_x, pos_y = start[0] + avr_x/2, start[1] + avr_y/2
    while pos_x < end[0]:
        while pos_y < end[1]:
            pos_list.append((pos_x, pos_y))
            pos_y = pos_y + avr_y
        pos_y = start[1] + avr_y/2
        pos_x = pos_x + avr_x
    return pos_list

bag_start_pos = ()
bag_end_pos = ()

market_start_pos =()
market_end_pos = ()

bag_pos_list = get_pos_list(bag_start_pos, bag_end_pos)
market_pos_list = get_pos_list(market_start_pos, market_end_pos)

def set_price(price):
    pyautogui.click(button='right')
    time.sleep(r())
    text = f'=a/b/o {int(price)} chaos'
    pyautogui.move(random.randint(),random.randint(),duration=r())

def auto_sell(item_pos, market_pos, price, type='abo'):
    pyautogui.press('space')
    pyautogui.press("\\")
    # move to '我的摊位
    pyautogui.moveTo(x=random.randint(231,309), y=random.randint(121,132), duration=r())
    time.sleep(r())
    pyautogui.click(button='left')
    pyautogui.keyDown('ctrl')
    pyautogui.moveTo(item_pos, duration=r())
    time.sleep(r())
    pyautogui.click(button='left')
    pyautogui.keyUp('ctrl')
    pyautogui.moveTo(market_pos, duration=r())
    set_price(price)
    