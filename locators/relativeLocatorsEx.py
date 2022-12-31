import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chromeOptions)
driver.maximize_window()
driver.implicitly_wait(10)
driver.set_page_load_timeout(30)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
relocate = locate_with(By.XPATH, "//input[@value='radio3']").below({By.XPATH: "//input[@value='radio2']"})
driver.find_element(relocate).click()
time.sleep(3)
relocate = locate_with(By.XPATH, "//input[@value='radio1']").above({By.XPATH: "//input[@value='radio2']"})
driver.find_element(relocate).click()
time.sleep(10)
driver.quit()
