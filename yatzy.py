from collections import namedtuple
from random import randint, shuffle

def new_scorepad():
	sp = {}
	for i in range(15):
		sp['Category'+str(i+1)] = 0
	sp['Total'] = 0	
	return sp
	
def die_rolls(n):
	for i in range(n):
		yield randint(1,6)

def Category1(p):
	print('\nRound 1: Ones')
	print('Try to get as many ones as possible')
	
	c = input('Press \'r\' to roll all dice: ')
	while c.lower() != 'r':
		c = input('Press \'r\' to roll all dice: ')

	for i in range(5):
		p.dice[i] = 0	
	keep_num = 0	
	# Roll 1	
	rolls = die_rolls(5)
	count = 1
	roll_save = []
	for i in rolls:
		print('Die '+str(count)+': '+str(i))
		roll_save.append(i)
		count += 1
	keep = input('Select the dice you want to keep (type in the die number separated by a space or enter to re-roll all): ')
	if len(keep) == 0:
		keep_dice = []
	else:
		keep_dice = [int(i) for i in keep.split(' ')]
	for i in keep_dice:
		p.dice[keep_num] = 	roll_save[i-1]
		keep_num += 1

	# Roll 2
	rolls = die_rolls(5-keep_num)
	count = 1
	roll_save = []
	for i in rolls:
		print('Die '+str(count)+': '+str(i))
		roll_save.append(i)
		count += 1
	keep = input('Select the dice you want to keep (type in the die number separated by a space or enter to re-roll all): ')
	if len(keep.strip()) == 0:
		keep_dice = []
	else:
		keep_dice = [int(i) for i in keep.strip().split(' ')]
	for i in keep_dice:
		p.dice[keep_num] = 	roll_save[i-1]
		keep_num += 1

	# Roll 3
	rolls = die_rolls(5-keep_num)
	count = 1
	for i in rolls:
		print('Die '+str(count)+': '+str(i))
		count += 1
		p.dice[keep_num] = i
		keep_num += 1
	
	cat1_score = p.dice.count(1)
	print('\nYour score in round 1 is: '+str(cat1_score))
	p.score['Category1'] = cat1_score
	p.score['Total'] += cat1_score 			

	return p

def Category2(p):
	print('\nRound 2: Twos')
	print('Try to get as many twos as possible')
	
	c = input('Press \'r\' to roll all dice: ')
	while c.lower() != 'r':
		c = input('Press \'r\' to roll all dice: ')

	for i in range(5):
		p.dice[i] = 0	
	keep_num = 0	
	# Roll 1	
	rolls = die_rolls(5)
	count = 1
	roll_save = []
	for i in rolls:
		print('Die '+str(count)+': '+str(i))
		roll_save.append(i)
		count += 1
	keep = input('Select the dice you want to keep (type in the die number separated by a space or enter to re-roll all): ')
	if len(keep) == 0:
		keep_dice = []
	else:
		keep_dice = [int(i) for i in keep.split(' ')]
	for i in keep_dice:
		p.dice[keep_num] = 	roll_save[i-1]
		keep_num += 1

	# Roll 2
	rolls = die_rolls(5-keep_num)
	count = 1
	roll_save = []
	for i in rolls:
		print('Die '+str(count)+': '+str(i))
		roll_save.append(i)
		count += 1
	keep = input('Select the dice you want to keep (type in the die number separated by a space or enter to re-roll all): ')
	if len(keep.strip()) == 0:
		keep_dice = []
	else:
		keep_dice = [int(i) for i in keep.strip().split(' ')]
	for i in keep_dice:
		p.dice[keep_num] = 	roll_save[i-1]
		keep_num += 1

	# Roll 3
	rolls = die_rolls(5-keep_num)
	count = 1
	for i in rolls:
		print('Die '+str(count)+': '+str(i))
		count += 1
		p.dice[keep_num] = i
		keep_num += 1
	
	cat2_score = 2*p.dice.count(2)
	print('\nYour score in round 2 is: '+str(cat2_score))
	p.score['Category2'] = cat2_score
	p.score['Total'] += cat2_score 			

	return p

