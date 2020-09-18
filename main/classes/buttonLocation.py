

def inputTap(x, y):
	return 'adb shell input tap ' + str(x) + ' ' + str(y)

sSkillsYAxis = 870
servantOneSkillsDic = {'One':inputTap(175,sSkillsYAxis), 'Two':inputTap(315,sSkillsYAxis), 'Three':inputTap(460,sSkillsYAxis)}
servantTwoSkillsDic = {'One':inputTap(650,sSkillsYAxis), 'Two':inputTap(765,sSkillsYAxis), 'Three':inputTap(900,sSkillsYAxis)}
servantThreeSkillsDic = {'One':inputTap(1125,sSkillsYAxis), 'Two':inputTap(1265,sSkillsYAxis), 'Three':inputTap(1420,sSkillsYAxis)}
servantSkillsDic = {'One':servantOneSkillsDic, 'Two':servantTwoSkillsDic, 'Three':servantThreeSkillsDic}

attackDic = {'Attack':inputTap(1770,900), 'mSkill':inputTap(1825,490), 'mSkillOne':inputTap(1430,470), 'mSkillTwo':inputTap(1555,470), 'mSkillThree':inputTap(1700,470)}

commonDic = {'confirmSkill':inputTap(1420,630), 'chooseSOne':inputTap(580,700), 'chooseSTwo':inputTap(1000,700), 'chooseSThree':inputTap(1500,700)}

cardDic = {'cardTwo':inputTap(650,750), 'cardFour':inputTap(1450,780),'ultOne':inputTap(680,350),'ultTwo':inputTap(1027,320)}