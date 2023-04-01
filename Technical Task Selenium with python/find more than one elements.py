from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:\chromedriver_win32 (2)\chromedriver.exe")
driver.get("https://www.facebook.com")

#find all links on the page
links=driver.find_element(By.TAG_NAME,"a")

#loop through the list of link and print in text
for link in links:
    print(link.text)

#quit the window
driver.quit()