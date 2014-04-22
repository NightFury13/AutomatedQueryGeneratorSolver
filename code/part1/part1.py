#########################
# Author : Mohit Jain	#
# RollNo : 201202164	#
#########################

import nltk
import sys
import pickle

def add_to_dict(dictionary, fname):
	f = open(fname, 'r')
	for line in f:
		temp = line[:-1]
		temp = temp.split(',')
		a = temp[0]
		b = temp[1:]
		if a not in dictionary:
			dictionary[a] = b

def solveQuery(matNum, player, lookfor, score, question, maxim):
		
	bat_in1 = {}
	bat_in2 = {}
	bowl_in1 = {}
	bowl_in2 = {}

	bat1 = '../../data/match'+str(matNum)+'/inn1_bat.txt'
	bat2 = '../../data/match'+str(matNum)+'/inn2_bat.txt'
	bowl1 = '../../data/match'+str(matNum)+'/inn1_bowl.txt'
	bowl2 = '../../data/match'+str(matNum)+'/inn2_bowl.txt'

	add_to_dict(bat_in1, bat1)
	add_to_dict(bat_in2, bat2)
	add_to_dict(bowl_in1, bowl1)
	add_to_dict(bowl_in2, bowl2)
	
	c1 = '../../data/match'+str(matNum)+'/1comm.p'
	c2 = '../../data/match'+str(matNum)+'/2comm.p'

	com1 = pickle.load(open(c1,'rb'))		
	com2 = pickle.load(open(c2,'rb'))		

	answer = []
	
	if question == 'which over':
		if lookfor[0] == 'out':
			if player in bat_in1:
				for ball in com1:
					if com1[ball]['to'].lower() in player.lower():
						if com1[ball]['what'] == 'OUT':
							answer.append(int(float(ball)))
			if player in bat_in2:
				for ball in com2:
					if com2[ball]['to'].lower() in player.lower():
						if com2[ball]['what'] == 'OUT':
							answer.append(float(ball))
		if lookfor[0] == 'hit':
			if len(lookfor) == 1:
				if score == 1:
					if player in bat_in1:
						if maxim == 0:
							for ball in com1:
								if com1[ball]['to'].lower() in player.lower():
									if com1[ball]['what']=='1 run':
										answer.append(int(float(ball)))
						if maxim == 1:
							maxHit = []
							maxHit.append(0)
							maxHit.append(0)
							prevOv = 0
							val = 0
							for ball in com1:
								if com1[ball]['to'].lower() in player.lower():
									if com1[ball]['what']=='1 run':
										if int(float(ball)) == prevOv:
											val += 1
										else:
											if val>maxHit[1]:
												maxHit[1] = val
												maxHit[0] = prevOv
											prevOv = int(float(ball))
											val = 1
							answer.append(maxHit[0])
						if maxim == -1:
							minHit = []
							minHit.append(0)
							minHit.append(100)
							prevOv = 0
							val = 0
							for ball in com1:
								if com1[ball]['to'].lower() in player.lower():
									if com1[ball]['what']=='1 run':
										if int(float(ball)) == prevOv:
											val += 1
										else:
											if val<minHit[1]:
												minHit[1] = val
												minHit[0] = prevOv
											prevOv = int(float(ball))
											val = 1
							answer.append(minHit[0])
					if player in bat_in2:
						if maxim == 0:
							for ball in com2:
								if com2[ball]['to'].lower() in player.lower():
									if com2[ball]['what']=='1 run':
										answer.append(int(float(ball)))
						if maxim == 1:
							maxHit = []
							maxHit.append(0)
							maxHit.append(0)
							prevOv = 0
							val = 0
							for ball in com2:
								if com2[ball]['to'].lower() in player.lower():
									if com2[ball]['what']=='1 run':
										if int(float(ball)) == prevOv:
											val += 1
										else:
											if val>maxHit[1]:
												maxHit[1] = val
												maxHit[0] = prevOv
											prevOv = int(float(ball))
											val = 1
							answer.append(maxHit[0])
						if maxim == -1:
							minHit = []
							minHit.append(0)
							minHit.append(100)
							prevOv = 0
							val = 0
							for ball in com2:
								if com2[ball]['to'].lower() in player.lower():
									if com2[ball]['what']=='1 run':
										if int(float(ball)) == prevOv:
											val += 1
										else:
											if val<minHit[1]:
												minHit[1] = val
												minHit[0] = prevOv
											prevOv = int(float(ball))
											val = 1
							answer.append(minHit[0])
				if score == 2:
					if player in bat_in1:
						if maxim == 0:
							for ball in com1:
								if com1[ball]['to'].lower() in player.lower():
									if com1[ball]['what']=='2 run':
										answer.append(int(float(ball)))
						if maxim == 1:
							maxHit = []
							maxHit.append(0)
							maxHit.append(0)
							prevOv = 0
							val = 0
							for ball in com1:
								if com1[ball]['to'].lower() in player.lower():
									if com1[ball]['what']=='2 run':
										if int(float(ball)) == prevOv:
											val += 1
										else:
											if val>maxHit[1]:
												maxHit[1] = val
												maxHit[0] = prevOv
											prevOv = int(float(ball))
											val = 1
							answer.append(maxHit[0])
						if maxim == -1:
							minHit = []
							minHit.append(0)
							minHit.append(100)
							prevOv = 0
							val = 0
							for ball in com1:
								if com1[ball]['to'].lower() in player.lower():
									if com1[ball]['what']=='2 run':
										if int(float(ball)) == prevOv:
											val += 1
										else:
											if val<minHit[1]:
												minHit[1] = val
												minHit[0] = prevOv
											prevOv = int(float(ball))
											val = 1
							answer.append(minHit[0])
					if player in bat_in2:
						if maxim == 0:
							for ball in com2:
								if com2[ball]['to'].lower() in player.lower():
									if com2[ball]['what']=='2 run':
										answer.append(int(float(ball)))
						if maxim == 1:
							maxHit = []
							maxHit.append(0)
							maxHit.append(0)
							prevOv = 0
							val = 0
							for ball in com2:
								if com2[ball]['to'].lower() in player.lower():
									if com2[ball]['what']=='2 run':
										if int(float(ball)) == prevOv:
											val += 1
										else:
											if val>maxHit[1]:
												maxHit[1] = val
												maxHit[0] = prevOv
											prevOv = int(float(ball))
											val = 1
							answer.append(maxHit[0])
						if maxim == -1:
							minHit = []
							minHit.append(0)
							minHit.append(100)
							prevOv = 0
							val = 0
							for ball in com2:
								if com2[ball]['to'].lower() in player.lower():
									if com2[ball]['what']=='2 run':
										if int(float(ball)) == prevOv:
											val += 1
										else:
											if val<minHit[1]:
												minHit[1] = val
												minHit[0] = prevOv
											prevOv = int(float(ball))
											val = 1
							answer.append(minHit[0])
				if score == 3:
					if player in bat_in1:
						if maxim == 0:
							for ball in com1:
								if com1[ball]['to'].lower() in player.lower():
									if com1[ball]['what']=='3 run':
										answer.append(int(float(ball)))
						if maxim == 1:
							maxHit = []
							maxHit.append(0)
							maxHit.append(0)
							prevOv = 0
							val = 0
							for ball in com1:
								if com1[ball]['to'].lower() in player.lower():
									if com1[ball]['what']=='3 run':
										if int(float(ball)) == prevOv:
											val += 1
										else:
											if val>maxHit[1]:
												maxHit[1] = val
												maxHit[0] = prevOv
											prevOv = int(float(ball))
											val = 1
							answer.append(maxHit[0])
						if maxim == -1:
							minHit = []
							minHit.append(0)
							minHit.append(100)
							prevOv = 0
							val = 0
							for ball in com1:
								if com1[ball]['to'].lower() in player.lower():
									if com1[ball]['what']=='3 run':
										if int(float(ball)) == prevOv:
											val += 1
										else:
											if val<minHit[1]:
												minHit[1] = val
												minHit[0] = prevOv
											prevOv = int(float(ball))
											val = 1
							answer.append(minHit[0])
					if player in bat_in2:
						if maxim == 0:
							for ball in com2:
								if com2[ball]['to'].lower() in player.lower():
									if com2[ball]['what']=='3 run':
										answer.append(int(float(ball)))
						if maxim == 1:
							maxHit = []
							maxHit.append(0)
							maxHit.append(0)
							prevOv = 0
							val = 0
							for ball in com2:
								if com2[ball]['to'].lower() in player.lower():
									if com2[ball]['what']=='3 run':
										if int(float(ball)) == prevOv:
											val += 1
										else:
											if val>maxHit[1]:
												maxHit[1] = val
												maxHit[0] = prevOv
											prevOv = int(float(ball))
											val = 1
							answer.append(maxHit[0])
						if maxim == -1:
							minHit = []
							minHit.append(0)
							minHit.append(100)
							prevOv = 0
							val = 0
							for ball in com2:
								if com2[ball]['to'].lower() in player.lower():
									if com2[ball]['what']=='3 run':
										if int(float(ball)) == prevOv:
											val += 1
										else:
											if val<minHit[1]:
												minHit[1] = val
												minHit[0] = prevOv
											prevOv = int(float(ball))
											val = 1
							answer.append(minHit[0])
				if score == 4:
					if player in bat_in1:
						if maxim == 0:
							for ball in com1:
								if com1[ball]['to'].lower() in player.lower():
									if com1[ball]['what']=='4 run':
										answer.append(int(float(ball)))
						if maxim == 1:
							maxHit = []
							maxHit.append(0)
							maxHit.append(0)
							prevOv = 0
							val = 0
							for ball in com1:
								if com1[ball]['to'].lower() in player.lower():
									if com1[ball]['what']=='4 run':
										if int(float(ball)) == prevOv:
											val += 1
										else:
											print prevOv
											if val>maxHit[1]:
												print val
												maxHit[1] = val
												maxHit[0] = prevOv
											prevOv = int(float(ball))
											val = 1
							answer.append(maxHit[0])
						if maxim == -1:
							minHit = []
							minHit.append(0)
							minHit.append(100)
							prevOv = 0
							val = 0
							for ball in com1:
								if com1[ball]['to'].lower() in player.lower():
									if com1[ball]['what']=='4 run':
										if int(float(ball)) == prevOv:
											val += 1
										else:
											if val<minHit[1]:
												minHit[1] = val
												minHit[0] = prevOv
											prevOv = int(float(ball))
											val = 1
							answer.append(minHit[0])
					if player in bat_in2:
						if maxim == 0:
							for ball in com2:
								if com2[ball]['to'].lower() in player.lower():
									if com2[ball]['what']=='4 run':
										answer.append(int(float(ball)))
						if maxim == 1:
							maxHit = []
							maxHit.append(0)
							maxHit.append(0)
							prevOv = 0
							val = 0
							for ball in com2:
								if com2[ball]['to'].lower() in player.lower():
									if com2[ball]['what']=='4 run':
										if int(float(ball)) == prevOv:
											val += 1
										else:
											if val>maxHit[1]:
												maxHit[1] = val
												maxHit[0] = prevOv
											prevOv = int(float(ball))
											val = 1
							answer.append(maxHit[0])
						if maxim == -1:
							minHit = []
							minHit.append(0)
							minHit.append(100)
							prevOv = 0
							val = 0
							for ball in com2:
								if com2[ball]['to'].lower() in player.lower():
									if com2[ball]['what']=='4 run':
										if int(float(ball)) == prevOv:
											val += 1
										else:
											if val<minHit[1]:
												minHit[1] = val
												minHit[0] = prevOv
											prevOv = int(float(ball))
											val = 1
							answer.append(minHit[0])
				if score == 6:
					if player in bat_in1:
						if maxim == 0:
							for ball in com1:
								if com1[ball]['to'].lower() in player.lower():
									if com1[ball]['what']=='6 run':
										answer.append(int(float(ball)))
						if maxim == 1:
							maxHit = []
							maxHit.append(0)
							maxHit.append(0)
							prevOv = 0
							val = 0
							for ball in com1:
								if com1[ball]['to'].lower() in player.lower():
									if com1[ball]['what']=='6 run':
										if int(float(ball)) == prevOv:
											val += 1
										else:
											if val>maxHit[1]:
												maxHit[1] = val
												maxHit[0] = prevOv
											prevOv = int(float(ball))
											val = 1
							answer.append(maxHit[0])
						if maxim == -1:
							minHit = []
							minHit.append(0)
							minHit.append(100)
							prevOv = 0
							val = 0
							for ball in com1:
								if com1[ball]['to'].lower() in player.lower():
									if com1[ball]['what']=='6 run':
										if int(float(ball)) == prevOv:
											val += 1
										else:
											if val<minHit[1]:
												minHit[1] = val
												minHit[0] = prevOv
											prevOv = int(float(ball))
											val = 1
							answer.append(minHit[0])
					if player in bat_in2:
						if maxim == 0:
							for ball in com2:
								if com2[ball]['to'].lower() in player.lower():
									if com2[ball]['what']=='6 run':
										answer.append(int(float(ball)))
						if maxim == 1:
							maxHit = []
							maxHit.append(0)
							maxHit.append(0)
							prevOv = 0
							val = 0
							for ball in com2:
								if com2[ball]['to'].lower() in player.lower():
									if com2[ball]['what']=='6 run':
										if int(float(ball)) == prevOv:
											val += 1
										else:
											if val>maxHit[1]:
												maxHit[1] = val
												maxHit[0] = prevOv
											prevOv = int(float(ball))
											val = 1
							answer.append(maxHit[0])
						if maxim == -1:
							minHit = []
							minHit.append(0)
							minHit.append(100)
							prevOv = 0
							val = 0
							for ball in com2:
								if com2[ball]['to'].lower() in player.lower():
									if com2[ball]['what']=='6 run':
										if int(float(ball)) == prevOv:
											val += 1
										else:
											if val<minHit[1]:
												minHit[1] = val
												minHit[0] = prevOv
											prevOv = int(float(ball))
											val = 1
							answer.append(minHit[0])
		if lookfor[0] == 'wide':
			if len(lookfor) == 1:
				if player in bowl_in1:
					val = 0
					prevOv = 0
					if maxim == 0:
						for ball in com1:
							if com1[ball]['from'].lower() in player.lower():
								if com1[ball]['what']=='1 wide' or com1[ball]['what']=='2 wides' or com1[ball]['what']=='5 wides':
									if int(float(ball)) == prevOv:
										val +=1
									else:
										if val == score:
											answer.append(prevOv)
										elif val>0 and score == 0:
											answer.append(prevOv)
										prevOv = int(float(ball))
										val = 1
					if maxim == 1:
						maxWide = []
						maxWide.append(0)
						maxWide.append(0)
						for ball in com1:
							if com1[ball]['from'].lower() in player.lower():
								if com1[ball]['what']=='1 wide' or com1[ball]['what']=='2 wides' or com1[ball]['what']=='5 wides':
									if int(float(ball)) == prevOv:
										val += 1
									else:
										if val>maxWide[1]:
											maxWide[1] = val
											maxWide[0] = prevOv
										prevOv = int(float(ball))
										val = 1
						answer.append(maxWide[0])
					if maxim == -1:
						minWide = []
						minWide.append(0)
						minWide.append(100)
						for ball in com1:
							if com1[ball]['from'].lower() in player.lower():
								if com1[ball]['what']=='1 wide' or com1[ball]['what']=='2 wides' or com1[ball]['what']=='5 wides':
									if int(float(ball)) == prevOv:
										val += 1
									else:
										if val<minWide[1]:
											minWide[1] = val
											minWide[0] = prevOv
										prevOv = int(float(ball))
										val = 1
						answer.append(minWide[0])
				if player in bowl_in2:
					val = 0
					prevOv = 0
					if maxim == 0:
						for ball in com2:
							if com2[ball]['from'].lower() in player.lower():
								if com2[ball]['what']=='1 wide' or com2[ball]['what']=='2 wides' or com2[ball]['what']=='5 wides':
									if int(float(ball)) == prevOv:
										val +=1
									else:
										if val == score:
											answer.append(prevOv)
										elif val>0 and score == 0:
											answer.append(prevOv)
										prevOv = int(float(ball))
										val = 1
					if maxim == 1:
						maxWide = []
						maxWide.append(0)
						maxWide.append(0)
						for ball in com2:
							if com2[ball]['from'].lower() in player.lower():
								if com2[ball]['what']=='1 wide' or com2[ball]['what']=='2 wides' or com2[ball]['what']=='5 wides':
									if int(float(ball)) == prevOv:
										val += 1
									else:
										if val>=maxWide[1]:
											maxWide[1] = val
											maxWide[0] = prevOv
											answer.append(maxWide[0])
										prevOv = int(float(ball))
										val = 1
					if maxim == -1:
						minWide = []
						minWide.append(0)
						minWide.append(100)
						for ball in com2:
							if com2[ball]['from'].lower() in player.lower():
								if com2[ball]['what']=='1 wide' or com2[ball]['what']=='2 wides' or com2[ball]['what']=='5 wides':
									if int(float(ball)) == prevOv:
										val += 1
									else:
										if val<minWide[1]:
											minWide[1] = val
											minWide[0] = prevOv
										prevOv = int(float(ball))
										val = 1
						answer.append(minWide[0])
		  
	elif question == 'which ball':
		if lookfor[0] == 'out':
			if player in bat_in1:
				for ball in com1:
					if com1[ball]['to'].lower() in player.lower():
						if com1[ball]['what'] == 'OUT':
							answer.append(float(ball))
			if player in bat_in2:
				for ball in com2:
					if com2[ball]['to'].lower() in player.lower():
						if com2[ball]['what'] == 'OUT':
							answer.append(float(ball))
		if lookfor[0] == 'hit':
			if len(lookfor) == 1:
				if score == 1:
					if player in bat_in1:
						for ball in com1:
							if com1[ball]['to'].lower() in player.lower():
								if com1[ball]['what']=='1 run':
									answer.append(float(ball))
					if player in bat_in2:
						for ball in com2:
							if com2[ball]['to'].lower() in player.lower():
								if com2[ball]['what']=='1 run':
									answer.append(float(ball))
				if score == 2:
					if player in bat_in1:
						for ball in com1:
							if com1[ball]['to'].lower() in player.lower():
								if com1[ball]['what']=='2 run':
									answer.append(float(ball))
					if player in bat_in2:
						for ball in com2:
							if com2[ball]['to'].lower() in player.lower():
								if com2[ball]['what']=='2 run':
									answer.append(float(ball))
				if score == 3:
					if player in bat_in1:
						for ball in com1:
							if com1[ball]['to'].lower() in player.lower():
								if com1[ball]['what']=='3 run':
									answer.append(float(ball))
					if player in bat_in2:
						for ball in com2:
							if com2[ball]['to'].lower() in player.lower():
								if com2[ball]['what']=='3 run':
									answer.append(float(ball))
				if score == 4:
					if player in bat_in1:
						for ball in com1:
							if com1[ball]['to'].lower() in player.lower():
								if com1[ball]['what']=='4 run':
									answer.append(float(ball))
					if player in bat_in2:
						for ball in com2:
							if com2[ball]['to'].lower() in player.lower():
								if com2[ball]['what']=='4 run':
									answer.append(float(ball))
				if score == 6:
					if player in bat_in1:
						for ball in com1:
							if com1[ball]['to'].lower() in player.lower():
								if com1[ball]['what']=='6 run':
									answer.append(float(ball))
					if player in bat_in2:
						for ball in com2:
							if com2[ball]['to'].lower() in player.lower():
								if com2[ball]['what']=='6 run':
									answer.append(float(ball))
			elif len(lookfor) == 3:
				if lookfor[1] == 'over':
					over = str(lookfor[2])
					arr = [over+'.1',over+'.2',over+'.3',over+'.4',over+'.5',over+'.6']
					if score == 1:
						if player in bat_in1:
							for ball in arr:
								if com1[ball]['to'].lower() in player.lower():
									if com1[ball]['what']=='1 run':
										answer.append(float(ball))
						if player in bat_in2:
							for ball in arr:
								if com2[ball]['to'].lower() in player.lower():
									if com2[ball]['what']=='1 run':
										answer.append(float(ball))
					if score == 2:
						if player in bat_in1:
							for ball in arr:
								if com1[ball]['to'].lower() in player.lower():
									if com1[ball]['what']=='2 run':
										answer.append(float(ball))
						if player in bat_in2:
							for ball in arr:
								if com2[ball]['to'].lower() in player.lower():
									if com2[ball]['what']=='2 run':
										answer.append(float(ball))
					if score == 3:
						if player in bat_in1:
							for ball in arr:
								if com1[ball]['to'].lower() in player.lower():
									if com1[ball]['what']=='3 run':
										answer.append(float(ball))
						if player in bat_in2:
							for ball in arr:
								if com2[ball]['to'].lower() in player.lower():
									if com2[ball]['what']=='3 run':
										answer.append(float(ball))
					if score == 4:
						if player in bat_in1:
							for ball in arr:
								if com1[ball]['to'].lower() in player.lower():
									if com1[ball]['what']=='4 run':
										answer.append(float(ball))
						if player in bat_in2:
							for ball in arr:
								if com2[ball]['to'].lower() in player.lower():
									if com2[ball]['what']=='4 run':
										answer.append(float(ball))
					if score == 6:
						if player in bat_in1:
							for ball in arr:
								if com1[ball]['to'].lower() in player.lower():
									if com1[ball]['what']=='6 run':
										answer.append(float(ball))
						if player in bat_in2:
							for ball in arr:
								if com2[ball]['to'].lower() in player.lower():
									if com2[ball]['what']=='6 run':
										answer.append(float(ball))
		if lookfor[0] == 'wide':
			if len(lookfor) == 3:
				if lookfor[1] == 'over':
					over = str(lookfor[2])
					arr = [over+'.1',over+'.2',over+'.3',over+'.4',over+'.5',over+'.6']
					if player in bowl_in1:
						for ball in arr:
							if com1[ball]['from'].lower() in player.lower():
								if com1[ball]['what']=='1 wide' or com1[ball]['what']=='2 wides' or com1[ball]['what']=='5 wides':
									answer.append(float(ball))
					if player in bowl_in2:
						for ball in arr:
							if com2[ball]['from'].lower() in player.lower():
								if com2[ball]['what']=='1 wide' or com2[ball]['what']=='2 wides' or com2[ball]['what']=='5 wides':
									answer.append(float(ball))
