import datetime

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

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
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
ActionChains(driver).scroll_by_amount(0, 200).perform()
driver.find_element(By.XPATH,"//input[@id='dob']").click()
calendar_month=driver.find_element(By.CSS_SELECTOR, "select.ui-datepicker-month")
select=Select(calendar_month)
select.select_by_visible_text("Nov")

calendar_year=driver.find_element(By.CSS_SELECTOR, "select.ui-datepicker-year")
select=Select(calendar_year)
select.select_by_visible_text("1990")
driver.find_element(By.XPATH, "//a[contains(text(),'19')]").click()
