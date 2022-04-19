import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=M&rtm=N&ymd=20210701',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# 코딩 시작
# print(soup)

# 순위
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number

# 이름
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis

# 가수
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis

tr = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
# print(tr)

for output in tr:
    rank = output.select_one('td.number')
    if rank is not None:
        rank = rank.text[0:2]
        title = output.select_one('td.info > a.title.ellipsis').text.strip()
        artist = output.select_one('td.info > a.artist.ellipsis').text
    print(rank, title, artist)