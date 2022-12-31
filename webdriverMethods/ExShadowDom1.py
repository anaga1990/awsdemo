import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://selectorshub.com/xpath-practice-page/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.set_page_load_timeout(30)
time.sleep(3)
shadow_host = driver.find_element(By.CSS_SELECTOR, "#userName").shadow_root
shadow_host.find_element(By.CSS_SELECTOR, "#kils").send_keys("NAGA")
time.sleep(30)
