from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome("C:\chromedriver_win32 (2)\chromedriver.exe")
driver.get("https://www.plupload.com/examples/")

element=driver.find_element(By.XPATH,"//span[normalize-space()='Add Files']")
element.click()
element.send_keys("C:\chromedriver_win32 (2)\spiderman-ps4-spiderman-superheroes-games-wallpaper-preview")