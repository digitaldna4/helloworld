"""
    나도코딩
    활용편3
    https://youtu.be/yQ20jZwDjTE
"""

from logging import currentframe
from selenium import webdriver
browser = webdriver.Chrome("d:/Workspaces/HelloWorld/helloworld/chromedriver_win32/chromedriver.exe")
browser.maximize_window()

# 페이지 이동
url = "https://play.google.com/store/movies/top"
browser.get(url)

# # 스크롤 내리기
# # 모니터(해상도) 높이인 1080위치로 스크롤 내리기
# browser.execute_script("window.schollTo(0, 1080)")

# # 화면 가장 아래로 스크로 내리기
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")


import time
interval = 2    # 2초에 한번씩 스크롤 내림

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복수행
while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # 페이지 로딩 대기
    time.sleep(interval)

    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break

print("스크롤 완료")


# # from selenium import webdriver
# # from selenium.webdriver.chrome.webdriver import WebDriver
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC

# url = "https://play.google.com/store/movies/top"
# headers = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
#     "Accept-Language":"ko-KR, ko"
#     }

# res = requests.get(url, headers=headers)
# res.raise_for_status()
# soup = BeautifulSoup(res.text, "lxml")

# movies = soup.find_all("div", attrs={"class":"ImZGtf mpg5gc"})
# print(len(movies))

# # with open("movie.html", "w", encoding="utf8") as f:
# #     # f.write(res.text)
# #     f.write(soup.prettify())    # html 문서를 예쁘게..

# for movie in movies:
#     title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
#     print(title)