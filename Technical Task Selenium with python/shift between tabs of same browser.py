from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Initialize open browser
driver = webdriver.Chrome("C:\chromedriver_win32 (2)\chromedriver.exe")

#max the window
driver.maximize_window()

#open new tab
driver.execute_script("window.open('');")

#switch to parent window and load webpage
driver.switch_to.window(driver.window_handles[0])
driver.get("https://www.facebook.com")
time.sleep(2)

#switch to childwindow and close
driver.switch_to.window(driver.window_handles[1])
driver.close()

time.sleep(2)

#quit window
driver.quit()

