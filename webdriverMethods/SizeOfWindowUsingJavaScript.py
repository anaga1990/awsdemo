import time

from selenium import webdriver
from selenium.webdriver.common.by import By

cp = webdriver.ChromeOptions()
cp.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=cp)
driver.maximize_window()
driver.delete_all_cookies()
driver.set_page_load_timeout(30)
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

height = driver.execute_script("return window.innerHeight;")
width = driver.execute_script("return window.innerWidth;")
print(height)
print(width)

driver.quit()