def Category3(p):
	print('\nRound 3: Threes')
	print('Try to get as many threes as possible')
	
	c = input('Press \'r\' to roll all dice: ')
	while c.lower() != 'r':
		c = input('Press \'r\' to roll all dice: ')

	for i in range(5):
		p.dice[i] = 0	
	keep_num = 0	
	# Roll 1	
	rolls = die_rolls(5)
	count = 1
	roll_save = []
	for i in rolls:
		print('Die '+str(count)+': '+str(i))
		roll_save.append(i)
		count += 1
	keep = input('Select the dice you want to keep (type in the die number separated by a space or enter to re-roll all): ')
	if len(keep) == 0:
		keep_dice = []
	else:
		keep_dice = [int(i) for i in keep.split(' ')]
	for i in keep_dice:
		p.dice[keep_num] = 	roll_save[i-1]
		keep_num += 1

	# Roll 2
	rolls = die_rolls(5-keep_num)
	count = 1
	roll_save = []
	for i in rolls:
		print('Die '+str(count)+': '+str(i))
		roll_save.append(i)
		count += 1
	keep = input('Select the dice you want to keep (type in the die number separated by a space or enter to re-roll all): ')
	if len(keep.strip()) == 0:
		keep_dice = []
	else:
		keep_dice = [int(i) for i in keep.strip().split(' ')]
	for i in keep_dice:
		p.dice[keep_num] = 	roll_save[i-1]
		keep_num += 1

	# Roll 3
	rolls = die_rolls(5-keep_num)
	count = 1
	for i in rolls:
		print('Die '+str(count)+': '+str(i))
		count += 1
		p.dice[keep_num] = i
		keep_num += 1
	
	cat3_score = 3*p.dice.count(3)
	print('\nYour score in round 3 is: '+str(cat3_score))
	p.score['Category3'] = cat3_score
	p.score['Total'] += cat3_score 			

	return p

def Category4(p):
	print('\nRound 4: Fours')
	print('Try to get as many fours as possible')
	
	c = input('Press \'r\' to roll all dice: ')
	while c.lower() != 'r':
		c = input('Press \'r\' to roll all dice: ')

	for i in range(5):
		p.dice[i] = 0	
	keep_num = 0	
	# Roll 1	
	rolls = die_rolls(5)
	count = 1
	roll_save = []
	for i in rolls:
		print('Die '+str(count)+': '+str(i))
		roll_save.append(i)
		count += 1
	keep = input('Select the dice you want to keep (type in the die number separated by a space or enter to re-roll all): ')
	if len(keep) == 0:
		keep_dice = []
	else:
		keep_dice = [int(i) for i in keep.split(' ')]
	for i in keep_dice:
		p.dice[keep_num] = 	roll_save[i-1]
		keep_num += 1

	# Roll 2
	rolls = die_rolls(5-keep_num)
	count = 1
	roll_save = []
	for i in rolls:
		print('Die '+str(count)+': '+str(i))
		roll_save.append(i)
		count += 1
	keep = input('Select the dice you want to keep (type in the die number separated by a space or enter to re-roll all): ')
	if len(keep.strip()) == 0:
		keep_dice = []
	else:
		keep_dice = [int(i) for i in keep.strip().split(' ')]
	for i in keep_dice:
		p.dice[keep_num] = 	roll_save[i-1]
		keep_num += 1

	# Roll 3
	rolls = die_rolls(5-keep_num)
	count = 1
	for i in rolls:
		print('Die '+str(count)+': '+str(i))
		count += 1
		p.dice[keep_num] = i
		keep_num += 1
	
	cat4_score = 4*p.dice.count(4)
	print('\nYour score in round 4 is: '+str(cat4_score))
	p.score['Category4'] = cat4_score
	p.score['Total'] += cat4_score 			

	return p

def Category5(p):
	print('\nRound 5: Fives')
	print('Try to get as many fives as possible')
	
	c = input('Press \'r\' to roll all dice: ')
	while c.lower() != 'r':
		c = input('Press \'r\' to roll all dice: ')

	for i in range(5):
		p.dice[i] = 0	
	keep_num = 0	
	# Roll 1	
	rolls = die_rolls(5)
	count = 1
	roll_save = []
	for i in rolls:
		print('Die '+str(count)+': '+str(i))
		roll_save.append(i)
		count += 1
	keep = input('Select the dice you want to keep (type in the die number separated by a space or enter to re-roll all): ')
	if len(keep) == 0:
		keep_dice = []
	else:
		keep_dice = [int(i) for i in keep.split(' ')]
	for i in keep_dice:
		p.dice[keep_num] = 	roll_save[i-1]
		keep_num += 1

	# Roll 2
	rolls = die_rolls(5-keep_num)
	count = 1
	roll_save = []
	for i in rolls:
		print('Die '+str(count)+': '+str(i))
		roll_save.append(i)
		count += 1
	keep = input('Select the dice you want to keep (type in the die number separated by a space or enter to re-roll all): ')
	if len(keep.strip()) == 0:
		keep_dice = []
	else:
		keep_dice = [int(i) for i in keep.strip().split(' ')]
	for i in keep_dice:
		p.dice[keep_num] = 	roll_save[i-1]
		keep_num += 1

	# Roll 3
	rolls = die_rolls(5-keep_num)
	count = 1
	for i in rolls:
		print('Die '+str(count)+': '+str(i))
		count += 1
		p.dice[keep_num] = i
		keep_num += 1
	
	cat5_score = 5*p.dice.count(5)
	print('\nYour score in round 5 is: '+str(cat5_score))
	p.score['Category5'] = cat5_score
	p.score['Total'] += cat5_score 			

	return p

