from selenium import webdriver
from selenium.webdriver.common.by import By

cp = webdriver.ChromeOptions()
cp.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=cp)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.XPATH, "//input[@id='name']").send_keys("naga")
driver.find_element(By.XPATH, "//input[@id='alertbtn']").click()
alertText = driver.switch_to.alert.text
print("**************************" + str(alertText))
driver.switch_to.alert.accept()
driver.find_element(By.XPATH, "//input[@id='name']").send_keys("python")
driver.find_element(By.XPATH, "//input[@id='alertbtn']").click()
alertText = driver.switch_to.alert.text
print("--------------------" + str(alertText))
driver.switch_to.alert.dismiss()
driver.quit()
