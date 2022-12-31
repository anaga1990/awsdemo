from selenium import webdriver
from selenium.webdriver.common.by import By

cp = webdriver.ChromeOptions()
cp.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=cp)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.XPATH, "//input[@id='autocomplete']").send_keys("in")
listData = driver.find_elements(By.XPATH, "//li[@class='ui-menu-item']/div")
for data in listData:
    if data.text == "India":
        data.click()
        break

driver.find_element(By.XPATH, "//input[@id='checkBoxOption2']").click()
