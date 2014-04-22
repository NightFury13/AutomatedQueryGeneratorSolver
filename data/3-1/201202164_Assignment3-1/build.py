from bs4 import BeautifulSoup
import bs4
import urllib
import os
import pickle
import re
#Data URLs for this knowledge base
url = ["","http://www.espncricinfo.com/new-zealand-v-india-2014/engine/match/667641.html","http://www.espncricinfo.com/new-zealand-v-india-2014/engine/match/667643.html","http://www.espncricinfo.com/new-zealand-v-india-2014/engine/match/667645.html","http://www.espncricinfo.com/new-zealand-v-india-2014/engine/match/667647.html","http://www.espncricinfo.com/new-zealand-v-india-2014/engine/match/667649.html"]

speech = ["http://www.espncricinfo.com/new-zealand-v-india-2014/engine/match/667641.html?innings=1;page=1;view=commentary","http://www.espncricinfo.com/new-zealand-v-india-2014/engine/match/667641.html?innings=2;page=1;view=commentary","http://www.espncricinfo.com/new-zealand-v-india-2014/engine/match/667643.html?innings=1;view=commentary","http://www.espncricinfo.com/new-zealand-v-india-2014/engine/match/667643.html?innings=2;page=1;view=commentary","http://www.espncricinfo.com/new-zealand-v-india-2014/engine/match/667645.html?innings=1;view=commentary","http://www.espncricinfo.com/new-zealand-v-india-2014/engine/match/667645.html?innings=2;page=1;view=commentary","http://www.espncricinfo.com/new-zealand-v-india-2014/engine/match/667647.html?innings=1;view=commentary",
"http://www.espncricinfo.com/new-zealand-v-india-2014/engine/match/667647.html?innings=2;page=1;view=commentary","http://www.espncricinfo.com/new-zealand-v-india-2014/engine/match/667649.html?innings=1;view=commentary","http://www.espncricinfo.com/new-zealand-v-india-2014/engine/match/667649.html?innings=2;page=1;view=commentary"]

#Name various files to be made
files = [[""],['',"11bat.txt","11bowl.txt","12bat.txt","12bowl.txt","1d.txt"],['',"21bat.txt","21bowl.txt","22bat.txt","22bowl.txt","2d.txt"],['',"31bat.txt","31bowl.txt","32bat.txt","32bowl.txt","3d.txt"],['',"41bat.txt","41bowl.txt","42bat.txt","42bowl.txt","4d.txt"],['',"51bat.txt","51bowl.txt","52bat.txt","52bowl.txt","5d.txt"]]

table1 = "inningsBat1"
table2 = "inningsBowl1"
table3 = "inningsBat2"
table4 = "inningsBowl2"


def getdata(url, filename, tableid, flag, winner_flag):

#Using BS4 to parse HTML page by tags
    page = urllib.urlopen(url)
    code = page.read()
    soup = BeautifulSoup(code)
#Get winner unless there is a draw. 
#In case of draw nothing is writted to file
    if winner_flag == 0:
        winner = soup.find('p', attrs={'class': 'statusText'})
        w = str(winner)
        win = w.split('>')[1].split('<')
        fp2 = open("details.txt", "a")
        fp2.write(win[0])
        fp2.write("\n")
        fp2.close()

#Using BS4 to parse HTML page by tags
#Get man of the match
        momtable = soup.find('table', attrs={'class': 'notesTable'})
        rows = momtable.findAll('tr')
        for row in rows:
            cols = row.findAll('td')
            for td in cols:
                list1 = str(td).split('<')
                for li in range(len(list1)):
                    if(str(list1[li]).find('Player of the match') != -1):
                        b = str(list1[li+1]).split('>')
                        c = b[1].replace("\n", "")
                        fp2 = open("details.txt", "a")
                        fp2.write(c)
                        fp2.write("\n")
                        fp2.close()

    table = soup.find('table', id=tableid)
    rows = table.findAll('tr')

# Get the first batting team
    if winner_flag == 0:
        inningdetails = rows[1].findAll('td')
        a1 = str(inningdetails[1]).split('<')
        if(len(a1) > 1):
            a2 = str(a1[1]).split('>')
            c = a2[1]
            c = c.lstrip()
            c = c.rstrip()
            fp2 = open("details.txt", "a")
            fp2.write(c)
            fp2.write("\n")
            if str(c) == "India innings":
                fp2.write("New Zealand innings")
            else:
                fp2.write("India innings")
            fp2.write("\n")
            fp2.close()

#Write table details
    for tr in range(2, len(rows)-flag, 2):
        data = []
        cols = rows[tr].findAll('td')
        for td in range(1, len(cols), 1):
            a = str(cols[td])
            a = a.split('>')
            if td == 1:
                b = str(a[2])
            else:
                b = str(a[1])

            b = b.split('<')
            c = str(b[0])
            c = c.rstrip()
            c = c.lstrip()
            c = c.replace("&amp;", "&")
            c = c.replace("&dagger;", "")
            if td != 1 and c != '':
                a = (",", c)
                s = ''
                s = s.join(a)
            else:
                s = str(c)
            fp = open(filename, "a")
            fp.write(str(s))
            fp.close()
        fp = open(filename, "a")
        fp.write("\n")
        fp.close()

def get_comm(url,n,e,g):
    	f = urllib.urlopen(url)
	html = f.read()

	soup = BeautifulSoup(html)
	table = soup.find('table', attrs={'class':'commsTable'})
	
	rows = table.findAll('tr')
	mohit = {}
	for tr in range(1,len(rows)-n,1):
	    comm = rows[tr].findAll('p', attrs={'class':'commsText'})
	    com = str(comm).split(',')
	    if len(com) > 2:
		    l= re.findall("\d+\.\d+",com[0])
		    if( len(l ) > 0):
			details = {}
			temp = str(com[0]).split('>')
			comm = str(temp[1]).split('<')
			x = comm[0]
			print x
			temp = str(com[1]).split('>')
			comm = str(temp[1]).split('\n')
			comm = comm[0].rstrip("\n")
			print comm
			details["to"] = comm.split(' ')[-1]
			l = comm.split(' ')
			ans = ""
			for i in range(len(l)):
				if l[i] == "to":
					break
				else:
					ans += " " + l[i]
			details["from"] = ans
			if(com[2].find("FOUR") != -1):
			    details["what"] = "4 run"
			elif(com[2].find("SIX") !=-1):
			    details["what"] = "6 run"
			elif(com[2].find("OUT") !=-1):
			    details["what"] = "OUT"
			elif(com[2].find("no ball") !=-1):
			    details["what"] = "no-ball"
			    x=x+'0'
			elif(com[2].find("wide") !=-1):
			    details["what"] = "1 wide"
			    x=x+'0'
			else:
			    	comm = com[2].lstrip("\n")
			    	details["what"] = comm
			try:
			    	details["why"] = " ".join(com[3:])
			except:
				pass
			print details
			mohit[x] = details
			pickle.dump(mohit, open(str(e)+str(g)+"comm.p","wb"))
	


for i in range(1,6): 
    name = "match" + str(i)
    os.mkdir(name)
    os.chdir(name)
    getdata(url[i], files[i][1], table1, 3, 0)
    getdata(url[i], files[i][2], table2, 0, 1)
    getdata(url[i], files[i][3], table3, 3, 1)
    getdata(url[i], files[i][4], table4, 0, 1)
    get_comm(speech[2*(i-1)],4,i,1)
    get_comm(speech[2*(i-1)+1],4,i,2)

    os.chdir("../")
os.chdir("../")
