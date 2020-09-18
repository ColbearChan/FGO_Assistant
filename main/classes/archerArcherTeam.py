import os
import time
from classes import buttonLocation as bl

def firstRound():
    os.system(bl.servantSkillsDic['One']['Three'])
    print('英灵1技能3')
    time.sleep(0.5)
    os.system(bl.commonDic['confirmSkill'])
    print('技能确定')
    time.sleep(2)

    os.system(bl.servantSkillsDic['Two']['Three'])
    print('英灵2技能3')
    time.sleep(0.5)
    os.system(bl.commonDic['confirmSkill'])
    print('技能确定')
    time.sleep(2)
       
    os.system(bl.attackDic['Attack'])
    print('Attack')
    time.sleep(1.0)
    os.system(bl.cardDic['ultOne'])
    print('选择大招1')
    time.sleep(0.2)
    os.system(bl.cardDic['cardTwo'])
    print('选择卡牌2')
    time.sleep(0.2)
    os.system(bl.cardDic['cardFour'])
    print('选择卡牌4')
    #过渡时间26s  预计30s
    time.sleep(40)


def secondRound():
    os.system(bl.servantSkillsDic['Two']['One'])
    print('英灵2技能1')
    time.sleep(0.5)
    os.system(bl.commonDic['confirmSkill'])
    print('技能确定')
    time.sleep(2)    
    os.system(bl.servantSkillsDic['Two']['Two'])
    print('英灵2技能2')
    time.sleep(0.5)
    os.system(bl.commonDic['confirmSkill'])
    print('技能确定')
    time.sleep(2)

    os.system(bl.servantSkillsDic['Three']['One'])
    print('英灵3技能1')
    time.sleep(0.5)
    os.system(bl.commonDic['confirmSkill'])
    print('技能确定')
    time.sleep(0.3)
    os.system(bl.commonDic['chooseSOne'])
    print('选择对象英灵1')
    time.sleep(2)
    os.system(bl.servantSkillsDic['Three']['Two'])
    print('英灵3技能2')
    time.sleep(0.5)
    os.system(bl.commonDic['confirmSkill'])
    print('技能确定')
    time.sleep(3)    
    os.system(bl.servantSkillsDic['Three']['Three'])
    print('英灵3技能3')
    time.sleep(0.5)
    os.system(bl.commonDic['confirmSkill'])
    print('技能确定')
    time.sleep(3)    
    

    os.system(bl.attackDic['Attack'])
    print('Attack')
    time.sleep(1.0)
    os.system(bl.cardDic['ultTwo'])
    print('选择大招2')
    time.sleep(0.2)
    os.system(bl.cardDic['cardTwo'])
    print('选择卡牌2')
    time.sleep(0.2)
    os.system(bl.cardDic['cardFour'])
    print('选择卡牌4')
    #过渡时间31s  预计33s
    time.sleep(40)


def thirdRound():
    os.system(bl.servantSkillsDic['One']['Three'])
    print('英灵1技能3')
    time.sleep(0.5)
    os.system(bl.commonDic['confirmSkill'])
    print('技能确定')
    time.sleep(2)

    #os.system('adb shell input tap 1860 470')
    #print('开启御主技能')
    #time.sleep(0.3)
    #os.system('adb shell input tap 1555 488')
    #print('选择御主技能2')
    #time.sleep(0.3)
    #os.system('adb shell input tap 1350 630')
    #print('技能确定')
    #time.sleep(0.3)
    #os.system('adb shell input tap 580 700')
    #print('选择对象英灵1')
    #time.sleep(2)
    
    os.system(bl.attackDic['Attack'])
    print('Attack')
    time.sleep(1.0)
    os.system(bl.cardDic['ultOne'])
    print('选择大招1')
    time.sleep(0.2)
    os.system(bl.cardDic['cardTwo'])
    print('选择卡牌2')
    time.sleep(0.2)
    os.system(bl.cardDic['cardFour'])
    print('选择卡牌4')
    time.sleep(30)

def main():
    print('This is archer archer team ready to roll')
    firstRound()
    secondRound()
    thirdRound()






    
