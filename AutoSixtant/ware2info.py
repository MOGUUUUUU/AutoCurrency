import win32gui
import pyautogui
import pyperclip
import random
import time
import os


file_path = os.path.abspath(__file__)
file_root = os.path.dirname(file_path)
os.chdir(file_root)

def r():
    return random.uniform(0.1, 0.2)

def r_pos(pos, range=1):
    return (pos[0]+random.randint(-range,range),pos[1]+random.randint(-range,range))


start_pos = (24,137)
end_pos = (646,764)
pos_list = []
avr_x, avr_y = (end_pos[0]-start_pos[0])/24, (end_pos[1]-start_pos[1])/24
pos_x, pos_y = start_pos[0]+avr_x/2, start_pos[1]+avr_y/2

while pos_x < end_pos[0]:
    while pos_y < end_pos[1]:
        pos_list.append(r_pos((pos_x,pos_y)))
        pos_y = pos_y + avr_y
    pos_x = pos_x + avr_x
    pos_y = start_pos[1] + avr_y/2

print (len(pos_list))
def get_info():
    time.sleep(r())
    os.system('echo off | clip')
    flag = 0
    while not len(pyperclip.paste()) and flag <10:
        pyautogui.hotkey('ctrl','c')
        # time.sleep(r())
        flag += 1
    if flag == 10:
        return None
    else :
        return pyperclip.paste().split('\n')[6]
                        
def ware2log():
    with open('item_info', 'a', encoding='utf-8') as f:
      for item in pos_list:
          pyautogui.moveTo(item,duration=r())
          info = get_info()
          if not info:
              return 
          f.write(info)
          
if __name__ == '__main__':
    hld = win32gui.FindWindow(None,u"Path of Exile")
    win32gui.SetForegroundWindow(hld)
    time.sleep(1)
    
    ware2log()