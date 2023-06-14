import pyautogui
import win32gui
import random
import time
import os
import pyperclip 

DIV2CHAOS = 180
DIV2SIXTANT = 50

sixtant_value = dict()
pos_sixtant = dict()

watchstone_click_pos = (995,942)
sixtant_click_pos = (433,430)
ware_pos = (898,419)


def r():
    return random.uniform(0.05, 0.1)

def r_pos(pos, range=1):
    return (pos[0]+random.randint(-range,range),pos[1]+random.randint(-range,range))

bag_start_pos = (1279, 593)
bag_end_pos = (1899, 844)
avr_x = (bag_end_pos[0] - bag_start_pos[0])/12
avr_y = (bag_end_pos[1] - bag_start_pos[1])/5
bag_pos_list = []
pos_x, pos_y = bag_start_pos[0] + avr_x/2, bag_start_pos[1] + avr_y/2
while pos_x < bag_end_pos[0]:
    while pos_y < bag_end_pos[1]:
        bag_pos_list.append(r_pos((pos_x, pos_y), range=3))
        pos_y = pos_y + avr_y
    pos_y = bag_start_pos[1] + avr_y/2
    pos_x = pos_x + avr_x

file_path = os.path.abspath(__file__)
file_root = os.path.dirname(file_path)
os.chdir(file_root)
with open('sixtant_value.txt', 'r', encoding='utf-8') as f:
    for line in f:
        sixtant = line.split(':')[0].strip()
        value = line.split(':')[1].strip()
        sixtant_value[sixtant] = int(value)
        
with open('pos_sixtant.txt', 'r', encoding='utf-8') as f:
    for line in f:
        pos = line.split(':')[0]
        sixtant = line.split(':')[1]
        pos_sixtant[pos] = sixtant
    
def click_sixtant():
    time.sleep(r())
    pyautogui.press('space')
    pyautogui.moveTo(r_pos(ware_pos), duration=r())
    time.sleep(r())
    pyautogui.click(button='left')
    time.sleep(r())
    pyautogui.moveTo(r_pos(sixtant_click_pos), duration=r())
    pyautogui.keyDown('shift')
    time.sleep(r())
    pyautogui.click(button='right')
    pyautogui.press('g')
    pyautogui.moveTo(r_pos(watchstone_click_pos), duration=r())
    time.sleep(r())    
    
def safe_click(button='left'):
    os.system('echo off | clip')
    time.sleep(0.1+r())
    totuse = 0
    while True:
        pyautogui.click(button=button)
        totuse += 1
        flag = 0
        while (not len(pyperclip.paste()) and flag < 5):
            pyautogui.hotkey('ctrl', 'c', interval=r()/10)
            time.sleep(r())
            flag = flag + 1
        if not len(pyperclip.paste()):
            if totuse > 3:
                return pyperclip.paste()
            continue
        return pyperclip.paste()
    
def get_sixtant_info(info):
    # print(info.split('\n'))
    sixtant = info.split('\n')[6].strip()
    return sixtant

compass_pos = (159,647)
def use_compass(bag_pos):       
    itempos = r_pos(pyautogui.position())
    pyautogui.keyUp('shift')
    time.sleep(r())
    pyautogui.press('space')
    pyautogui.moveTo(r_pos(ware_pos), duration=r())
    time.sleep(r())
    pyautogui.click(button='left')
    pyautogui.moveTo(r_pos(compass_pos), duration=r())
    pyautogui.click(button='right')
    time.sleep(r())
    pyautogui.press('g')
    time.sleep(r())
    pyautogui.moveTo(itempos, duration=r())
    time.sleep(r())
    pyautogui.click(button='left')
    pyautogui.press('i')
    time.sleep(r())
    pyautogui.moveTo(bag_pos, duration=r())
    time.sleep(r())
    pyautogui.click(button='left')
    pyautogui.press('i')
    
def auto_sixtant(times=160, ignore= 10):
    sixtants = []
    click_sixtant()
    idx = 0
    totval = 0
    i = 0
    for j in range(times):
        i = j + 1
        if idx > 30 :
            break
        info = safe_click()
        if not info:
            time.sleep(60+r()*5)
            print(f"Use sixtant error, wait 60 seconds.\n")
            continue
        sixtant = get_sixtant_info(info)
        if not (sixtant in sixtant_value):
            pyautogui.keyUp('shift')
            value = pyautogui.prompt(f'Set {sixtant}:')
            sixtant_value[sixtant] = int(value)
            if sixtant_value[sixtant] < ignore:
                click_sixtant()
                continue
        if sixtant_value[sixtant] < ignore:
            continue
        sixtants.append(sixtant)
        use_compass(r_pos(bag_pos_list[idx]))
        totval += sixtant_value[sixtant]
        idx = idx + 1
        time.sleep(r())
        click_sixtant()

    pyautogui.keyUp('shift')
    chaos_cost = i/DIV2SIXTANT+idx/DIV2CHAOS
    print('Use {}sixtants, Cost: {:.2f}Divs, Profits: {:.2f}Divs.\n'.format(i, chaos_cost/DIV2CHAOS, (totval-chaos_cost)/DIV2CHAOS))
    return sixtants


if __name__ == '__main__':
    hld = win32gui.FindWindow(None,u"Path of Exile")
    win32gui.SetForegroundWindow(hld)
    time.sleep(1)
    
    sixtants = auto_sixtant()
    pyautogui.keyUp('shift')
    
    
    # update "sixtant_value.txt"
    # sort by value down
    sixtant_price = sorted(sixtant_value.items(), key=lambda v:int(v[1]), reverse=True)
    with open('sixtant_value.txt', 'w', encoding='utf-8') as f:
        for info in sixtant_price:
            key, value = info
            line = f'{key}:{value}'
            f.write(line + '\n')    
    
            