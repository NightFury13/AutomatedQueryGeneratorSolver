import os 
import pickle
import re
import urllib2
from bs4 import BeautifulSoup

speech = ["http://www.espncricinfo.com/new-zealand-v-india-2014/engine/match/667641.html?innings=1;page=1;view=commentary","http://www.espncricinfo.com/new-zealand-v-india-2014/engine/match/667641.html?innings=2;page=1;view=commentary","http://www.espncricinfo.com/new-zealand-v-india-2014/engine/match/667643.html?innings=1;view=commentary","http://www.espncricinfo.com/new-zealand-v-india-2014/engine/match/667643.html?innings=2;page=1;view=commentary","http://www.espncricinfo.com/new-zealand-v-india-2014/engine/match/667645.html?innings=1;view=commentary","http://www.espncricinfo.com/new-zealand-v-india-2014/engine/match/667645.html?innings=2;page=1;view=commentary","http://www.espncricinfo.com/new-zealand-v-india-2014/engine/match/667647.html?innings=1;view=commentary",
"http://www.espncricinfo.com/new-zealand-v-india-2014/engine/match/667647.html?innings=2;page=1;view=commentary","http://www.espncricinfo.com/new-zealand-v-india-2014/engine/match/667649.html?innings=1;view=commentary","http://www.espncricinfo.com/new-zealand-v-india-2014/engine/match/667649.html?innings=2;page=1;view=commentary"]

def get_comm(url,n,e,g):
        f = urllib2.urlopen(url)
        html = f.read()
 
        soup = BeautifulSoup(html)
        table = soup.find('table', attrs={'class':'commsTable'})
       
        rows = table.findAll('tr')
        dev = {}
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
                            details["what"] = "4 runs"
                        elif(com[2].find("SIX") !=-1):
                            details["what"] = "6 runs"
                        elif(com[2].find("OUT") !=-1):
                            details["what"] = "OUT"
                        else:
                                comm = com[2].lstrip("\n")
                                details["what"] = comm
                        try:
                                details["why"] = " ".join(com[3:])
                        except:
                                pass
                        print details
                        dev[x] = details
			pickle.dump(dev, open(str(e)+str(g)+"comm.p","wb"))

for i in range(1,6): 
    name = "match" + str(i)
    os.mkdir(name)
    os.chdir(name)
    get_comm(speech[2*(i-1)],4,i,1)
    get_comm(speech[2*(i-1)+1],4,i,2)
    os.chdir("../")
