from selenium import webdriver
from selenium import By

driver = webdriver.Chrome()

driver.get("https://kinnser.net/login.cfm")
userElem = driver.find_element(By.ID, "username")
userElem.send_keys("jason")



