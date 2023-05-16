import win32gui
import win32con
import subprocess
import pyautogui

#通过窗口标题获取句柄
# id = win32gui.FindWindow(None,u"Path of Exile")
        
# win32gui.SetForegroundWindow(id)

# subprocess.run('echo off | clip',shell=True)
needs = ['链结石','机会石','崇高石','觉醒六分仪','祝福石','✿点金石','重铸石','改造石','神圣石',\
    '改造石','混沌石','命运卡','裂隙戒指','链结石','幻色石','催化剂',\
        '裂隙戒指','启蒙','赋予','增幅(辅)','卡兰德','宝石匠的棱镜','远古石','瓦尔宝珠',\
            '制图钉','安睡之凝珠宝','星团珠宝'] 

with open ('./tmp',encoding='utf-8') as f:
    i = f.readlines()
    for j in i:
        for item in needs:
            if item in j:
                print (item)
                