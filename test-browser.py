import os, time
from selenium import webdriver
chromedriver = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'# # 啟動 chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get('http://www.google.com/xhtml'); # 前往 google 首頁
time.sleep(5) # 等待5秒
search_box = driver.find_element_by_name('q') # 取得搜尋框
search_box.send_keys('ChromeDriver') # 在搜尋框內輸入 'ChromeDriver'
search_box.submit() # 令 chrome driver 按下 submit
time.sleep(5)
driver.quit() # 關閉 chromedriver