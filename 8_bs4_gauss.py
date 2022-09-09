import requests
from bs4 import BeautifulSoup



url = "https://comic.naver.com/webtoon/list?titleId=675554"
res = requests.get(url)
res.raise_for_status()


soup = BeautifulSoup(res.text, "lxml")


# cartoons = soup.find_all("td" , attrs ={"class" :"title"})
# title = cartoons[0].a.get_text()
# link = cartoons[0].a["href"]
# print(title)
# print("http://comic.naver.com" + link)

# 만화 제목 + 링크 가져오기
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "http://comic.naver.com" + cartoon.a["href"]
#     print(title, link)

#평점 구하기
cartoons = soup.find_all("div" , attrs={"class" :"rating_type"})

for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    print(rate)
