import requests
import re
from bs4  import BeautifulSoup

# 쿠팡에서 노트북 검색시 첫 페이지 url
url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=&backgroundColor="
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}

res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("li", attrs={"class":re.compile("^search-product")})

# print(items[0].find("div", attrs={"class":"name"}).get_text())

for i in items:
    # 로켓 배송 아닌 경우 제외
    rocket = i.find("span", attrs={"class":"badge rocket"})
    if not rocket:
        print("로켓 배송만 포함합니다")
        continue
        
    # 삼성전자 상품 제외
    name = i.find("div", attrs={"class":"name"}).get_text() # 제품명
    if "삼성전자" in name:
        print("삼성전자 제품 제외")
        continue

    price = i.find("strong", attrs={"class":"price-value"}).get_text() # 가격

    # 리뷰 50개 이상, 평점 4.2 이상만 조회
    rate = i.find("em", attrs={"class":"rating"}) # 평점 - 평점이 없는 경우가 있었음
    if rate:
        rate = rate.get_text()
    else:
        print("평점 없음")
        continue

    rate_cnt = i.find("span", attrs={"class":"rating-total-count"}) # 평점 수 (30)
    if rate_cnt:
        rate_cnt = rate_cnt.get_text()
        rate_cnt = rate_cnt[1:-1] # 평점 수 옆의 괄호 제거
    else:
        print("평점 수 없음")
        continue

    if float(rate) >= 4.2 and int(rate_cnt) >= 50:
        print(name, price, rate, rate_cnt, sep="☆")
