import os
import time

def firstIn():
    os.system('adb shell input tap 1400 550')
    time.sleep(1)
    os.system('adb shell input tap 1360 280')
    time.sleep(1)
    os.system('adb shell input swipe 1312 870 1208 640')
    time.sleep(0.5)
    os.system('adb shell input tap 1450 940')
    time.sleep(1)

def secondIn():
    os.system('adb shell input tap 1400 550')
    time.sleep(1)
    os.system('adb shell input tap 1360 280')
    time.sleep(1)
    os.system('adb shell input tap 1530 255')
    time.sleep(1)

