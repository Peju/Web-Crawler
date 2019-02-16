import urllib
import requests
from bs4 import BeautifulSoup


seedUrl = "https://en.wikipedia.org/wiki/Orange_(fruit)"
compileURL = []
tenWords = ['fruit','species','health','location','farming','history','nutrition','biology','food']

    
def fuo(url):
    testReq  = requests.get(url)
    if testReq == 404:
        return
    print(testReq)
    abc = 0

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
                abc +=1
            if abc == 2:
                found = True
                print("2 terms have been matched")
                f = open('DataCode.txt','w',encoding="utf8")
                f.write(str(testVar))
                f.close
                break
                
        if found == True:
            break
        
fuo(seedUrl)

"""

f = open('urlList1.txt','w',encoding="utf8")
f.write(data)
f.close()

seedUrl = "https://en.wikipedia.org/wiki/Orange_(fruit")

pageResponse = requests.get(seedUrl, timeout = 3)

contents = BeautifulSoup(pageResponse.content, "html.parser")

textCon = []
for i in range (0,20):
    chunks = contents.find_all("p"[i].text)
    textCon.append(chunks)
"""
"""
seed: orange https://en.wikipedia.org/wiki/Orange_(fruit)
citrus https://en.wikipedia.org/wiki/Citrus_%C3%97_sinensis

related terms
1. orange (fruit)
2. species
3. health benefits
4. location
5. farming
6. history
7. foods
8. nutrition
9. biology
10. recipes

"""
"""
aeedUrls = ['https://en.wikipedia.org/wiki/Orange_(fruit)','https://en.wikipedia.org/wiki/Citrus_%C3%97_sinensis']

queue

soup.find_all("a")

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

def processQueue();
 """


