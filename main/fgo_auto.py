import os
import time


from classes import saberCasterTeam
from classes import archerLancerTeam
from classes import archerArcherTeam
from common import common

#setup.py bdist_msi for installer in cx_freeze

#common.apples()
#time.sleep(3)
#i = int(input('输入次数: '))
#while i > 0:
##    common.reTop()
##    common.choosingAlly()
##    time.sleep(3)
    #saberCasterTeam.main()
    #common.endingBit()
    #time.sleep(2)
    #i = i - 1

roles = {1 : archerLancerTeam, 2 : archerArcherTeam, 3 : saberCasterTeam}

def main(choices, numberOfRounds):
	numberOfRound = numberOfRounds
	while numberOfRound > 0:
		print('还有' + str(numberOfRound) + '次')
		common.reTop()
		common.choosingAlly()
		time.sleep(3)
		choices.main()
		common.endingBit()
		time.sleep(5)
		numberOfRound = numberOfRound - 1


def eatGoldApples():
	common.goldApples()

def eatSilverApples():
	common.silverApples()
	