import os
import sys
import re
def bowled799(bowl1, play):
        ans = []
        for i in play:
                temp1 = [0, 0, 0, 0, 0, 0]
                if i in bowl1:
                        temp1 = bowl1[i]
                        if (float(temp1[4]) > 8.01):
                                ans.append(i)
        return ans


def bowled7(bowl1, play):
        ans = []
        for i in play:
                temp1 = [0, 0, 0, 0, 0, 0]
                if i in bowl1:
                        temp1 = bowl1[i]
                        if (float(temp1[0]) > 7):
                                ans.append(i)
        return ans


def nowick0(bowl1, play):
        ans = []
        for i in play:
                temp1 = [0, 0, 0, 0, 0, 0]
                if i in bowl1:
                        temp1 = bowl1[i]
                        if (int(temp1[3]) == 0):
                                ans.append(i)
        return ans

def score50(bat1, play):
    ans = []
    for i in play:
        temp1 = [-1, -1, -1, -1, -1, -1]
        if i in bat1:
            temp1 = bat1[i]
            if int(temp1[1]) >= 50:
                    ans.append(i)
    return ans

def nowick(bowl1, play):
        ans = []
        for i in play:
                temp1 = [0, 0, 0, 0, 0, 0]
                if i in bowl1:
                        temp1 = bowl1[i]
                        if (int(temp1[3]) > 0):
                                ans.append(i)
        return ans

def parse_for_sr(bat1, play, num):
    ans = []
    for i in play:
        temp = [0, 0, 0, 0, 0, 0, 0]
        if i in bat1:
            temp = bat1[i]
        k = float(temp[6])
        if k < num:
            ans.append(i)
    return ans

def score100(bat1, play):
    toreturn = []
    for i in play:
        temp1 = [-1, -1, -1, -1, -1, -1]
        if i in bat1:
            temp1 = bat1[i]
            if int(temp1[1]) >= 100:
                    toreturn.append(i)
    return toreturn

def boundry(bat1, play):
    c2 = []
    for i in play:
        temp = [-1, -1, -1, -1, -1, -1]
        if i in bat1:
                temp = bat1[i]
        if (int(temp[4]) > 0):
                c2.append(i)
    return c2

def sr(bat1, play, num):
    ans = []
    for i in play:
        temp = [0, 0, 0, 0, 0, 0, 0]
        if i in bat1:
            temp = bat1[i]
        k = float(temp[6])
        if k > num:
            ans.append(i)
    return ans

def six(bat, play):
    ans = []
    for i in play:
        temp = [-1, -1, -1, -1, -1, -1]
        if i in bat:
            temp = bat[i]
        n4 = float(temp[4])
        n6 = float(temp[5])
        if n6 > n4:
            ans.append(i)
    return ans

def score100(bat1, play):
    toreturn = []
    for i in play:
        temp1 = [-1, -1, -1, -1, -1, -1]
        if i in bat1:
            temp1 = bat1[i]
            if int(temp1[1]) >= 100:
                    toreturn.append(i)
    return toreturn

def duck(bat1, play):
    c2 = []
    for i in play:
        temp = [-1, -1, -1, -1, -1, -1]
        if i in bat1:
                temp = bat1[i]
        if (int(temp[1]) == 0):
                c2.append(i)
    return c2



def add_to_dict(dictionary, fname):
	f = open(fname, 'r')
	for line in f:
		temp = line[:-1]
		temp = temp.split(',')
		a = temp[0]
		b = temp[1:]
		if a not in dictionary:
			dictionary[a] = b

def getdetails():
    details = []
    f = open('details.txt', 'r')
    i = 0
    for line in f:
        temp = line[:-1]
        temp = temp.split(' ')
        if (i == 0):
            if ('Match' in temp[0]):
                details.append(['Tie'])
            elif ('New' in temp[0]):
                details.append([temp[0]+' '+temp[1]])
            else:
                details.append([temp[0]])
        elif i == 1:
            details.append([temp[0] + temp[1]])
            if ('New' in temp[2]):
                details.append(['New Zealand'])
            elif('India' in temp[2]):
                details.append(['India'])
        i += 1
    return details

def listplayers(fname):
    play = []
    f = open(fname, 'r')
    for line in f:
        temp = line[:-1]
        temp = temp.split(',')
        a = temp[0]
        a = a.split('\t')
        if a[0] not in play:
            play.append(a[0])
    return play

def parse_for_played(play, bat, bowl,k):
    arr = set()
    for i in bat:
        arr.add(i)
    for i in bowl:
        arr.add(i)
    play.append(arr)

def get_wides(wides, players, bowl):
    for j in players:
        for i in bowl:
            try:
                temp = i[-1][5][1]
            except IndexError:
                continue
            if (j == i[0]):
                wides[j] += int(temp)

def number_wides(more, players,wides):
    for i in players:
        if i == 'I Sharma':
            catch1 = wides[i]
        else:
            catch2 = wides[i]

    if (catch1 > catch2):
        more.append('I Sharma')
    else:
        more.append('RA Jadeja')

def get_catches(catch, players, bat):
    for j in players:
        for i in bat:
            temp = i[1][0]
            if ( j in temp.split(' ')[1] and temp[0]=='c'):
                print temp
                catch[j] += 1

def number_catches(more, catch):
    for i in catch:
        if i == 'Southee':
            catch1 = catch[i]
        else:
            catch2 = catch[i]

    if (catch1 > catch2):
        more.append('Southee')
    else:
        more.append('None')

def get_nummom(nummom, mom, bat):
    for i in mom:
        nummom[i] += 1

def number_momatch(ans, nummom):
    flag = 0
    for i in nummom:
        if (nummom[i] > 1):
            ans.append(i)

def economy(value):
    if value <= 4:
        return 20
    elif value == 5:
        return 15
    elif value == 6:
        return 10
    else:
        return 2

def maidens(value):
    if value >= 2:
        return 10
    elif value == 1:
        return 5
    else:
        return 1

def wickets(value):
    return value*3

def evaluate_final(out, array):
    final = 0
    m = -1000
    for i in range(len(array)):
        temp = array[i]
        final += maidens(float(temp[0]))
        final += wickets(float(temp[2]))
        final += economy(float(temp[3]))
        if final > m:
            m = final
        final = 0
    out.append(m)

def check_for_better(out, stats, inn, arr0):
    arr1 = []
    arr2 = []
    for i in arr0:
        if i == inn[0]:
            arr1.append(arr0[i])
        else:
            arr2.append(arr0[i])
    evaluate_final(out, arr1)
    evaluate_final(out, arr2)

def get_better_inning(out, inn):
    if out[0] > out[1]:
        return inn[0]
    return inn[1]

import math
def strikerate(value):
        return float(2*value/math.sqrt(value))
def sixes(value):
	return value*1.5
def fours(value):
	return value*1.2

def dots(value):
	runs = float(value[1])
	balls = float(value[3])
	four = float(value[4])
	six = float(value[5])
	#Approx dot balls
        dots = balls - ((four + six) + 0.7*(runs - (4*four + 6*six)))
	return ((dots)/balls)*100

def parse_for_hitting(hitting, bat, k):
	final = 0
	for i in bat:
		if 'MS Dhoni' in i:
			temp = bat[i]
			final += strikerate(float(temp[6]))
			final += sixes(float(temp[5]))
			final += fours(float(temp[5]))
			final -= dots(temp)/2
	hitting[k] = final
