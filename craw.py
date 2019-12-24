import requests
from bs4 import BeautifulSoup
res = requests.Session()

res = requests.get('https://www.ptt.cc/bbs/joke/index6915.html', verify=False)
res.encoding = 'utf-8'
soup = BeautifulSoup(res.content)
for entry in soup.select('.r-ent'):     
    print(entry.select('.title')[0].text,entry.select('.date')[0].text,entry.select('.author')[0].text)

