import os
import time


#corn boy- cherry cola    moodblanc - faith (Ostberg Edit)

def goldApples():
    os.system('adb shell input tap 323 1049')
    print('AP回复')
    time.sleep(1)
    os.system('adb shell input tap 900 500')
    print('选择金苹果')
    time.sleep(0.5)
    os.system('adb shell input tap 1300 850')
    print('确定')

def silverApples():
    os.system('adb shell input tap 323 1049')
    print('AP回复')
    time.sleep(1)
    os.system('adb shell input tap 900 500')
    print('选择银苹果')
    time.sleep(0.5)
    os.system('adb shell input tap 1300 850')
    print('确定')   

def choosingAlly():
    time.sleep(3)
    os.system('adb shell input tap 1312 640')
    print("选择第二位支援英灵")
    time.sleep(4)
    os.system('adb shell input tap 1800 1000')
    print("确定")
    time.sleep(30)
    #过渡时间25s  预计28s

def endingBit():
    time.sleep(10)
    os.system('adb shell input tap 1312 640')
    print('羁绊确认')
    time.sleep(3)
    os.system('adb shell input tap 1312 640')
    print('经验确认')
    time.sleep(2)
    os.system('adb shell input tap 1800 1000')
    print('确认，下一步')
    #time.sleep(14)
    time.sleep(2)

def reTop():
    os.system('adb shell input tap 1460 280')
    print('选择最上面的任务')
    time.sleep(1.5)

def reStart():
    os.system('adb shell input tap 1350 860')
    time.sleep(1.5)

def notReStart():
    os.system('adb shell input tap 900 860')
    time.sleep(15)