def Category6(p):
	print('\nRound 6: Sixes')
	print('Try to get as many sixes as possible')
	
	c = input('Press \'r\' to roll all dice: ')
	while c.lower() != 'r':
		c = input('Press \'r\' to roll all dice: ')

	for i in range(5):
		p.dice[i] = 0	
	keep_num = 0	
	# Roll 1	
	rolls = die_rolls(5)
	count = 1
	roll_save = []
	for i in rolls:
		print('Die '+str(count)+': '+str(i))
		roll_save.append(i)
		count += 1
	keep = input('Select the dice you want to keep (type in the die number separated by a space or enter to re-roll all): ')
	if len(keep) == 0:
		keep_dice = []
	else:
		keep_dice = [int(i) for i in keep.split(' ')]
	for i in keep_dice:
		p.dice[keep_num] = 	roll_save[i-1]
		keep_num += 1

	# Roll 2
	rolls = die_rolls(5-keep_num)
	count = 1
	roll_save = []
	for i in rolls:
		print('Die '+str(count)+': '+str(i))
		roll_save.append(i)
		count += 1
	keep = input('Select the dice you want to keep (type in the die number separated by a space or enter to re-roll all): ')
	if len(keep.strip()) == 0:
		keep_dice = []
	else:
		keep_dice = [int(i) for i in keep.strip().split(' ')]
	for i in keep_dice:
		p.dice[keep_num] = 	roll_save[i-1]
		keep_num += 1

	# Roll 3
	rolls = die_rolls(5-keep_num)
	count = 1
	for i in rolls:
		print('Die '+str(count)+': '+str(i))
		count += 1
		p.dice[keep_num] = i
		keep_num += 1
	
	cat6_score = 6*p.dice.count(6)
	print('\nYour score in round 6 is: '+str(cat6_score))
	p.score['Category6'] = cat6_score
	p.score['Total'] += cat6_score 			

	return p

def Category7(p):
	print('\nRound 7: Pair')
	print('Try to get a pair of any number')
	
	c = input('Press \'r\' to roll all dice: ')
	while c.lower() != 'r':
		c = input('Press \'r\' to roll all dice: ')

	for i in range(5):
		p.dice[i] = 0	
	keep_num = 0	
	# Roll 1	
	rolls = die_rolls(5)
	count = 1
	roll_save = []
	for i in rolls:
		print('Die '+str(count)+': '+str(i))
		roll_save.append(i)
		count += 1
	keep = input('Select the dice you want to keep (type in the die number separated by a space or enter to re-roll all): ')
	if len(keep) == 0:
		keep_dice = []
	else:
		keep_dice = [int(i) for i in keep.split(' ')]
	for i in keep_dice:
		p.dice[keep_num] = 	roll_save[i-1]
		keep_num += 1

	# Roll 2
	rolls = die_rolls(5-keep_num)
	count = 1
	roll_save = []
	for i in rolls:
		print('Die '+str(count)+': '+str(i))
		roll_save.append(i)
		count += 1
	keep = input('Select the dice you want to keep (type in the die number separated by a space or enter to re-roll all): ')
	if len(keep.strip()) == 0:
		keep_dice = []
	else:
		keep_dice = [int(i) for i in keep.strip().split(' ')]
	for i in keep_dice:
		p.dice[keep_num] = 	roll_save[i-1]
		keep_num += 1

	# Roll 3
	rolls = die_rolls(5-keep_num)
	count = 1
	for i in rolls:
		print('Die '+str(count)+': '+str(i))
		count += 1
		p.dice[keep_num] = i
		keep_num += 1
	
	if p.dice.count(6) >= 2:
		cat7_score = 12
	elif p.dice.count(5) >= 2:
		cat7_score = 10
	elif p.dice.count(4) >= 2:
		cat7_score = 8
	elif p.dice.count(3) >= 2:
		cat7_score = 6
	elif p.dice.count(2) >= 2:
		cat7_score = 4
	elif p.dice.count(1) >= 2:
		cat7_score = 2
	else:
		cat7_score = 0	
	print('\nYour score in round 7 is: '+str(cat7_score))
	p.score['Category7'] = cat7_score
	p.score['Total'] += cat7_score 			

	return p		

