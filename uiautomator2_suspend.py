#from uiautomator import Device  u1 寫法
#d = Device('0123456789ABCDEF', adb_server_port=5038) u1 寫法
# -*- coding: utf-8 -*-

from time import sleep
import uiautomator2 as u2



d = u2.connect('0123456789ABCDEF')
#()內為device號碼
#d.app_start("com.getac.qct.app")



"""a = int(input("suspend/resume: "))
while a > 0 :
    d.screen_off()# Turn off screen
    sleep(3)
    d.screen_on()# Turn on screen
    d.swipe(600, 675, 600, 320)
    sleep(3)
    a -= 1"""


#d(resourceID="lock_icon").swipe.up(step=10)
d(text="Camera").click()

