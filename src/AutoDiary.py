import os
import pyautogui
import win32gui
import pyperclip
import random
import time

key_value = { '区域内残骸数量提高': 40,
              '爆炸范围扩大': 40,
              '爆炸物数量提高': 40,
              '发掘的箱子有' : 25,
              '残骸有': 40,
              '炸药放置范围扩大': 50,
              '区域内怪物之印的数量提高': 40,
              '区域内符纹怪物之印的数量提高': 40,
              '区域内额外有': 16,
              '怪物掉落的神器数量提高': 40}

key_weights = {'区域内残骸数量提高': 1,
               '爆炸范围扩大': 1.05,
               '爆炸物数量提高': 1.15,
               '发掘的箱子有' : 2.15,
               '残骸有': 1.15,
               '炸药放置范围扩大': 1,
               '区域内怪物之印的数量提高': 1.15,
               '区域内符纹怪物之印的数量提高': 1.15,
               '区域内额外有': 2.15,
               '怪物掉落的神器数量提高': 1.1}

no_wants = ('药剂','冷却','元素伤害','总回复速度')

def r():
    return random.uniform(0.01, 0.03)

def get_pos():
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
    return item_pos
    
def auto_diary(item_pos):
    hld = win32gui.FindWindow(None,u"Path of Exile")
    win32gui.SetForegroundWindow(hld)
    ans = []
    pyautogui.moveTo(1223+random.randint(-5,5),614+random.randint(-5,5),duration=r())
    pyautogui.keyDown('shift')
    time.sleep(r())
    pyautogui.click(button='right')
    for pos in item_pos:
        pyautogui.moveTo(pos,duration=r())  
        os.system('echo off | clip')
        pyautogui.hotkey('ctrl','c',interval=r())
        flag = 0
        while not len(pyperclip.paste()) and flag < 5:
            flag += 1
            pyautogui.hotkey('ctrl','c',interval=r())
            time.sleep(r())
        if not len(pyperclip.paste()):
            pyautogui.keyUp('shift')
            return ans
        info = pyperclip.paste()
        count = 0
        while not check(info) and count < 10:
            count += 1
            pyautogui.click(button='left')
            time.sleep(r())
        if check(info):
            ans.append(pos)
    pyautogui.keyUp('shift')
    return ans
    
def check(info):
    text = info.split('-')
    for area in text:
        if len(area) and '黑镰' in area:
            line = area.split('\n')
            area_value = 0
            for needline in line:
                if '%' in needline:
                    line_type = needline.split(' ')[0]
                    area_value += key_value[line_type] * key_weights[line_type]
            now_value = 0  
            for needline in line:
                if '%' in needline:
                    line_type = needline.split(' ')[0]
                    line_value = int(needline.split(' ')[1].strip('%'))
                    now_value += line_value * key_weights[line_type]
            print (f'now_value is {now_value}  need value is {area_value*0.75}')
            if now_value >= area_value*0.75:
                return True
    return False

if __name__ == '__main__':
    item_pos = get_pos()
    ans = auto_diary(item_pos)
    print (len(ans))
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('shift')
    for pos in ans:
        pyautogui.moveTo(pos,duration=r())
        time.sleep(r())
        pyautogui.click(button='left')
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('shift')
    # ans = get_info(item_pos)
    # pyautogui.keyDown('ctrl')
    # pyautogui.keyDown('shift')
    # for pos in ans:
    #     pyautogui.moveTo(pos,duration=r())
    #     time.sleep(0.2+r())
    #     pyautogui.click(button='left')
        