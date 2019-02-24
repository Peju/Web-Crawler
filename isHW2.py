import urllib
import requests
import queue
from bs4 import BeautifulSoup

seedUrl = "https://en.wikipedia.org/wiki/Orange_(fruit)"
compileURL = []
tenWords = ['fruit','species','health','location','farming','history','nutrition','biology','food']

qe = queue.Queue()
    
def mainCheck(url):
    testReq  = requests.get(url)
    if testReq == 404:
        return
    print(testReq)
    counterN = 0

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
                print("2 terms have been matched")
                f = open('DataCode.txt','w',encoding="utf8")
                f.write(str(testVar))
                f.close
                break
                
        if found == True:
            break
  
mainCheck(seedUrl)

while(True):
    print(str(len(compileURL)) + " links returned")
    f = open('listurl.txt','w',encoding="utf8")
    f.write(str(compileURL))
    f.close
    break


"""
pageResponse = requests.get(seedUrl, timeout = 3)

for i in range (0,20):
    chunks = contents.find_all("p"[i].text)
    textCon.append(chunks

for url in seedUrls:
    seedUrls.append(url)
    visitedUrlList.append(url)
while queue is not empty:
    url = queue.pop()
    pageContent = retrievePageContent(url)
    if pageContent is None:
        continue
    termCounter = 0
    pageMainText = extractMainText(pageContent)
    for term in relatedTerms:
        if match (term, pageMainText, CaseInsensitive):
            termCounter = termCounter+1
            if termCounter >= 2:
                pageTitle = getTitle(pageContent)
                save(pageTitle, pageContent)
                savedUrlList.add(url)
                pageCounter = pageCounter+1
                print("page # termCounter: url")
                break
    if pageCounter >= 500:
        break
    outGoingUrls = extractOutGoingUrl(pageContent)
    for outGoingUrl in outGoingUrls:
        if domainCheck(outGoingUrl) and outGoingUrl not in visitedUrlList:
            queue.add(outGoingUrl)
            visitedUrlList.add(outGoingUrl)
save(savedUrlList)
 """
