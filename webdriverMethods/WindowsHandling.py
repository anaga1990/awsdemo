from selenium import webdriver
from selenium.webdriver.common.by import By

cp = webdriver.ChromeOptions()
cp.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=cp)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.ID, "openwindow").click()
mainWindow = driver.current_window_handle
allWindows = len(driver.window_handles)
print("**********************" + str(allWindows))
for currentWindow in driver.window_handles:
    if currentWindow != mainWindow:
        driver.switch_to.window(currentWindow)

print(str(driver.title))
driver.close()
driver.switch_to.window(mainWindow)
print("MAIN WINDOW TITLE ==> "+str(driver.title))
driver.quit()

