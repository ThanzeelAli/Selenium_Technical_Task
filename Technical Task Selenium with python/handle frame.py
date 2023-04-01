from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:\chromedriver_win32 (2)\chromedriver.exe")

#max the window
driver.maximize_window()


driver.get("htttps://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe_frameborder_css")

#switch to frame
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframeResult"))

#switch to another frame
driver.switch_to.frame(0)
driver.find_element(By.XPATH,"//a[@id='cert_navbtn']").click()


time.sleep(6)

#quit the window
driver.quit()