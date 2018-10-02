from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import re

# response = requests.get('http://addon.jinhakapply.com/RatioV1/RatioH/Ratio11080161.html?1537707368320')

# 크롤링하고자 하는 url
targetUrl = "http://addon.jinhakapply.com/RatioV1/RatioH/Ratio11080161.html?1537707368320"
# targelUrl의 코드를 읽어온다
# html = urlopen(targetUrl).read()
# beautifulSoup을 통하여 html로 parsing
soupData = BeautifulSoup(urlopen(targetUrl).read(), 'html.parser')

sel = soupData.find('select', {'id': 'selType'})

optionVal = list(soupData.find_all('option'))
# optionVal = sel['value']
selList = []
st = 'SelType'
# 전형 selValue 값 저장 in selList
for o in optionVal:
    val = o.get('value')
    newst = st+val
    if '0' not in val:
        selList.append([newst])



data = []


for i in soupData.find_all('table', {'class' : 'tableRatio3'}):
    for j in i.find_all('tr'):
        tds = list(j.find_all('td'))
       # for td in tds:
       #     print("")


            #print(tds[0].text)
            #displayName = td[0].text
            #print(displayName)

'''
            if '대학' not in tds:
                displayName = tds[0].text
                mojip = tds[1].text
                jiwon = tds[2].text
                ratio = tds[3].text
                data.append([mojip, jiwon, ratio])
'''




###for tr in table.find('tr'):
###    print(tr)



'''
        if '대학' in tds[0].text:
            displayName = tds[1].text
            mojip = tds[2].text
            jiwon = tds[3].text
            ratio = tds[4].text
            data.append([displayName, mojip, jiwon, ratio])
            '''

# print(data)


'''
            displayName = tds[0].text
            mojip = tds[1].text
            jiwon = tds[2].text
            ratio = tds[3].text
            data.append([displayName, mojip, jiwon, ratio])
            print(data)
'''

'''
# 학과명을 받아오는 변수
#unit = soupData
# 경쟁률을 받아오는 변수
rate = soupData

#p = re.compile()
unit = soupData.findAll("td", {"class":"unit"})

rspn = unit.find("rowspan")
for tag in unit:
    if rspn in tag:
        print(tag)
        tag.extract()
    print(tag)
    
'''
# for rowspan in rowspanElements:
 #   rowspan.extract()


# for tag in unit.select('td[class=unit]'):
#    unitList = tag.text.strip()
#    if '대학' not in unitList:
#        print(unitList)

