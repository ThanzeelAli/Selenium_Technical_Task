from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys


#different browser
browsers=["chrome","firefox"]

#use loop method to launch the browser
for browser in browsers:
   if browser=="chrome":
       driver = webdriver.Chrome("C:\chromedriver_win32 (2)\chromedriver.exe")
   elif browser=="firefox":
      driver = webdriver.Firefox("C:\Program Files\Mozilla Firefox\firefox.exe")

   # max the window
   driver.maximize_window()

   driver.get("https://www.google.com")
   time.sleep(2)

   # open new window with load a new webpage
   driver.execute_script('window.open("");')
   driver.switch_to.window(driver.window_handles[1])
   driver.get("https://web.whatsapp.com/")
   driver.implicitly_wait(2)

   # open another window with load a new webpage
   driver.execute_script('window.open("");')
   driver.switch_to.window(driver.window_handles[2])
   driver.get("https://letcode.in/dropable")
   driver.implicitly_wait(2)

   # close current window
   driver.close()

   # switch to pervious window
   driver.switch_to.window(driver.window_handles[1])
   driver.close()

   # quit the chrome browser
   driver.quit()