#################################################	
#Batsman
################################################# 
	elif question == 'which bowler':
		if lookfor[0] == 'hit':
			if len(lookfor) == 1:
				if player in bat_in1:
					for ball in com1:
						if com1[ball]['to'].lower() in player.lower():
							check = ''
							if score == 1:
								check = '1 run'
							elif score == 2:
								check = '2 run'
							elif score == 3:
								check = '3 run'
							elif score == 4:
								check = '4 run'
							elif score == 5:
								check = '5 run'
							elif score == 6:
								check = '6 run'
							if com1[ball]['what']==check:
								answer.append(com1[ball]['from'])
				if player in bat_in2:
					for ball in com2:
						if com2[ball]['to'].lower() in player.lower():
							check = ''
							if score == 1:
								check = '1 run'
							elif score == 2:
								check = '2 run'
							elif score == 3:
								check = '3 run'
							elif score == 4:
								check = '4 run'
							elif score == 5:
								check = '5 run'
							elif score == 6:
								check = '6 run'
							if com2[ball]['what']==check:
								answer.append(com2[ball]['from'])
		if lookfor[0] == 'out':
			if player in bat_in1:
				for ball in com1:
					if com1[ball]['to'].lower() in player.lower():
						if com1[ball]['what'] == 'out':
							answer.append(com1[ball]['from'])
			if player in bat_in2:
				for ball in com2:
					if com2[ball]['to'].lower() in player.lower():
						if com2[ball]['what'] == 'OUT':
							answer.append(com2[ball]['from'])
	if len(answer)==0:
		print "None"
	else:
		print answer

