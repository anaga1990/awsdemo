import os.path
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
        self.takeScreenShot(driver)



    def takeScreenShot(self, driver):
        fileName = str(round(time.time() * 1000))+".png"
        screendir = "C:/Worldline/Python_workspace/Selenioum4.X/"
        if not os.path.isdir(screendir):
            os.makedirs(screendir)
        screenShot = screendir + fileName
        try:
            driver.save_screenshot(screenShot)
            print("screen shot taken in ==> " + screenShot)
        except NotADirectoryError:
            print("issue with snapshot")

ex = ExOfScreenShot()
ex.exOfShot()
