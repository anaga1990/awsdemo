import time

from selenium import webdriver
from selenium.webdriver.common.by import By

cp = webdriver.ChromeOptions()
cp.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=cp)
driver.maximize_window()
driver.delete_all_cookies()
driver.set_page_load_timeout(30)
driver.implicitly_wait(10)
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")

'''
javascript for openURL
'''
driver.execute_script("window.location = 'https://rahulshettyacademy.com/AutomationPractice/';")
driver.find_element(By.XPATH, "//input[@id='autocomplete']").send_keys("in")

''' Scroll to elemnet location using javaScript'''
driver.execute_script("arguments[0].scrollIntoView()", driver.find_element(By.XPATH, "//div[@class='totalAmount']"))
time.sleep(10)

'''
    type something in textbox
'''
driver.execute_script("arguments[0].value='india';",driver.find_element(By.XPATH, "//input[@id='autocomplete']"))

''' 
    click using javaScript
'''
driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, "//input[@value='radio3']"))

'''
    scroll By will scroll every time  
'''
driver.execute_script("window.scrollBy(0,200)")
time.sleep(1)
driver.execute_script("window.scrollBy(0,200)")
time.sleep(1)
driver.execute_script("window.scrollBy(0,200)")
time.sleep(1)
'''
    scrollTo Method will scroll only once
'''
driver.execute_script("window.scrollTo(0,200)")

