import os
import time
from classes import buttonLocation as bl





def firstRound():
	os.system(bl.servantSkillsDic['Three']['One'])
	print('英灵3技能1')
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

	os.system(bl.servantSkillsDic['Two']['Three'])
	print('英灵2技能3')
	time.sleep(0.5)
	os.system(bl.commonDic['confirmSkill'])
	print('技能确定')
	time.sleep(2)
	   
	os.system(bl.attackDic['Attack'])
	print('Attack')
	time.sleep(0.75)
	os.system(bl.cardDic['ultTwo'])
	print('选择大招2')
	time.sleep(0.1)
	os.system(bl.cardDic['cardTwo'])
	print('选择卡牌2')
	time.sleep(0.1)
	os.system(bl.cardDic['cardFour'])
	print('选择卡牌4')
	#过渡时间30s  预计37s
	time.sleep(30)

def secondRound():
	os.system(bl.attackDic['mSkill'])
	print('开启御主技能')
	time.sleep(0.3)
	os.system(bl.attackDic['mSkillTwo'])
	print('选择御主技能2')
	time.sleep(0.3)
	os.system(bl.commonDic['confirmSkill'])
	print('技能确定')
	time.sleep(0.3)
	os.system(bl.commonDic['chooseSThree'])
	print('选择对象英灵3')
	time.sleep(2)

	os.system(bl.attackDic['Attack'])
	print('Attack')
	time.sleep(0.75)
	os.system(bl.cardDic['ultThree'])
	print('选择大招3')
	time.sleep(0.1)
	os.system(bl.cardDic['cardTwo'])
	print('选择卡牌2')
	time.sleep(0.1)
	os.system(bl.cardDic['cardFour'])
	print('选择卡牌4')
	#过渡时间35s  预计40s
	time.sleep(37)


def thirdRound():
	os.system(bl.servantSkillsDic['One']['Two'])
	print('英灵1技能2')
	time.sleep(0.5)
	os.system(bl.commonDic['confirmSkill'])
	print('技能确定')
	time.sleep(2)

	os.system(bl.servantSkillsDic['One']['One'])
	print('英灵1技能1')
	time.sleep(0.5)
	os.system(bl.commonDic['confirmSkill'])
	print('技能确定')
	time.sleep(2)

	os.system(bl.attackDic['Attack'])
	print('Attack')
	time.sleep(0.75)
	os.system(bl.cardDic['ultOne'])
	print('选择大招1')
	time.sleep(0.1)
	os.system(bl.cardDic['cardTwo'])
	print('选择卡牌2')
	time.sleep(0.1)
	os.system(bl.cardDic['cardFour'])
	print('选择卡牌4')
	#过渡时间35s  预计40s
	time.sleep(23)

def main():
	print('This is baserker team ready to engage')
	firstRound()
	secondRound()
	thirdRound()