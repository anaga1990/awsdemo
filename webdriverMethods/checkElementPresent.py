from selenium import webdriver
from selenium.webdriver.common.by import By


def is_element_present(self, element):
    self.element = element
    try:
        if element is not None:
            print("element found")
            return True
        else:
            return False
    except:
        print("element not Found")
        return False


def element_present_or_not(self, elements):
    try:
        if len(elements) > 0:
            print("element found")
            return True
        else:
            print("element not Found")
            return False
    except:
        print("element not found")
        return False


class Test(object):
    def test(self):
        cp = webdriver.ChromeOptions()
        cp.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=cp)
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        driver.find_element(By.XPATH, "//input[@id='hide-textbox']").click()
        element = driver.find_element(By.XPATH, "//input[@id='displayed-text']")
        is_available = self.is_element_present(element)
        print(is_available)


tc = Test()
tc.test()
