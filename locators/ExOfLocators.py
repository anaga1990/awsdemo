from selenium import webdriver
from selenium.webdriver.common.by import By

cp = webdriver.ChromeOptions()
cp.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=cp)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.ID, "checkBoxOption3").click()
driver.find_element(By.NAME, "checkBoxOption1").click()
driver.find_element(By.CLASS_NAME, "radioButton").click()
driver.find_element(By.LINK_TEXT, "Home")
