import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.core import driver

today = datetime.datetime.today()
my_date = today + datetime.timedelta(days=13)
futureDate = my_date.strftime("%d")
if futureDate.startswith("0"):
    futureDate = futureDate[1:2]

# to get YYYY format
future_short_month = my_date.strftime("%b")
future_month = my_date.strftime("%B")[:4]
future_year = my_date.strftime("%Y")
print(futureDate)
print(future_short_month)
print(future_year)
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

num = 0
while True:
    data = driver.find_element(By.XPATH, "//td[@class='monthTitle']").text.split(" ", 2)
    current_focused_month = data[0]
    current_focused_year = data[1]
    print(current_focused_month + " & " + current_focused_year)
    if current_focused_month != future_short_month or current_focused_month != future_month and current_focused_year != future_year:
        driver.find_element(By.XPATH, "//td[@class='next']/button").click()
    else:
        break

driver.find_element(By.XPATH, "//td[text()='" + futureDate + "']").click()
