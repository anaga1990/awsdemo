import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.set_page_load_timeout(30)
driver.implicitly_wait(10)
driver.delete_all_cookies()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.find_element(By.CSS_SELECTOR, "input[value='radio3']").click()
driver.find_element(By.XPATH, "//input[@id='autocomplete']").send_keys("ind")
time.sleep(10)