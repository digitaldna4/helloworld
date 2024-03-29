"""
    나도코딩
    활용편3
    https://youtu.be/yQ20jZwDjTE
"""

import time
from selenium import webdriver

browser = webdriver.Chrome("d:/Workspaces/HelloWorld/helloworld/chromedriver_win32/chromedriver.exe")

# 1. 네이버로 이동
browser.get("http://naver.com")

# 2. 로그인
elem = browser.find_element_by_class_name("link_login")
elem.click()

# 3. id. pw 입력
browser.find_element_by_id("id").send_keys("iiiii")
browser.find_element_by_id("pw").send_keys("ppppp")

# 4. 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

# 5. id를 새로 입력
time.sleep(3)
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("iiiii2")

# 6. html 정보 출력
print(browser.page_source)

# 7. 브라우저 종료
#browser.close()    # 현재 탭만 종료
browser.quit()      # 전체 종료
