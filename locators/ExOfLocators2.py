from selenium import webdriver
from selenium.webdriver.common.by import By

cp = webdriver.ChromeOptions()
cp.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=cp)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR, "input[value='radio2']").click()
driver.find_element(By.XPATH, "//input[@id='autocomplete']").click()
data = driver.find_elements(By.TAG_NAME, "a")
print(len(data))