def Category8(p):
	print('\nRound 8: Two Pairs')
	print('Try to get two distinct pairs of numbers')
	
	c = input('Press \'r\' to roll all dice: ')
	while c.lower() != 'r':
		c = input('Press \'r\' to roll all dice: ')

	for i in range(5):
		p.dice[i] = 0	
	keep_num = 0	
	# Roll 1	
	rolls = die_rolls(5)
	count = 1
	roll_save = []
	for i in rolls:
		print('Die '+str(count)+': '+str(i))
		roll_save.append(i)
		count += 1
	keep = input('Select the dice you want to keep (type in the die number separated by a space or enter to re-roll all): ')
	if len(keep) == 0:
		keep_dice = []
	else:
		keep_dice = [int(i) for i in keep.split(' ')]
	for i in keep_dice:
		p.dice[keep_num] = 	roll_save[i-1]
		keep_num += 1

	# Roll 2
	rolls = die_rolls(5-keep_num)
	count = 1
	roll_save = []
	for i in rolls:
		print('Die '+str(count)+': '+str(i))
		roll_save.append(i)
		count += 1
	keep = input('Select the dice you want to keep (type in the die number separated by a space or enter to re-roll all): ')
	if len(keep.strip()) == 0:
		keep_dice = []
	else:
		keep_dice = [int(i) for i in keep.strip().split(' ')]
	for i in keep_dice:
		p.dice[keep_num] = 	roll_save[i-1]
		keep_num += 1

	# Roll 3
	rolls = die_rolls(5-keep_num)
	count = 1
	for i in rolls:
		print('Die '+str(count)+': '+str(i))
		count += 1
		p.dice[keep_num] = i
		keep_num += 1
	
	if p.dice.count(6) >= 2:
		if p.dice.count(5) >= 2:
			cat8_score = 22
		elif p.dice.count(4) >= 2:
			cat8_score = 20
		elif p.dice.count(3) >= 2:
			cat8_score = 18
		elif p.dice.count(2) >= 2:
			cat8_score = 16
		elif p.dice.count(1) >= 2:
			cat8_score = 14
		else:
			cat8_score = 0	
	elif p.dice.count(5) >= 2:
		if p.dice.count(4) >= 2:
			cat8_score = 18
		elif p.dice.count(3) >= 2:
			cat8_score = 16
		elif p.dice.count(2) >= 2:
			cat8_score = 14
		elif p.dice.count(1) >= 2:
			cat8_score = 12
		else:
			cat8_score = 0
	elif p.dice.count(4) >= 2:
		if p.dice.count(3) >= 2:
			cat8_score = 14
		elif p.dice.count(2) >= 2:
			cat8_score = 12
		elif p.dice.count(1) >= 2:
			cat8_score = 10
		else:
			cat8_score = 0
	elif p.dice.count(3) >= 2:
		if p.dice.count(2) >= 2:
			cat8_score = 10
		elif p.dice.count(1) >= 2:
			cat8_score = 8
		else:
			cat8_score = 0
	elif p.dice.count(2) >= 2:
		if p.dice.count(1) >= 2:
			cat8_score = 6
		else:
			cat8_score = 0
	else:
		cat8_score = 0	
	print('\nYour score in round 8 is: '+str(cat8_score))
	p.score['Category8'] = cat8_score
	p.score['Total'] += cat8_score 			

	return p

