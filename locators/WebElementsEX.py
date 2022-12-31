from selenium import webdriver
from selenium.webdriver.common.by import By

cp = webdriver.ChromeOptions()
cp.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=cp)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.ID, "autocomplete").send_keys("in")
listOfCountries = driver.find_elements(By.CSS_SELECTOR, "ul.ui-autocomplete li div")
sizeOfElements = len(listOfCountries)
print("auto suggest DropDown size => " + str(sizeOfElements))
for country in listOfCountries:
    print(country.text)
