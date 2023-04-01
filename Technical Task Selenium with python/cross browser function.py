from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys


#different browser
browsers=["chrome","firefox","edge"]

#use loop method to launch the browser
for browser in browsers:
   if browser=="chrome":
       driver = webdriver.Chrome("C:\chromedriver_win32 (2)\chromedriver.exe")
   elif browser=="firefox":
      driver = webdriver.Firefox("C:\Program Files\Mozilla Firefox\firefox.exe")
   elif browser=="edge":
       driver= webdriver.Edge("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")


   # max the window
   driver.maximize_window()

   driver.get("https://web.whatsapp.com/")

   #quit the window
   driver.quit()
