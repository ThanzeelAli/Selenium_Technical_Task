from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome("C:\chromedriver_win32 (2)\chromedriver.exe")
driver.maximize_window()

driver.get("https://www.oyorooms.com/")
chennai=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div[2]/div/div[2]")
tnagar=driver.find_element(By.CSS_SELECTOR,"#root > div > div.homePage__container > div.cmsWrapper.cmsWrapper--topFold > div.oyo-row.oyo-row--no-spacing.headerMDD > div > div:nth-child(2) > div > a:nth-child(3)")

action=ActionChains(driver)
action.move_to_element(chennai).click(tnagar).perform()