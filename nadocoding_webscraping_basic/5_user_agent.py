"""
    나도코딩
    활용편3
    https://youtu.be/yQ20jZwDjTE
"""

import requests
url = "http://nadocoding.tistory.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

with open("hellocoding.html", "w", encoding="utf8") as f:
    f.write(res.text)
