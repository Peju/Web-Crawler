import urllib
import requests
import queue
from bs4 import BeautifulSoup

seedUrl = "https://en.wikipedia.org/wiki/Orange_(fruit)"
seedUrl2 = "https://en.wikipedia.org/wiki/Citrus"
compileURL = []
tenWords = ['fruit','species','health','location','farming','history','nutrition','biology','food']
compileURL.append(seedUrl)
compileURL.append(seedUrl2)
goodUrls = []
	
def check(url):

    try:
            testReq  = requests.get(url)
            print(testReq)
            counterN = 0
            global counter
            global compileURL
            global goodUrls

        
            found = False

            data = testReq.text

            soupTest = BeautifulSoup(data,"html.parser")

            testVar = soupTest.find_all('div',{'class': "mw-parser-output"})[0]
            testVar2 = str(testVar).split()
            print (len(testVar2))

            for link in soupTest.find_all('a'):
                #print(link.get('href'))
                compileURL.append(link.get('href'))

            for x in testVar2:
                #print (x)
                for y in tenWords:
                    if x == y:
                        counterN +=1
                    if counterN == 2:
                        found = True
                        goodUrls.append(url)
                        counter +=1
                        print("2 terms have been matched")
                        f = open(str(counter)+'DataCode.txt','w',encoding="utf8")
                        f.write(str(testVar))
                        f.close
                        break
                        
                if found == True:
                    break
    except:
            return
    
counter = 0 # counter for number of good sites

while counter < 501 and compileURL:
	check(compileURL.pop(0))

f = open('listurl.txt','w',encoding="utf8")
f.write(str(goodUrls))
f.close


