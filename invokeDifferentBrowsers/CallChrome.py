from selenium import webdriver

options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--headless")
driver=webdriver.Chrome(options=options)
driver.maximize_window()
print("Chrome is called")
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#driver.quit()
