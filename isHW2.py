import urllib
from bs4 import BeautifulSoup

"""
seed: orange https://en.wikipedia.org/wiki/Orange_(fruit)
citrus https://en.wikipedia.org/wiki/Citrus_%C3%97_sinensis
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
    
