"""
    나도코딩
    활용편3
    https://youtu.be/yQ20jZwDjTE
"""

from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("windows-size=1920x1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

browser = webdriver.Chrome("d:/Workspaces/HelloWorld/helloworld/chromedriver_win32/chromedriver.exe", options=options)
browser.maximize_window()

# 페이지 이동
url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)

detected_value = browser.find_element_by_id("detected_value")
print(detected_value.text)
browser.quit()


# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/91.0.4472.124 Safari/537.36