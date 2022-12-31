from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

co = webdriver.ChromeOptions()
co.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=co)
driver.maximize_window()
driver.set_page_load_timeout(30)
# driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/client/")
driver.find_element(By.ID, "userEmail").send_keys("nagarjuna1990@gmail.com")
driver.find_element(By.ID, "userPassword").send_keys("Test@2889")
driver.find_element(By.ID, "login").click()
subDriver=driver.find_element(By.XPATH, "//b[contains(text(),'zara coat 3')]/parent::h5/parent::div")
wait = WebDriverWait(subDriver, 15)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Add To Cart')]")))
subDriver.find_element(By.XPATH, "//button[contains(text(),'Add To Cart')]").click()


