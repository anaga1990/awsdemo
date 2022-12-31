import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

cp = webdriver.ChromeOptions()
cp.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=cp)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
dropdownElement = driver.find_element(By.ID, "dropdown-class-example")
select = Select(dropdownElement)
select.select_by_index(1)
time.sleep(2)
select.select_by_value("option3")
time.sleep(2)
select.select_by_visible_text('Option2')
time.sleep(5)
driver.quit()