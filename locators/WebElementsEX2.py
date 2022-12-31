from selenium import webdriver
from selenium.webdriver.common.by import By

cp = webdriver.ChromeOptions()
cp.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=cp)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.ID, "autocomplete").send_keys("in")
listOfRadio = driver.find_elements(By.XPATH, "//input[contains(@value,'radi')]")
sizeOfElements = len(listOfRadio)
print("auto suggest DropDown size => " + str(sizeOfElements))
for a in listOfRadio:
    is_been_selected = a.is_selected()
    if not is_been_selected:
        a.click()

driver.quit()