def Category9(p):
	print('\nRound 9: Three of a kind')
	print('Try to get three dice showing same number')
	
	c = input('Press \'r\' to roll all dice: ')
	while c.lower() != 'r':
		c = input('Press \'r\' to roll all dice: ')

	for i in range(5):
		p.dice[i] = 0	
	keep_num = 0	
	# Roll 1	
	rolls = die_rolls(5)
	count = 1
	roll_save = []
	for i in rolls:
		print('Die '+str(count)+': '+str(i))
		roll_save.append(i)
		count += 1
	keep = input('Select the dice you want to keep (type in the die number separated by a space or enter to re-roll all): ')
	if len(keep) == 0:
		keep_dice = []
	else:
		keep_dice = [int(i) for i in keep.split(' ')]
	for i in keep_dice:
		p.dice[keep_num] = 	roll_save[i-1]
		keep_num += 1

	# Roll 2
	rolls = die_rolls(5-keep_num)
	count = 1
	roll_save = []
	for i in rolls:
		print('Die '+str(count)+': '+str(i))
		roll_save.append(i)
		count += 1
	keep = input('Select the dice you want to keep (type in the die number separated by a space or enter to re-roll all): ')
	if len(keep.strip()) == 0:
		keep_dice = []
	else:
		keep_dice = [int(i) for i in keep.strip().split(' ')]
	for i in keep_dice:
		p.dice[keep_num] = 	roll_save[i-1]
		keep_num += 1

	# Roll 3
	rolls = die_rolls(5-keep_num)
	count = 1
	for i in rolls:
		print('Die '+str(count)+': '+str(i))
		count += 1
		p.dice[keep_num] = i
		keep_num += 1
	
	if p.dice.count(6) >= 3:
		cat9_score = 18
	elif p.dice.count(5) >= 3:
		cat9_score = 15
	elif p.dice.count(4) >= 3:
		cat9_score = 12
	elif p.dice.count(3) >= 3:
		cat9_score = 9
	elif p.dice.count(2) >= 3:
		cat9_score = 6
	elif p.dice.count(1) >= 3:
		cat9_score = 3
	else:
		cat9_score = 0	
	print('\nYour score in round 9 is: '+str(cat9_score))
	p.score['Category9'] = cat9_score
	p.score['Total'] += cat9_score	

	return p	

def Category10(p):
	print('\nRound 10: Four of a kind')
	print('Try to get four dice showing the same number')
	
	c = input('Press \'r\' to roll all dice: ')
	while c.lower() != 'r':
		c = input('Press \'r\' to roll all dice: ')

	for i in range(5):
		p.dice[i] = 0	
	keep_num = 0	
	# Roll 1	
	rolls = die_rolls(5)
	count = 1
	roll_save = []
	for i in rolls:
		print('Die '+str(count)+': '+str(i))
		roll_save.append(i)
		count += 1
	keep = input('Select the dice you want to keep (type in the die number separated by a space or enter to re-roll all): ')
	if len(keep) == 0:
		keep_dice = []
	else:
		keep_dice = [int(i) for i in keep.split(' ')]
	for i in keep_dice:
		p.dice[keep_num] = 	roll_save[i-1]
		keep_num += 1

	# Roll 2
	rolls = die_rolls(5-keep_num)
	count = 1
	roll_save = []
	for i in rolls:
		print('Die '+str(count)+': '+str(i))
		roll_save.append(i)
		count += 1
	keep = input('Select the dice you want to keep (type in the die number separated by a space or enter to re-roll all): ')
	if len(keep.strip()) == 0:
		keep_dice = []
	else:
		keep_dice = [int(i) for i in keep.strip().split(' ')]
	for i in keep_dice:
		p.dice[keep_num] = 	roll_save[i-1]
		keep_num += 1

	# Roll 3
	rolls = die_rolls(5-keep_num)
	count = 1
	for i in rolls:
		print('Die '+str(count)+': '+str(i))
		count += 1
		p.dice[keep_num] = i
		keep_num += 1
	
	if p.dice.count(6) >= 4:
		cat10_score = 24
	elif p.dice.count(5) >= 4:
		cat10_score = 20
	elif p.dice.count(4) >= 4:
		cat10_score = 16
	elif p.dice.count(3) >= 4:
		cat10_score = 12
	elif p.dice.count(2) >= 4:
		cat10_score = 8
	elif p.dice.count(1) >= 4:
		cat10_score = 4
	else:
		cat10_score = 0	
	print('\nYour score in round 10 is: '+str(cat10_score))
	p.score['Category10'] = cat10_score
	p.score['Total'] += cat10_score 			

	return p

