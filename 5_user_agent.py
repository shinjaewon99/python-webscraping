import requests

url ="https://www.acmicpc.net/"
header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}

res = requests.get(url, headers=header)
res.raise_for_status()



with open("baekjoon.html" , "w", encoding="utf8")as f:
    f.write(res.text) 





