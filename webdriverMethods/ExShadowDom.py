import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://selectorshub.com/xpath-practice-page/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.set_page_load_timeout(30)
time.sleep(3)
shadow_host = driver.find_element(By.CSS_SELECTOR, "#userName")
script = 'return arguments[0].shadowRoot'
shadow_root = driver.execute_script(script, shadow_host)
shadow_root.find_element(By.CSS_SELECTOR, "#kils").send_keys("NAGA")
time.sleep(30)
