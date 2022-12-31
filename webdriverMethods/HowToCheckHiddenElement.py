from selenium import webdriver
from selenium.webdriver.common.by import By

cp = webdriver.ChromeOptions()
cp.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=cp)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.XPATH,"//input[@id='hide-textbox']").click()
data=driver.find_element(By.XPATH,"//input[@id='displayed-text']").get_attribute("style")
if data.__contains__('none'):
    print('=>>>>>>> element hidden')
else:
    print("==>>> element displayed")
    driver.find_element(By.XPATH, "//input[@id='displayed-text']").send_keys("nana")