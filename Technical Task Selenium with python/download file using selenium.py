from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome("C:\chromedriver_win32 (2)\chromedriver.exe")
driver.get("https://demo.automationtesting.in/FileDownload.html")

driver.find_element(By.ID,"textbox").send_keys("downloading option")
driver.find_element(By.ID,"createTxt").click()
driver.find_element(By.XPATH,"//a[@id='link-to-download']").click()