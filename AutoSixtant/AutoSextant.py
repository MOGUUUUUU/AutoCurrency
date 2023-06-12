import pyautogui
import win32gui
import random
import time
import os
import pyperclip 

DIV2CHAOS = 180
DIV2SIXTANT = 55

sixtant_value = dict()
pos_sixtant = dict()

watchstone_click_pos = ()
sixtant_click_pos = ()

with open('sixtant_value', 'r', encoding='utf-8') as f:
    for line in f:
        sixtant = line.split(':')[0]
        value = line.split(':')[1]
        sixtant_value[sixtant] = int(value)
        
with open('pos_sixtant', 'r', encoding='utf-8') as f:
    for line in f:
        pos = line.split(':')[0]
        sixtant = line.split(':')[1]
        pos_sixtant[pos] = sixtant

def r():
    return random.uniform(0.1, 0.2)

def cal_profit():
    value = 0
    
def click_sixtant():
    pyautogui.moveTo(sixtant_click_pos, duration=r())
    pyautogui.keyDown('shift')
    time.sleep(r())
    pyautogui.click(button='right')
    pyautogui.moveTo(watchstone_click_pos, duration=r())    
    
def safe_click(button='left'):
    os.system('echo off | clip')
    # pyautogui.moveTo(pos[0]+random.randint(-1,1),pos[1]+random.randint(-1,1),duration=r())
    while True:
        pyautogui.click(button=button)
        flag = 0
        while (len(pyperclip.paste) and flag < 10):
            pyautogui.hotkey('ctrl', 'c', interval=r())
            flag = flag + 1
        if not len(pyperclip.paste()):
            continue
        return pyperclip.paste()
    
def get_sixtant(info):
    sixtant = info.split('\n')
    return sixtant
                
def auto_sixtant(times=55, ignore= 3):
    sixtants = []
    click_sixtant()
    for i in range(times):
        info = safe_click()
        sixtant = get_sixtant(info)
        if sixtant_value[sixtant] < ignore:
            continue
        sixtants.append(sixtant)
    return sixtants