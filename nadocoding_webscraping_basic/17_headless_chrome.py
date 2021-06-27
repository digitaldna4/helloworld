"""
    나도코딩
    활용편3
    https://youtu.be/yQ20jZwDjTE
"""

from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("windows-size=1920x1080")

browser = webdriver.Chrome("d:/Workspaces/HelloWorld/helloworld/chromedriver_win32/chromedriver.exe", options=options)
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
browser.get_screenshot_as_file("google_movie.png")

import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, "lxml")

#movies = soup.find_all("div", attrs={"class":["ImZGtf mpg5gc", "Vpfmgd"]})
movies = soup.find_all("div", attrs={"class":"Vpfmgd"})
print(len(movies))

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    print(title)

    # 할인 전 가격
    original_price = movie.find("span", attrs={"class":"SUt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
    else:
        print(title, "<할인 되지 않은 영화 제외>")
        continue

    # 할인된 가격
    price = movie.find("span", attrs={"class":"VfPpfd ZdBevf i5DZme"}).get_text()

    # 링크
    link = movie.find("a", attrs={"class":"JC71ub"})["href"]

    print(f"제목 : {title}")
    print(f"할인 전 금액 : {original_price}")
    print(f"할인 후 금액 : {price}")
    print("링크 : ", "https://play.google.com"+link)
    print("-" * 100)

browser.quit()



# [22704:22724:0623/215252.669:ERROR:device_event_log_impl.cc(214)] [21:52:52.668] USB: usb_device_handle_win.cc:1058 Failed to read descriptor from node connection: A device attached to the system is not functioning. (0x1F)



