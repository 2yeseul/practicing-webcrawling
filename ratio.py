from urllib.request import urlopen
from bs4 import BeautifulSoup



# 크롤링하고자 하는 url
targetUrl = "http://addon.jinhakapply.com/RatioV1/RatioH/Ratio11080161.html?1537707368320"

soupData = BeautifulSoup(urlopen(targetUrl).read(), 'html.parser')

# 크롤링으로 얻을 data 저장
data = []
# div 태그를 가진 코드를 전부 찾는다
divs = soupData.find_all("div")

# 각 div 태그 안, tr과 td 찾기
for div in divs:
    for tr in soupData.find_all("tr",{"onmouseover" : "this.className='over';"}):
        tds = list(tr.find_all("td"))
        for td in tds:
            # 단과대학 포함된 경우
            if '대학' in tds[0].text.strip() and len(tds) >=5:
                displayName = tds[1].text.strip()
                mojip = tds[2].text.strip()
                jiwon = tds[3].text.strip()
                ratio = tds[4].text.strip()

            # 단과대학 포함되지 않은 경우
            elif '대학' not in tds[0].text.strip() and len(tds) >= 4:
                displayName = tds[0].text.strip()
                mojip = tds[1].text.strip()
                jiwon = tds[2].text.strip()
                ratio = tds[3].text.strip()

        data.append([displayName, mojip, jiwon, ratio ])

for i in range(0, len(data)):
    print(data[i])
#print(data)
