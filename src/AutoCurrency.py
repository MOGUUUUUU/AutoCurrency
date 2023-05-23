import os
import win32gui
import pyautogui
import random
import pyperclip
import time

pos = dict()
os.system('echo off | clip')

with open('.\pos','r') as f:
    for line in f:
        pass

def r():
    return random.uniform(0.01,0.03)

def auto_currency(currency_type=None, needs=tuple(), limit=2400, *arg):
    hld = win32gui.FindWindow(None,u"Path of Exile")
    win32gui.SetForegroundWindow(hld)
    count = 0
    
    if currency_type and currency_type == 'alteration':
        count = use_alteration(needs=needs, limit=limit, target_pos=target_pos)
    
    print(f'total used {count} {currency_type}s')
    
def use_alteration(needs=tuple(), target_pos=None, limit=2400):
    count = 0
    if not target_pos:
        return 0
    pyautogui.moveTo(pos['alteration'], duration=r())
    time.sleep(0.1+r())
    pyautogui.click(button='right')
    pyautogui.keyDown('shift')
    pyautogui.moveTo(target_pos)
    last_paste = None 
    while True:
        if count >= limit:
            return count
        for need in needs:
            if last_paste and need in last_paste:
                pyautogui.keyUp('shift')
                return count
        pyautogui.click(button='left')
        time.sleep(r())
        count += 1
        while last_paste == pyperclip.paste():
            last_paste = pyperclip.paste()
            os.system('echo off | clip')
            pyautogui.click(button='left')
            count += 1
            pyautogui.hotkey('ctrl','c',interval=r())
            time.sleep(0.2+r())

if __name__ == '__main__':
    needs = tuple()
    item_pos = []
    start_pos = (0,0)
    end_pos = (0,0)
    posx, posy = 0, 0
    while posx < end_pos[0]:
        while posy < end_pos[1]:
            item_pos.append(posx + random.randint(-5,5), posy + random.randint(-5,5))
            posy += (end_pos[1] - start_pos[1])*0.2
        posx += (end_pos[0] - start_pos[0])*0.1
        posy = start_pos[1]
    
    for target_pos in item_pos:
        auto_currency(currency_type='alteration', needs=needs, limit=2400, target_pos=target_pos)