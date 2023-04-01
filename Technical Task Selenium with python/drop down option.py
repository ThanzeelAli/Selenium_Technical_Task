from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome("C:\chromedriver1\chromedriver.exe")
driver.get("https://letcode.in/dropdowns")

#Select the apple using visible text
sele = driver.find_element(By.XPATH,"//select[@id='fruits']")
drop = Select(sele)
drop.select_by_visible_text("Mango")

#Select your super hero's
superhero = driver.find_element(By.XPATH,"Select your super hero's")
gets = Select(superhero)
gets.select_by_index(2)