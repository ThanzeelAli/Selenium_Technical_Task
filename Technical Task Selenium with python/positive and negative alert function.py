from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException

driver = webdriver.Chrome("C:\chromedriver_win32 (2)\chromedriver.exe")
#website link
driver.get("https://letcode.in/alert")



#switch function with single alert function
windo=driver.find_element(By.XPATH,"//button[@id='accept']")
windo.click()
driver.switch_to.alert.accept()

driver.quit()

#negative
driver = webdriver.Chrome("C:\chromedriver_win32 (2)\chromedriver.exe")
#website link
driver.get("https://letcode.in/alert")

try:
    alert = driver.switch_to.alert
except NoAlertPresentException:
    pass

driver.quit()
