#This code deals with the Text processing part of question.
#The commentary is parsed and stored as a dict in .p files. Please see build.py for extraction and parsing of commentary
# Author: Devansh Shah
# 201256053

import re
import pickle
import os
from common import *
def getmatch(words):
    num = {"first":1,"fourth":4,"second":2,"third":3,"forth":4,"fifth":5}
    for i in range(len(words)):
        if words[i] in num:
            return num[words[i]]
    return 0

def getplayers(words,players):
    final = ""
    prev = 0
    for j in players:
            ans = ""
            ct = 0
            x = j.split(" ")
            for k in x:
                for i in range(len(words)):
                    if words[i].lower() == k.lower():
                        ans += k + " "
                        ct+=1
                        if ct>prev:
                            prev = ct
                            final = ans
    return final

def getquestion(words):
    if "which" in words:
        if "which over" in " ".join(words) or "which overs" in " ".join(words) or "which over(s)" in " ".join(words):
            return 2
        elif "which ball" in " ".join(words):
            return 1
        elif "bowler" in " ".join(words):
            return 5
    elif "who" in words:
        if "dismissed" in words:
            return 3
        elif "hit" in words:
            return 4

def ai(no,who,what,words):
    os.chdir("match"+str(no))
    inn1 = pickle.load(open(str(no)+"1comm.p","rb"))
    inn2 = pickle.load(open(str(no)+"2comm.p","rb"))
    over = -1
    if "over" in words:
        print words
        for i in words:
            try:
                over = int(i)
            except:
                pass
        over = str(over)
        if over != "-1":
         for i in inn1:
            if re.match(over+'\.*',i):
                pass
            else:
                inn1[i]['what'] = ""
                inn1[i]['to'] = ""
                inn1[i]['from'] = ""
                inn1[i]['why'] = ""
         for i in inn2:
            if re.match(over+'\.*',i):
                pass
            else:
                inn2[i]['what'] = ""
                inn2[i]['to'] = ""
                inn2[i]['from'] = ""
                inn2[i]['why'] = ""

    score = {"ones":1,"twos":2,"fours":4,"sixes":6,"threes":3,"four":4,"six":6,"wide":-1,"no ball": -2}

    if what == 3:
        for i in inn1:
            print inn1[i]['to']
            if inn1[i]['what'] == 'OUT' and inn1[i]['to'] in who:
                return inn1[i]["from"]
        for i in inn2:
            print inn2[i]['to'],
            print who
            if inn2[i]['what'] == 'OUT' and inn2[i]['to'] in who:
                return inn2[i]["from"]

    elif what == 1 or what == 2:
        for k in words:
            k = k.lower()
        for l in words:
            print l
            for j in score:
                if j == l:
                    ans = []
                    for i in inn1:
                        print str(score[j]) + ' run',
                        print inn1[i]['what']
                        if (str(score[j]) + ' run') in inn1[i]['what'].lower() and inn1[i]['to'] in who:
                            ans.append(inn1[i])
                    for i in inn2:
                        print str(score[j]) + ' run',
                        print inn2[i]['what'].lower()
                        if (str(score[j]) + ' run') in inn2[i]['what'].lower() and inn2[i]['to'] in who:
                            ans.append(inn2[i])
                    return ans
        if 'wicket' in words or 'out' in words:
            for i in inn1:
                if inn1[i]['what'] == 'OUT' and inn1[i]['to'] in who:
                    return i
            for i in inn2:
                if inn2[i]['what'] == 'OUT' and inn2[i]['to'] in who:
                    return i
    os.chdir("..")


def main():
    question = raw_input("Ask me a question: <info><description><question> format only ")
    parse = question.split(' ')
    playerprofile1 = "./player_profile/indian_players_profile.txt"
    playerprofile2 = "./player_profile/nz_players_profile.txt"
    indiaplayers = listplayers(playerprofile1)
    nzplayers = listplayers(playerprofile2)
    players = indiaplayers+nzplayers
    match = getmatch(parse)
    player = getplayers(parse,players)
    quest = getquestion(parse)
    print match
    print player
    print quest
    ans = ai(match,player,quest,parse)
    print ans

if __name__ == "__main__":
    main()
