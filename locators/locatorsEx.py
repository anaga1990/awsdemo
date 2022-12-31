import time

from selenium import webdriver
from selenium.webdriver.common.by import By

chromeOptions=webdriver.ChromeOptions()
chromeOptions.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=chromeOptions)
driver.maximize_window()
driver.implicitly_wait(10)
driver.set_page_load_timeout(30)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
elementByID=driver.find_element(By.ID, "checkBoxOption1")
if elementByID is not None:
    print("elementByID -->")
    print(elementByID)

driver.find_element(By.NAME, "checkBoxOption1").click()
driver.find_element(By.CLASS_NAME, "radioButton").click()
driver.find_element(By.CSS_SELECTOR, "#autocomplete").send_keys("india")
driver.find_element(By.XPATH, "//input[@value='option2']").click()
driver.find_element(By.LINK_TEXT,"Home").click()
time.sleep(10)
driver.quit()