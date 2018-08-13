"""Test step
1.Log in (getacdvd3test@gmail.com/dvd3test) admin account
2.Go to welcome landing page -->Click Start button  ---- print log
3.Select any group --> Click Next button (remove)
4.Open Activation code and download
5.Select up to 20 items setup --- print log
6.Generate and type description --- print log
7.Generate
8.Download QR code with images
9.Download QR code with files
10.Send to other devices
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.command import Command
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import unittest, time, re , os

IE_path = "C:\Python36\selenium\IEDriverServer.exe" #IEdriver.exe執行檔所存在的路徑
start_time = time.time()

web = webdriver.Ie(IE_path)

driver = webdriver.Ie(IE_path)
driver.get("https://xpress.getac.com/login") #deploy登入頁
driver.maximize_window() #讓瀏覽器開最大
driver.find_element_by_xpath("//*[@id='email']").clear()
driver.find_element_by_xpath("//*[@id='email']").send_keys("getacdvd3test@gmail.com")#輸入帳號getacdvd3test@gmail.com
driver.find_element_by_id("password").clear()
driver.find_element_by_id("password").send_keys("dvd3test")              #輸入密碼dvd3test
driver.find_element_by_xpath("/html/body/app-root/app-entry-portal/div/div[2]/app-login/div/div[2]/form/div[5]/button").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/app-root/app-user/div[2]/user-application/div/div[2]/div[2]/div/div/div/div[3]/button[1]").click() #點選open Xpress
driver.implicitly_wait(20)

try:  
    driver.find_element_by_xpath("/html/body/app-root/div[2]/app-deployxpress/app-dx-landing/div[1]/div/div[1]/h3")  
    print ('test pass: enter welcome page success')  
except Exception as e:
    print ("Exception found", format(e))  #判斷進入welcome landong page成功

driver.find_element_by_xpath("/html/body/app-root/div[2]/app-deployxpress/app-dx-landing/div[1]/div/div[3]/button").click() #按welcome landing page的start button
driver.implicitly_wait(4)
driver.find_element_by_xpath("/html/body/app-root/div[2]/app-deployxpress/app-qr-generator/app-target-device/div/div/div[2]/form/div[3]/app-custom-select/div/button").click() #select Android OS
driver.implicitly_wait(2)
driver.find_element_by_xpath("//ul[@id='drop']/li[2]").click() #select Android 6.0
driver.implicitly_wait(2)
driver.find_element_by_css_selector("button.btn-dex").click()#click next#
driver.implicitly_wait(4)
driver.find_element_by_xpath("//img[@alt='Settings']").click() #open Activate code
time.sleep(1)
driver.find_element_by_xpath("//li").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/app-root/div[2]/app-deployxpress/app-activate-qrcode/div/div/div/div[2]/button").click() #download Activate code to local
time.sleep(1)
driver.find_element_by_xpath("/html/body/app-root/div[2]/app-deployxpress/app-activate-qrcode/div/div/div/div[1]/button/img").click() #close activate code
time.sleep(1)
driver.find_element_by_xpath("/html/body/app-root/div[2]/app-deployxpress/app-qr-generator/app-config-main/div/div[2]/app-config-panel/div/div/div[2]/app-dynamic-form/div/form/div/div[3]").click() #add Wireless & Networks/wifi on/off 
time.sleep(1)
driver.find_element_by_xpath("/html/body/app-root/div[2]/app-deployxpress/app-qr-generator/app-config-main/div/div[1]/div[1]/div[2]/ul/li[2]").click() #switch to Wireless & Networks/BT #
time.sleep(1)
driver.find_element_by_xpath("/html/body/app-root/div[2]/app-deployxpress/app-qr-generator/app-config-main/div/div[2]/app-config-panel/div/div/div[2]/app-dynamic-form/div/form/div/div[3]").click() #add Wireless & Networks / BT on /off
time.sleep(1)
driver.find_element_by_xpath("//div[2]/div/div/span").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/app-root/div[2]/app-deployxpress/app-qr-generator/app-config-main/div/div[1]/div[1]/div[1]/div").click() #Wireless & Networks / Cellular Networks & Mobile Plan
time.sleep(1)
driver.find_element_by_xpath("/html/body/app-root/div[2]/app-deployxpress/app-qr-generator/app-config-main/div/div[1]/div[1]/div[2]/ul/li[3]").click() #
time.sleep(1)
driver.find_element_by_xpath("/html/body/app-root/div[2]/app-deployxpress/app-qr-generator/app-config-main/div/div[2]/app-config-panel/div/div/div[2]/app-dynamic-form/div/form/div/div[3]").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/app-root/div[2]/app-deployxpress/app-qr-generator/app-config-main/div/div[1]/div[1]/div[2]/ul/li[4]").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/app-root/div[2]/app-deployxpress/app-qr-generator/app-config-main/div/div[2]/app-config-panel/div/div/div[2]/app-dynamic-form/div/form/div/div[3]").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/app-root/div[2]/app-deployxpress/app-qr-generator/app-config-main/div/div[2]/app-config-panel/div/div/div[3]/app-dynamic-form/div/form/div[1]/div[3]").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/app-root/div[2]/app-deployxpress/app-qr-generator/app-config-main/div/div[2]/app-config-panel/div/div/div[4]/app-dynamic-form/div/form/div[1]/div[3]").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/app-root/div[2]/app-deployxpress/app-qr-generator/app-config-main/div/div[1]/div[1]/div[2]/ul/li[5]").click()#Wireless & Networks /  Networking Miscellaneous
time.sleep(1)
driver.find_element_by_xpath("/html/body/app-root/div[2]/app-deployxpress/app-qr-generator/app-config-main/div/div[2]/app-config-panel/div/div/div[3]/app-dynamic-form/div/form/div/div[3]").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/app-root/div[2]/app-deployxpress/app-qr-generator/app-config-main/div/div[2]/app-config-panel/div/div/div[5]/app-dynamic-form/div/form/div/div[3]").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/app-root/div[2]/app-deployxpress/app-qr-generator/app-config-main/div/div[1]/div[2]/div[1]/div").click()#切到Device
time.sleep(1)
driver.find_element_by_xpath("/html/body/app-root/div[2]/app-deployxpress/app-qr-generator/app-config-main/div/div[1]/div[2]/div[2]/ul/li[1]").click() #切到Device/Display
time.sleep(1)
driver.find_element_by_xpath("/html/body/app-root/div[2]/app-deployxpress/app-qr-generator/app-config-main/div/div[2]/app-config-panel/div/div/div[2]/app-dynamic-form/div/form/div/div[3]").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/app-root/div[2]/app-deployxpress/app-qr-generator/app-config-main/div/div[2]/app-config-panel/div/div/div[3]/app-dynamic-form/div/form/div/div[3]").click() #sleep
time.sleep(1)
driver.find_element_by_xpath("/html/body/app-root/div[2]/app-deployxpress/app-qr-generator/app-config-main/div/div[2]/app-config-panel/div/div/div[5]/app-dynamic-form/div/form/div/div[3]").click() #Adaptive Brightness
time.sleep(1)
driver.find_element_by_xpath("/html/body/app-root/div[2]/app-deployxpress/app-qr-generator/app-config-main/div/div[1]/div[2]/div[2]/ul/li[2]").click() # Device / Sound & Notification
time.sleep(1)
driver.find_element_by_xpath("/html/body/app-root/div[2]/app-deployxpress/app-qr-generator/app-config-main/div/div[2]/app-config-panel/div/div/div[2]/app-dynamic-form/div/form/div/div[3]").click() #Media Volume
time.sleep(1)
driver.find_element_by_xpath("/html/body/app-root/div[2]/app-deployxpress/app-qr-generator/app-config-main/div/div[2]/app-config-panel/div/div/div[5]/app-dynamic-form/div/form/div/div[3]").click() #Screen Lock Sound
time.sleep(1)
driver.find_element_by_xpath("/html/body/app-root/div[2]/app-deployxpress/app-qr-generator/app-config-main/div/div[2]/app-config-panel/div/div/div[8]/app-dynamic-form/div/form/div/div[3]").click() #Vibrate on Touch
time.sleep(1)
driver.find_element_by_xpath("//div[2]/div[2]/ul/li[3]").click() #切到Device / Users 
time.sleep(1)
driver.find_element_by_id("Add User").send_keys("aaaaa") # Add user "aaaaa"
time.sleep(1)
driver.find_element_by_css_selector("button[type=\"submit\"]").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/app-root/div[2]/app-deployxpress/app-qr-generator/app-config-main/div/div[1]/div[2]/div[2]/ul/li[5]").click() # Device / Device Miscellaneous
time.sleep(1)
driver.find_element_by_xpath("/html/body/app-root/div[2]/app-deployxpress/app-qr-generator/app-config-main/div/div[2]/app-config-panel/div/div/div[2]/app-dynamic-form/div/form/div/div[3]").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/app-root/div[2]/app-deployxpress/app-qr-generator/app-config-main/div/div[1]/div[3]/div[1]/div").click() #切到Personal
time.sleep(1)
driver.find_element_by_xpath("/html/body/app-root/div[2]/app-deployxpress/app-qr-generator/app-config-main/div/div[1]/div[3]/div[2]/ul/li[1]").click() #Security
time.sleep(1)
driver.find_element_by_xpath("/html/body/app-root/div[2]/app-deployxpress/app-qr-generator/app-config-main/div/div[2]/app-config-panel/div/div/div[3]/app-dynamic-form/div/form/div/div[3]").click() # Screen Lock
time.sleep(1)
driver.find_element_by_xpath("/html/body/app-root/div[2]/app-deployxpress/app-qr-generator/app-config-main/div/div[2]/app-config-panel/div/div/div[5]/app-dynamic-form/div/form/div/div[3]").click() # Unknow Source
time.sleep(1)
driver.find_element_by_xpath("/html/body/app-root/div[2]/app-deployxpress/app-qr-generator/app-config-main/div/div[1]/div[3]/div[2]/ul/li[3]").click() # Personal / Personal Miscellaneous
time.sleep(1)
driver.find_element_by_xpath("/html/body/app-root/div[2]/app-deployxpress/app-qr-generator/app-config-main/div/div[2]/app-config-panel/div/div/div[2]/app-dynamic-form/div/form/div/div[3]").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/app-root/div[2]/app-deployxpress/app-qr-generator/app-config-main/div/div[1]/div[4]/div[1]/div").click()  #切到System
time.sleep(1)
driver.find_element_by_xpath("/html/body/app-root/div[2]/app-deployxpress/app-qr-generator/app-config-main/div/div[1]/div[4]/div[2]/ul/li[1]").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/app-root/div[2]/app-deployxpress/app-qr-generator/app-config-main/div/div[2]/app-config-panel/div/div/div[2]/app-dynamic-form/div/form/div/div[3]").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/app-root/div[2]/app-deployxpress/app-qr-generator/app-config-main/div/div[2]/app-config-panel/div/div/div[4]/app-dynamic-form/div/form/div/div[3]").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/app-root/div[2]/app-deployxpress/app-qr-generator/app-config-main/div/div[2]/app-config-panel/div/div/div[7]/app-dynamic-form/div/form/div/div[3]").click()
time.sleep(1)

a1 = driver.switch_to.alert  # 透過switch_to.alert切换到alert 設定達20個警告 
time.sleep(1)
print (a1.text) #印出彈跳視窗訊息
a1.accept()  # alert“確認”
time.sleep(1)

driver.find_element_by_xpath("/html/body/app-root/div[2]/app-deployxpress/app-qr-generator/app-config-main/div/div[3]/div[23]/button").click() #click Generate btn to generate QR code
time.sleep(1)
driver.find_element_by_xpath("//*[@id='qrcode_string']").send_keys("Auto test QR code")
time.sleep(1)

try:  
    driver.find_element_by_xpath("/html/body/app-root/div[2]/app-deployxpress/app-qr-generator/app-config-main/app-name-confirm/div/div/div/div[1]/span")  
    print ('Test pass: Complete generation success')  
except Exception as e:
    print ("Exception found", format(e))  #判斷QR code Complete generation成功
    
driver.find_element_by_xpath("//*[@id='btn_generate']").click()#確認Complete generation提示
time.sleep(4) #QR code產生頁面loading較慢所以設4
driver.find_element_by_xpath("/html/body/app-root/div[2]/app-deployxpress/app-qr-generator/app-qr-distribute/div/div/div[3]/div[3]/button").click() #More actions button
time.sleep(1)
driver.find_element_by_xpath("/html/body/app-root/div[2]/app-deployxpress/app-qr-generator/app-qr-distribute/app-more-actions/div/div/div/div[2]/div[2]/button").click() #download QR code --  images
time.sleep(1)
driver.find_element_by_xpath("/html/body/app-root/div[2]/app-deployxpress/app-qr-generator/app-qr-distribute/app-more-actions/div/div/div/div[2]/app-dl-file/form/div[2]/button[2]").click() #download QR code -- download images
time.sleep(1)
driver.find_element_by_xpath("//select").click() #Images to Files
time.sleep(1)
Select(driver.find_element_by_xpath("//select")).select_by_visible_text("Files")
time.sleep(2)
driver.find_element_by_xpath("//option[@value='1: Object']").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/app-root/div[2]/app-deployxpress/app-qr-generator/app-qr-distribute/app-more-actions/div/div/div/div[2]/app-dl-file/form/div[2]/button[2]").click() #download QR code -- Files
time.sleep(1)
driver.find_element_by_xpath("/html/body/app-root/div[2]/app-deployxpress/app-qr-generator/app-qr-distribute/app-more-actions/div/div/div/div[2]/app-dl-file/form/div[2]/button[1]").click() # Back to More actions
time.sleep(1)
driver.find_element_by_xpath("//img[@alt='Send']").click()
driver.find_element_by_xpath("//div[2]/button").click()
driver.find_element_by_xpath("//input[@value='0']").click()
driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(1)

a1 = driver.switch_to.alert  # 透過switch_to.alert切换到顯示 Successful transmission! 
time.sleep(1)
print (a1.text) #印出彈跳視窗訊息
a1.accept()  # alert“確認”
time.sleep(1)


driver.find_element_by_xpath("/html/body/app-root/div[2]/app-deployxpress/app-qr-generator/app-qr-distribute/app-more-actions/div/div/div/div[2]/app-send-file/div/form/div[2]/button[1]").click()
driver.find_element_by_xpath("/html/body/app-root/div[2]/app-deployxpress/app-qr-generator/app-qr-distribute/app-more-actions/div/div/div/div[1]/button").click()

print("--- %s seconds ---" % (time.time() - start_time)) #印出跑完時間
