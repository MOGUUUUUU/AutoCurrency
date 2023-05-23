import os
import win32gui
import pyautogui
import random
import pyperclip
import time
import subprocess

pos = dict()
pos['alteration'] = (108,304)
subprocess.run('echo off | clip',shell=True)

with open('./config/position','r') as f:
    for line in f:
        pass

def r():
    return random.uniform(0.01,0.03)

def auto_currency(currency_type=None, needs=tuple(), limit=2400, item_pos=[], *arg):
    hld = win32gui.FindWindow(None,u"Path of Exile")
    win32gui.SetForegroundWindow(hld)
    count = 0
    
    if currency_type and currency_type == 'alteration':
        count = use_alteration(needs=needs, limit=limit, item_pos=item_pos)
    
    print(f'total used {count} {currency_type}s')
    
def use_alteration(needs=tuple(), item_pos=None, limit=2400):
    count, totcount = 0, 0
    if not len(item_pos):
        return 0
    pyautogui.moveTo(pos['alteration'][0]+random.randint(-1,1),pos['alteration'][1]+random.randint(-1,1), duration=r())
    time.sleep(0.1+r())
    pyautogui.click(button='right')
    pyautogui.keyDown('shift')
    need = '冷却回复速度加快 3%'
    f = open('log.txt','w',encoding='utf-8')
    for target_pos in item_pos:
        print(need)
        totcount += count
        count = 0
        pyautogui.moveTo(target_pos,duration=0.3+r())
        while True:
            pyautogui.hotkey('ctrl','c')
            if count >= limit:
                pyautogui.keyUp('shift')
                print('Exceed limit!')
                return (totcount + count)
            if need in pyperclip.paste():
                break
            # for need in needs:
            #     print (f'needs: {need}')
            #     if need in pyperclip.paste():
            #         pyautogui.keyUp('shift')
            #         break
            pyautogui.click(button='left')
            pyautogui.hotkey('ctrl','c')
            time.sleep(0.2+r())
            count += 1
            print(f'total_click: {totcount}',file=f)
            print(f'item_click: {count}',file=f)
            print(f'paste is:\n {pyperclip.paste()}',file=f)
    return totcount

if __name__ == '__main__':
    # hld = win32gui.FindWindow(None,u"Path of Exile")
    # win32gui.SetForegroundWindow(hld)
    
    needs = ('冷却回复速度加快 3%','###thisistuple')
    item_pos = []
    start_pos = (1273,589)
    end_pos = (1903,847)
    avr_x = (end_pos[0]-start_pos[0])/12
    avr_y = (end_pos[1]-start_pos[1])/5
    posx, posy = 1294, 612
    while posx < end_pos[0]:
        while posy < end_pos[1]:
            item_pos.append((posx + random.randint(-2,2), posy + random.randint(-2,2)))
            posy += avr_y
        posx += avr_x
        posy = 612
    auto_currency(currency_type='alteration', needs=needs,limit=10000, item_pos=item_pos)
    # for target_pos in item_pos:
    #     # pyautogui.moveTo(target_pos,duration=r())
    #     auto_currency(currency_type='alteration', needs=needs, limit=10, target_pos=target_pos)
    #     break