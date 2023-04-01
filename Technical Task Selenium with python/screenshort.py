from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome("C:\chromedriver_win32 (2)\chromedriver.exe")
time.sleep(5)
driver.get("https://web.whatsapp.com/")

#screenshot

element=driver.find_element(By.XPATH,"//span[normalize-space()='Add Files']")
element.screenshot("upload.png")

driver.implicitly_wait(5)

driver.quit()