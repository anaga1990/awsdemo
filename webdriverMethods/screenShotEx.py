import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class ExOfScreenShot():

    def exOfShot(self):
        cp = webdriver.ChromeOptions()
        cp.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=cp)
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        screenFileName = "C:/Worldline/Python_workspace/Selenioum4.X/1.png"
        try:
            driver.save_screenshot(screenFileName)
            print("screen shot taken in ==> " + screenFileName)
        except NotADirectoryError:
            print("issue with snapshot")


ex = ExOfScreenShot()
ex.exOfShot()