def Category11(p):
	print('\nRound 11: Small straight')
	print('Try to get the sequence 1, 2, 3, 4, 5 across the dice')
	
	c = input('Press \'r\' to roll all dice: ')
	while c.lower() != 'r':
		c = input('Press \'r\' to roll all dice: ')

	for i in range(5):
		p.dice[i] = 0	
	keep_num = 0	
	# Roll 1	
	rolls = die_rolls(5)
	count = 1
	roll_save = []
	for i in rolls:
		print('Die '+str(count)+': '+str(i))
		roll_save.append(i)
		count += 1
	keep = input('Select the dice you want to keep (type in the die number separated by a space or enter to re-roll all): ')
	if len(keep) == 0:
		keep_dice = []
	else:
		keep_dice = [int(i) for i in keep.split(' ')]
	for i in keep_dice:
		p.dice[keep_num] = 	roll_save[i-1]
		keep_num += 1

	# Roll 2
	rolls = die_rolls(5-keep_num)
	count = 1
	roll_save = []
	for i in rolls:
		print('Die '+str(count)+': '+str(i))
		roll_save.append(i)
		count += 1
	keep = input('Select the dice you want to keep (type in the die number separated by a space or enter to re-roll all): ')
	if len(keep.strip()) == 0:
		keep_dice = []
	else:
		keep_dice = [int(i) for i in keep.strip().split(' ')]
	for i in keep_dice:
		p.dice[keep_num] = 	roll_save[i-1]
		keep_num += 1

	# Roll 3
	rolls = die_rolls(5-keep_num)
	count = 1
	for i in rolls:
		print('Die '+str(count)+': '+str(i))
		count += 1
		p.dice[keep_num] = i
		keep_num += 1
	
	if 1 in p.dice and 2 in p.dice and 3 in p.dice and 4 in p.dice and 5 in p.dice:
		cat11_score = 15
	else:
		cat11_score = 0	
	print('\nYour score in round 11 is: '+str(cat11_score))
	p.score['Category11'] = cat11_score
	p.score['Total'] += cat11_score 			

	return p	

def Category12(p):
	print('\nRound 11: Large straight')
	print('Try to get the sequence 2, 3, 4, 5, 6 across the dice')
	
	c = input('Press \'r\' to roll all dice: ')
	while c.lower() != 'r':
		c = input('Press \'r\' to roll all dice: ')

	for i in range(5):
		p.dice[i] = 0	
	keep_num = 0	
	# Roll 1	
	rolls = die_rolls(5)
	count = 1
	roll_save = []
	for i in rolls:
		print('Die '+str(count)+': '+str(i))
		roll_save.append(i)
		count += 1
	keep = input('Select the dice you want to keep (type in the die number separated by a space or enter to re-roll all): ')
	if len(keep) == 0:
		keep_dice = []
	else:
		keep_dice = [int(i) for i in keep.split(' ')]
	for i in keep_dice:
		p.dice[keep_num] = 	roll_save[i-1]
		keep_num += 1

	# Roll 2
	rolls = die_rolls(5-keep_num)
	count = 1
	roll_save = []
	for i in rolls:
		print('Die '+str(count)+': '+str(i))
		roll_save.append(i)
		count += 1
	keep = input('Select the dice you want to keep (type in the die number separated by a space or enter to re-roll all): ')
	if len(keep.strip()) == 0:
		keep_dice = []
	else:
		keep_dice = [int(i) for i in keep.strip().split(' ')]
	for i in keep_dice:
		p.dice[keep_num] = 	roll_save[i-1]
		keep_num += 1

	# Roll 3
	rolls = die_rolls(5-keep_num)
	count = 1
	for i in rolls:
		print('Die '+str(count)+': '+str(i))
		count += 1
		p.dice[keep_num] = i
		keep_num += 1
	
	if 6 in p.dice and 2 in p.dice and 3 in p.dice and 4 in p.dice and 5 in p.dice:
		cat12_score = 20
	else:
		cat12_score = 0	
	print('\nYour score in round 12 is: '+str(cat12_score))
	p.score['Category12'] = cat12_score
	p.score['Total'] += cat12_score 			

	return p

