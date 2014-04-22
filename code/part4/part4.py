import os
import re
import nltk
from nltk.corpus import wordnet as wn
import pickle

def makeFreqTable(arr):
	table = {}
	for word in arr:
		if word[0] not in table:
			table[word[0]] = 1
		else:
			table[word[0]] += 1
	return table

def parseQuery(query):

	text = nltk.word_tokenize(query)
	tagged = nltk.pos_tag(text)

	arr = []
	for word in tagged:
		if re.findall('NN.*',word[1]) or re.findall('VB.*',word[1]):
			arr.append(word)
	freqTable = {}
	freqTable = makeFreqTable(arr)
	return freqTable

def getMatchNum(query):
	
	for i in range(len(query)):
		if query[i+1] == 'match' or query[i+1] == 'Match' or query[i+1] == 'match,' or query[i+1] == 'Match,':
			if query[i] == 'first':
				return 1
			elif query[i] == 'second':
				return 2
			elif query[i] == 'third':
				return 3
			elif query[i] == 'fourth':
				return 4
			elif query[i] == 'fifth':
				return 5

def main():
	query = raw_input()

	freqQuery = {}
	freqQuery = parseQuery(query)

	q = query.split('?')[0]
	q = q.split(' ')
	matchNum = getMatchNum(q)

	freqComm1 = {}
	freqComm2 = {}
	addr1 = '../../data/match'+str(matchNum)+'/1comm.p'
	addr2 = '../../data/match'+str(matchNum)+'/2comm.p'
	comm1 = pickle.load(open(addr1,'rb')) 
	comm2 = pickle.load(open(addr2,'rb'))
	
	for ball in comm1:
		q = comm1[ball]['to']+comm1[ball]['from']+comm1[ball]['what']+comm1[ball]['why']
		freqComm1[ball] = parseQuery(q)
	for ball in comm2:
		q = comm2[ball]['to']+comm2[ball]['from']+comm2[ball]['what']+comm2[ball]['why']
		freqComm2[ball] = parseQuery(q)

	best = 0
	fl = 0
	answer = ''
	for ball in freqComm1:
		count = 0
		for word in freqQuery:
			for m in freqComm1[ball]:
				simil = []
				syns = wn.synsets(m)
				for s in syns:
					for l in s.lemmas:
						simil.append(l.name)
				if word.lower() in simil:
					count += 1		
		if count > best:
			best = count
			answer = ball
			fl = 0
	
	for ball in freqComm2:
		count = 0
		for word in freqQuery:
			for m in freqComm2[ball]:
				simil = []
				syns = wn.synsets(m)
				for s in syns:
					for l in s.lemmas:
						simil.append(l.name)
				if word.lower() in simil:
					count += 1		
		if count > best:
			best = count
			answer = ball
			fl = 1

	if fl == 0:
		print freqComm1[answer]
	else:
		print freqComm2[answer]
if __name__ == '__main__':
	main()
