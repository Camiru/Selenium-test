# Selenium-test
Selenium test (include IDE , webdriver..etc.)
## 安裝Python (以3.5為主)<br />

## 安裝Selenium
pip install selenium<br />
Chrome驅動程式<br />
至https://sites.google.com/a/chromium.org/chromedriver/downloads/下載驅動程式，並將檔案存放於有設定環境變數的路徑當中。<br />
Firefox驅動程式<br />
至https://github.com/mozilla/geckodriver/releases下載驅動程式，並將檔案存放於有設定環境變數的路徑當中。<br /><br />
#20191224更新另一方法(先設定上述驅動程式所下載到的路徑，再加入參數到selenium)<br />
driver_path = C:\XXX\pathToYourDriver\xxx.exe<br />
driver = webdriver.Chrome(driver_path,options=options)<br /><br />

## 練習開始!
import time<br />
time.sleep(5)<br /><br />
from selenium import webdriver<br />
from selenium.webdriver.firefox.options import Options<br /><br />

options = Options()<br />
#關閉瀏覽器跳出訊息<br />
prefs = {<br />
    'profile.default_content_setting_values' :<br />
        {<br />
        'notifications' : 2<br />
         }<br />
}<br />
options.add_experimental_option('prefs',prefs)<br />
options.add_argument("--headless")            #不開啟實體瀏覽器背景執行<br />
options.add_argument("--start-maximized")     #最大化視窗<br />
options.add_argument("--incognito")           #開啟無痕模式<br />
driver = webdriver.Firefox(firefox_options=options)<br />
driver.get("http://www.google.com/")<br />
driver.quit()                        #關閉所有視窗(.close()關閉單一視窗)<br />
#火狐瀏覽器
firefoxOptions.set_preference(“dom.webnotifications.serviceworker.enabled”, false)  #取消跳出訊息框<br />
firefoxOptions.set_preference(“dom.webnotifications.enabled”, false)          #取消跳出訊息框<br /><br /><br />
## 瀏覽器視窗設定<br />
browser.set_window_size(480, 800)#視窗大小設定<br />
browser.maximize_window() #視窗最大化<br />
browser.minimize_window() #視窗最小化<br /><br />
## 選擇各種元素方法<br />
find_element_by_id()<br />
find_element_by_name()<br />
find_element_by_class_name()<br />
find_element_by_tag_name()           #html標籤<br />
find_element_by_link_text()<br />
find_element_by_partial_link_text()<br />
find_element_by_xpath()              #個人認為最好用<br />
                                     #/html開頭為絕對路徑；//為相對路徑find_element_by_css_selector()<br /><br />
#find_element及find_elements的差別<br />
find_element:傳第一個符合條件的WebElement<br />
find_elements:傳回所有符合條件的WebElement<br />
## 顯性等待與隱性等待<br />
time.sleep(n)<br />
#Time模組中的sleep，必須足足等待n秒鐘，稱為顯性等待<br />
implicitly_wait(n)<br />
#Selenium模組中的隱性等待，最多等n秒鐘，如果前一事件提早完成就直接進行下一個動作<br /><br />
# driver.quit與 driver.close差異在於close關閉當時執行的視窗, quit則是關閉所有視窗<br /><br />

## 來小小實作吧 - 在搜尋列輸入ChromeDriver後搜尋<br/>
from selenium import webdriver <br/>
import time <br/> <br/> 

driver = webdriver.Chrome() <br/>
driver.get('http://www.google.com/xhtml'); # 前往 google 首頁 <br/>
driver.maximize_window() <br/>
time.sleep(5) # 等待5秒 <br/> <br/> 

#user = driver.find_element_by_class('gb_kb').text <br/>
#print(user) <br/> <br/>

size = driver.find_element_by_name('q').size <br/>
print(size) <br/>
search_box = driver.find_element_by_name('q') # 取得搜尋框 <br/>
search_box.send_keys('ChromeDriver') # 在搜尋框內輸入 'ChromeDriver' <br/>
search_box.submit() # 令 chrome driver 按下 submit <br/>
time.sleep(5) <br/> <br/>

#driver.quit() # 關閉 chromedriver <br/>