def Category13(p):
	print('\nRound 13: Full house')
	print('Try to get one Three of a kind and one Pair')
	
	c = input('Press \'r\' to roll all dice: ')
	while c.lower() != 'r':
		c = input('Press \'r\' to roll all dice: ')

	for i in range(5):
		p.dice[i] = 0	
	keep_num = 0	
	# Roll 1	
	rolls = die_rolls(5)
	count = 1
	roll_save = []
	for i in rolls:
		print('Die '+str(count)+': '+str(i))
		roll_save.append(i)
		count += 1
	keep = input('Select the dice you want to keep (type in the die number separated by a space or enter to re-roll all): ')
	if len(keep) == 0:
		keep_dice = []
	else:
		keep_dice = [int(i) for i in keep.split(' ')]
	for i in keep_dice:
		p.dice[keep_num] = 	roll_save[i-1]
		keep_num += 1

	# Roll 2
	rolls = die_rolls(5-keep_num)
	count = 1
	roll_save = []
	for i in rolls:
		print('Die '+str(count)+': '+str(i))
		roll_save.append(i)
		count += 1
	keep = input('Select the dice you want to keep (type in the die number separated by a space or enter to re-roll all): ')
	if len(keep.strip()) == 0:
		keep_dice = []
	else:
		keep_dice = [int(i) for i in keep.strip().split(' ')]
	for i in keep_dice:
		p.dice[keep_num] = 	roll_save[i-1]
		keep_num += 1

	# Roll 3
	rolls = die_rolls(5-keep_num)
	count = 1
	for i in rolls:
		print('Die '+str(count)+': '+str(i))
		count += 1
		p.dice[keep_num] = i
		keep_num += 1
	
	if p.dice.count(6) >= 3:
		if p.dice.count(5) >= 2:
			cat13_score = 28
		elif p.dice.count(4) >= 2:
			cat13_score = 26
		elif p.dice.count(3) >= 2:
			cat13_score = 24
		elif p.dice.count(2) >= 2:
			cat13_score = 22
		elif p.dice.count(1) >= 2:
			cat13_score = 20
		else:
			cat13_score = 0	
	elif p.dice.count(5) >= 3:
		if p.dice.count(6) >= 2:
			cat13_score = 27
		elif p.dice.count(4) >= 2:
			cat13_score = 23	
		elif p.dice.count(3) >= 2:
			cat13_score = 21
		elif p.dice.count(2) >= 2:
			cat13_score = 19
		elif p.dice.count(1) >= 2:
			cat13_score = 17
		else:
			cat13_score = 0
	elif p.dice.count(4) >= 3:
		if p.dice.count(6) >= 2:
			cat13_score = 24
		elif p.dice.count(5) >= 2:
			cat13_score = 22
		elif p.dice.count(3) >= 2:
			cat13_score = 18	
		elif p.dice.count(2) >= 2:
			cat13_score = 16
		elif p.dice.count(1) >= 2:
			cat13_score = 14
		else:
			cat13_score = 0
	elif p.dice.count(3) >= 3:
		if p.dice.count(6) >= 2:
			cat13_score = 21
		elif p.dice.count(5) >= 2:
			cat13_score = 19
		elif p.dice.count(4) >= 2:
			cat13_score = 17	
		elif p.dice.count(2) >= 2:
			cat13_score = 13	
		elif p.dice.count(1) >= 2:
			cat13_score = 11
		else:
			cat13_score = 0
	elif p.dice.count(2) >= 3:
		if p.dice.count(6) >= 2:
			cat13_score = 18
		elif p.dice.count(5) >= 2:
			cat13_score = 16
		elif p.dice.count(4) >= 2:
			cat13_score = 14	
		elif p.dice.count(3) >= 2:
			cat13_score = 12	
		elif p.dice.count(1) >= 2:
			cat13_score = 8
		else:
			cat13_score = 0
	elif p.dice.count(1) >= 3:
		if p.dice.count(6) >= 2:
			cat13_score = 15
		elif p.dice.count(5) >= 2:
			cat13_score = 13
		elif p.dice.count(4) >= 2:
			cat13_score = 11	
		elif p.dice.count(3) >= 2:
			cat13_score = 9	
		elif p.dice.count(2) >= 2:
			cat13_score = 7
		else:
			cat13_score = 0		
	else:
		cat13_score = 0	
	print('\nYour score in round 13 is: '+str(cat13_score))
	p.score['Category13'] = cat13_score
	p.score['Total'] += cat13_score 			

	return p	

def Category14(p):
	print('\nRound 14: Chance')
	print('Try to get the dice to show as high of a total as possible')
	
	c = input('Press \'r\' to roll all dice: ')
	while c.lower() != 'r':
		c = input('Press \'r\' to roll all dice: ')

	for i in range(5):
		p.dice[i] = 0	
	keep_num = 0	
	# Roll 1	
	rolls = die_rolls(5)
	count = 1
	roll_save = []
	for i in rolls:
		print('Die '+str(count)+': '+str(i))
		roll_save.append(i)
		count += 1
	keep = input('Select the dice you want to keep (type in the die number separated by a space or enter to re-roll all): ')
	if len(keep) == 0:
		keep_dice = []
	else:
		keep_dice = [int(i) for i in keep.split(' ')]
	for i in keep_dice:
		p.dice[keep_num] = 	roll_save[i-1]
		keep_num += 1

	# Roll 2
	rolls = die_rolls(5-keep_num)
	count = 1
	roll_save = []
	for i in rolls:
		print('Die '+str(count)+': '+str(i))
		roll_save.append(i)
		count += 1
	keep = input('Select the dice you want to keep (type in the die number separated by a space or enter to re-roll all): ')
	if len(keep.strip()) == 0:
		keep_dice = []
	else:
		keep_dice = [int(i) for i in keep.strip().split(' ')]
	for i in keep_dice:
		p.dice[keep_num] = 	roll_save[i-1]
		keep_num += 1

	# Roll 3
	rolls = die_rolls(5-keep_num)
	count = 1
	for i in rolls:
		print('Die '+str(count)+': '+str(i))
		count += 1
		p.dice[keep_num] = i
		keep_num += 1
	
	cat14_score = 0
	for i in p.dice:
		cat14_score += i
	print('\nYour score in round 14 is: '+str(cat14_score))
	p.score['Category14'] = cat14_score
	p.score['Total'] += cat14_score 			

	return p

