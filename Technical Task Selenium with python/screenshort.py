from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome("C:\chromedriver_win32 (2)\chromedriver.exe")
time.sleep(5)
driver.get("https://www.facebook.com/")

#screenshot

element=driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[5]/a")
element.click()
time.sleep(5)
element.screenshot("account.png")

driver.implicitly_wait(5)

driver.quit()
