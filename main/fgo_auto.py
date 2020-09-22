import os
import time


from classes import saberCasterTeam
from classes import archerLancerTeam
from classes import archerArcherTeam
from classes import baserkerTeam
from common import common

#setup.py bdist_msi for installer in cx_freeze



#roles = {1 : archerLancerTeam, 2 : archerArcherTeam, 3 : saberCasterTeam, 5: baserkerTeam}
roles = {1: baserkerTeam}


def main(choices, numberOfRounds, stamina, maxStamina):
	curStamina = stamina
	numberOfRound = numberOfRounds
	if curStamina < 40:
		eatGoldApples()
		curStamina += maxStamina
		time.sleep(5)
	common.reTop()
	while numberOfRound > 0:
		print('还有' + str(numberOfRound) + '次')
		common.choosingAlly()
		#time.sleep(3)
		choices.main()
		common.endingBit()
		#time.sleep(5)
		numberOfRound -= 1
		curStamina -= 40
		if numberOfRound != 0:
			if curStamina < 40:
				common.notReStart()
				eatGoldApples()
				curStamina += maxStamina
				time.sleep(5)
				common.reTop()
			else:
				common.reStart()
	print('-=-结束-=-')

def eatGoldApples():
	common.goldApples()

def eatSilverApples():
	common.silverApples()
	
