import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.core import driver

today = datetime.datetime.today()
my_date = today + datetime.timedelta(days=30)
futureDate = my_date.strftime("%d")
# to get Mmm YYYY format
future_month_year = my_date.strftime("%b %Y")
print(futureDate)
print(future_month_year)

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.delete_all_cookies()
driver.set_page_load_timeout(30)
driver.implicitly_wait(10)
driver.get("https://www.redbus.in/")
driver.find_element(By.XPATH, "//label[normalize-space()='Date']").click()
print(driver.find_element(By.XPATH, "//td[@class='monthTitle']").text)

while driver.find_element(By.XPATH, "//td[@class='monthTitle']").text != future_month_year:
    driver.find_element(By.XPATH, "//td[@class='next']/button").click()

driver.find_element(By.XPATH,"//td[text()='"+futureDate+"']").click()



