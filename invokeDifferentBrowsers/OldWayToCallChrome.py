import time

from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\Worldline\Selenium_Dir\Ext_lib\chromedriver108.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.set_page_load_timeout(30)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(10)