def Category15(p):
	print('\nRound 15: Yatzy')
	print('Try to get all dice showing the same number')
	
	c = input('Press \'r\' to roll all dice: ')
	while c.lower() != 'r':
		c = input('Press \'r\' to roll all dice: ')

	for i in range(5):
		p.dice[i] = 0	
	keep_num = 0	
	# Roll 1	
	rolls = die_rolls(5)
	count = 1
	roll_save = []
	for i in rolls:
		print('Die '+str(count)+': '+str(i))
		roll_save.append(i)
		count += 1
	keep = input('Select the dice you want to keep (type in the die number separated by a space or enter to re-roll all): ')
	if len(keep) == 0:
		keep_dice = []
	else:
		keep_dice = [int(i) for i in keep.split(' ')]
	for i in keep_dice:
		p.dice[keep_num] = 	roll_save[i-1]
		keep_num += 1

	# Roll 2
	rolls = die_rolls(5-keep_num)
	count = 1
	roll_save = []
	for i in rolls:
		print('Die '+str(count)+': '+str(i))
		roll_save.append(i)
		count += 1
	keep = input('Select the dice you want to keep (type in the die number separated by a space or enter to re-roll all): ')
	if len(keep.strip()) == 0:
		keep_dice = []
	else:
		keep_dice = [int(i) for i in keep.strip().split(' ')]
	for i in keep_dice:
		p.dice[keep_num] = 	roll_save[i-1]
		keep_num += 1

	# Roll 3
	rolls = die_rolls(5-keep_num)
	count = 1
	for i in rolls:
		print('Die '+str(count)+': '+str(i))
		count += 1
		p.dice[keep_num] = i
		keep_num += 1
	
	if p.dice.count(6) == 6:
		cat15_score = 50
	elif p.dice.count(5) == 6:
		cat15_score = 50
	elif p.dice.count(4) == 6:
		cat15_score = 50
	elif p.dice.count(3) == 6:
		cat15_score = 50
	elif p.dice.count(2) == 6:
		cat15_score = 50
	elif p.dice.count(1) == 6:
		cat15_score = 50
	else:
		cat15_score = 0	
	print('\nYour score in round 15 is: '+str(cat15_score))
	p.score['Category15'] = cat15_score
	p.score['Total'] += cat15_score 			

	return p	

Player = namedtuple('Player', 'name score dice')

print('\nWelcome to the game of Yatzy.\n')
players = []
player_name = input('Enter name of player: ')

while player_name.lower().strip() != 'start':
	p = Player(player_name, new_scorepad(), [0,0,0,0,0])
	players.append(p)
	player_name = input('Enter name of player: ')

if len(players) is 0:
	print('\nError: There should be atleast one player.\nExiting.')
	exit()

print('\nGood Luck. Have Fun.\n')

shuffle(players)

for i in range(len(players)):
	print('\nPlayer '+str(i+1)+': '+players[i].name)
	players[i] = Category1(players[i])
	players[i] = Category2(players[i])
	players[i] = Category3(players[i])
	players[i] = Category4(players[i])
	players[i] = Category5(players[i])
	players[i] = Category6(players[i])
	players[i] = Category7(players[i])
	players[i] = Category8(players[i])
	players[i] = Category9(players[i])
	players[i] = Category10(players[i])
	players[i] = Category11(players[i])
	players[i] = Category12(players[i])
	players[i] = Category13(players[i])
	players[i] = Category14(players[i])
	players[i] = Category15(players[i])
	print('\nYour total score is: '+str(players[i].score['Total'])+'\n')

zipped_pairs = zip([players[i].score['Total'] for i in range(len(players))], players)
z = [x for _, x in sorted(zipped_pairs)]
z.reverse()
print('Leaderboard\nName\t\tScore')
for i in z:
	print(i.name+'\t\t'+str(i.score['Total']))