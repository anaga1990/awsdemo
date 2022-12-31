from selenium import webdriver

edgeOptions=webdriver.EdgeOptions()
edgeOptions.add_experimental_option("detach", True)
#edgeOptions.add_argument("--headless")
driver=webdriver.Edge(options=edgeOptions)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
