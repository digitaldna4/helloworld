"""
    나도코딩
    활용편3
    https://youtu.be/yQ20jZwDjTE
"""

import time
from selenium import webdriver

browser = webdriver.Chrome("d:/Workspaces/HelloWorld/helloworld/chromedriver_win32/chromedriver.exe")
browser.maximize_window()   # 창 최대화


url = "https://flight.naver.com/flights/"
browser.get(url)

browser.find_element_by_link_text("가는날 선택").click()

# 이번달
# browser.find_elements_by_link_text("27")[0].click()
# browser.find_elements_by_link_text("29")[0].click()

# 다음달
# browser.find_elements_by_link_text("27")[1].click()
# browser.find_elements_by_link_text("29")[1].click()

# 이번달~다음달
browser.find_elements_by_link_text("27")[0].click()
browser.find_elements_by_link_text("29")[1].click()

# 제주도 선택
browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]").click()

# 항공권 검색
browser.find_element_by_link_text("항공권 검색").click()

# 첫번째 결과 출력
elem = browser.find_element_by_xpath("//*[@id='content']/div[2]/div/div[4]/ul/li[1]")
print(elem.text)