def parseQuery(query):

	query = query.split(' ')

	matNum = 0
	for num in query:
		if num == 'first':
			matNum = 1
			break
		elif num == 'second':
			matNum = 2
			break
		elif num == 'third':
			matNum = 3
			break
		elif num == 'fourth':
			matNum = 4
			break
		elif num == 'fifth':
			matNum = 5
			break
	
	bat_in1 = {}
	bat_in2 = {}
	bowl_in1 = {}
	bowl_in2 = {}

	if matNum is not 0:
		bat1 = '../../data/match'+str(matNum)+'/inn1_bat.txt'
		bat2 = '../../data/match'+str(matNum)+'/inn2_bat.txt'
		bowl1 = '../../data/match'+str(matNum)+'/inn1_bowl.txt'
		bowl2 = '../../data/match'+str(matNum)+'/inn2_bowl.txt'

		add_to_dict(bat_in1, bat1)
		add_to_dict(bat_in2, bat2)
		add_to_dict(bowl_in1, bowl1)
		add_to_dict(bowl_in2, bowl2)

	else:
		print "# There were only 5 matches played. :/"
		return -1

	player = ''
	for pl in query:
		if len(pl)>=4:
			for i in bat_in1.keys():
				if pl in str(i):
					player = i
					break
			for i in bat_in2.keys():
				if pl in str(i):
					player = i
					break
			for i in bowl_in1.keys():
				if pl in str(i):
					player = i
					break
			for i in bowl_in2.keys():
				if pl in str(i):
					player = i
					break
	if player == '':
		print "# Are you sure that's a player? :/"
		return -1


	lookfor = []
	score = 0
	maxim = 0
	for desc in query:
		if desc == 'hit' or desc == 'hits':
			lookfor.append('hit')
			for sc in query:
				if ((sc=='one')or(sc=='ones')):
					score = 1
					break
				if ((sc=='two')or(sc=='twos')):
					score = 2
					break
				if ((sc=='three')or(sc=='threes')):
					score = 3
					break
				if ((sc=='four')or(sc=='fours')):
					score = 4
					break
				if ((sc=='six')or(sc=='sixes')):
					score = 6
					break
				try:
					score = int(sc)
					break
				except:
					score = score
					#kuch nahi
		if desc == 'wides' or desc == 'wide':
			lookfor.append('wide')
			for sc in query:
				if (sc=='one'):
					score = 1
					break
				if (sc=='two'):
					score = 2
					break
				if (sc == 'three'):
					score = 3
					break
				if (sc == 'four'):
					score = 4
					break
				if (sc == 'five'):
					score = 5
					break
				if (sc == 'six'):
					score = 6
					break
				try:
					score = int(sc)
					break
				except:
					score = score
					#kuch nahi
		if desc == 'noball' or desc == 'no-ball':
			lookfor.append('noball')
			for sc in query:
				if (sc=='one'):
					score = 1
					break
				if (sc=='two'):
					score = 2
					break
				if (sc == 'three'):
					score = 3
					break
				if (sc == 'four'):
					score = 4
					break
				if (sc == 'five'):
					score = 5
					break
				if (sc == 'six'):
					score = 6
					break
				try:
					score = int(sc)
					break
				except:
					score = score
					#kuch nahi
		if desc == 'over':				#this cannot be the last word, that will be over with a "?".
			for i in range(len(query)):
				if query[i] == desc:
					lookfor.append('over')
					lookfor.append(int(float(query[i+1])))
		if desc == 'out':
			lookfor.append('out')
		if desc == 'maximum' or desc == 'max':
			maxim = 1
		if desc == 'minimum' or desc == 'min':
			maxim = -1

	if lookfor[0] == '':
		print "# I dont get what you say... :/"
		return -1
	
	question = ''
	for i in range(len(query)):
		if query[i]=='which':
			if query[i+1]=='ball?' or query[i+1]=='balls?':
				question = 'which ball'
				break
			elif query[i+1]=='over?' or query[i+1]=='overs?':
				question = 'which over'
				break
			elif query[i+1]=='bowler?' or query[i+1]=='bowlers?':
				question = 'which bowler'
				break
			elif query[i+1]=='batsman?' or query[i+1]=='batsmen?':
				question = 'which batsman'
				break
		if query[i]=='who':
			if query[i+1] == 'dismissed?':
				question = 'who dismissed'
				break
	if question == '':
		print "# Give me a domain to search in, which over/ball/batsman...etc :/"
		return -1

	if score>6 or (len(lookfor)==3 and score == lookfor[2]):
		score = 0

	print matNum, player,
	print lookfor[0], score,
	try:
		print lookfor[1], lookfor[2],
	except:
		pass
	print question

	solveQuery(matNum, player, lookfor, score, question, maxim)

def main():

	query = raw_input()

	temp = parseQuery(query)
	
	#unsuccesful query parse
	if temp == -1:
		return

if __name__ == "__main__":
	main()
