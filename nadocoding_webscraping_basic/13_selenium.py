"""
    나도코딩
    활용편3
    https://youtu.be/yQ20jZwDjTE
"""

from selenium import webdriver

browser = webdriver.Chrome("d:/Workspaces/HelloWorld/helloworld/chromedriver_win32/chromedriver.exe")
browser.get("http://naver.com")




# D:\Workspaces\HelloWorld\helloworld\nadocoding_webscraping_basic>python
# Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> from selenium import webdriver
# >>> browser = webdriver.Chrome("d:/Workspaces/HelloWorld/helloworld/chromedriver_win32/chromedriver.exe")

# DevTools listening on ws://127.0.0.1:8479/devtools/browser/8326c99d-7155-447c-b530-d6dbe7d48f01
# [27900:11188:0614/232129.731:ERROR:device_event_log_impl.cc(214)] [23:21:29.731] USB: usb_device_handle_win.cc:1058 Failed to read descriptor from node connection: A device attached to the system is not functioning. (0x1F)
# [27900:11188:0614/232129.754:ERROR:device_event_log_impl.cc(214)] [23:21:29.754] USB: usb_device_handle_win.cc:1058 Failed to read descriptor from node connection: A device attached to the system is not functioning. (0x1F)
# [27900:11188:0614/232129.755:ERROR:device_event_log_impl.cc(214)] [23:21:29.755] USB: usb_device_handle_win.cc:1058 Failed to read descriptor from node connection: A device attached to the system is not functioning. (0x1F)
# >>> browser.get("http://naver.com")
# >>> elem = browser.find_elemebt_by_class_name("link_login")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'WebDriver' object has no attribute 'find_elemebt_by_class_name'
# >>> elem = browser.find_element_by_class_name("link_login") 
# >>> elem
# <selenium.webdriver.remote.webelement.WebElement (session="13d137d616d98432b0ee7f9a1439d5d3", element="69060f0d-b19d-4bc1-8ae7-9821a2a694d9")>
# >>> elem.click()
# >>> browser.back()
# >>> browser.forward() 
# >>> [21872:16056:0614/232329.216:ERROR:gpu_init.cc(440)] Passthrough is not supported, GL is disabled

# >>> browser.back()    
# >>> elem = browser.find_element_by_id)"query") 
#   File "<stdin>", line 1
#     elem = browser.find_element_by_id)"query")
#                                      ^
# SyntaxError: unmatched ')'
# >>> elem = browser.find_element_by_id("query") 
# >>> elem
# <selenium.webdriver.remote.webelement.WebElement (session="13d137d616d98432b0ee7f9a1439d5d3", element="75f75092-62e8-4c6b-b2c1-f8447a9fe940")>
# >>> from selenium.webdriver.common.keys import Keys
# >>> elem.send_keys("Hello Doding")
# >>> elem.send_keys(keys.ENTER)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'keys' is not defined
# >>> elem.send_keys(Keys.ENTER) 
# >>> elem = browser.find_elements_by_tag_name("a") 
# >>> for e in elem:
# ...     elem.get_attribute("href")
# ... 
# Traceback (most recent call last):
#   File "<stdin>", line 2, in <module>
# AttributeError: 'list' object has no attribute 'get_attribute'
# >>> for e in elem:             f")
# ...     e.get_attribute("a")))))))                a")
# ... 
# >>>     e.get_attribute("a")
# KeyboardInterrupt
# >>>   