import subprocess
import pyautogui
import random
import pyperclip
import win32gui
import time
import put_to_ware


needs = ['链结石','机会石','崇高石','剥离石','觉醒六分仪','祝福石','重铸石','改造石','神圣石',\
    '改造石','混沌石','命运卡','链结石','制图钉','棱光催化剂','丰沃催化剂','不稳定的催化剂',\
        '启蒙(辅)','赋予(辅)','增幅(辅)','卡兰德','宝石匠的棱镜','远古石','瓦尔宝珠',\
            '安睡之凝珠宝','星团珠宝','脑层','有害催化剂'] 


       
avr_x=52
avr_y=52
items = []


def r():
    return random.uniform(0.01,0.03)


def check(text):
    if '深渊珠宝' in text and '物品等级: 86' in text:
        return True
    if '星团珠宝' in text:
        if '物品等级: 84' in text or '物品等级: 85' in text or '物品等级: 86' in text:
            return True
        else :
            return False
    else :
        return False
 
        
def bargain():
    minprice = 0
    while (True):
        flag = 0
        subprocess.run('echo off | clip',shell=True)
        while (len(pyperclip.paste()) == 0 and flag <2):
            flag += 1
            pyautogui.moveTo(random.randint(600,630),random.randint(755,762),duration=r())
            time.sleep(r())
            pyautogui.click(button='left',clicks=2,interval=r())
            time.sleep(r())
            pyautogui.hotkey('ctrl','c',interval=r())
        if len(pyperclip.paste()) == 0 :
            return
        maxprice = int(pyperclip.paste())
        subprocess.run('echo off | clip',shell=True)
        if abs(maxprice-minprice) > 6 :
            tmp = (minprice+maxprice)/2.15
            minprice = tmp
            pyautogui.typewrite(str(int(tmp)),interval=r())
        pyautogui.moveTo(random.randint(548,702),random.randint(854,874),duration=r())
        time.sleep(r())
        pyautogui.click(button='left')
        


def get_info():
    x_pos = 330
    y_pos = 280
    while (True):
        pyautogui.moveTo(x_pos+random.randint(-10,10),y_pos+random.randint(-10,10),duration=r())
        time.sleep(r())
        subprocess.run('echo off | clip',shell=True)
        flag = 0
        while (len(pyperclip.paste())==0 and flag <5):
            flag += 1
            pyautogui.hotkey('ctrl','c',interval=random.uniform(0,0.1))
        now_text = pyperclip.paste()
        if (len(now_text) == 0):
            return
        for needitem in needs:
            if needitem in now_text:
                # print (needitem+'\n')
                if needitem == '安睡之凝珠宝' or needitem == '星团珠宝':
                    if check(now_text) is not True:
                        continue
                items.append(needitem)
                pyautogui.click(button='left')
                bargain()
                break                
        subprocess.run('echo off | clip',shell=True)
        y_pos +=52
        if (y_pos>850):
            y_pos = 280
            x_pos += 52
        
def main(times):
    for i in range(times):
        get_info()
        pyautogui.moveTo(random.randint(929,960),random.randint(860,887),duration=r())
        pyautogui.click(button='left')
    
    pyautogui.moveTo(951,200,duration=r())
    time.sleep(0.1+r())
    pyautogui.click(button='left')
        
    pyautogui.moveTo(898,415,duration=r())
    time.sleep(0.1+r())
    pyautogui.click(button='left')
    time.sleep(0.1+r())
    
    put_to_ware.putting()
        
    pyautogui.keyDown('ctrl')
    pyautogui.moveTo(1017+random.randint(-2,2),358+random.randint(-1,1),duration=r())
    time.sleep(0.1+r())
    pyautogui.click(button='left')
    pyautogui.keyUp('ctrl')


if __name__ == '__main__':
    hld = win32gui.FindWindow(None,u"Path of Exile")
    win32gui.SetForegroundWindow(hld)
    
    for i in range (8):
        main(40)
    
    with open('log.txt','a',encoding='utf-8') as log:
        log.write(f'now time is {time.localtime()}\n')
        for item in items:
            log.write(item+'\n')