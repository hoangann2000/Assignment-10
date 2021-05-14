import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select

class Test(unittest.TestCase):
    def testName(self):
        chrome_driver_path = "G:\seledriver\chromedriver.exe"
        driver = webdriver.Chrome(chrome_driver_path)

        driver.get("https://itmscoaching.herokuapp.com/form")
        title = driver.title
        self.assertTrue(title == "Formy")
        
        firstname = driver.find_element_by_id("first-name")
        firstname.send_keys("Binh")

        time.sleep(1)

        lastname = driver.find_element_by_id("last-name")
        lastname.send_keys("Nguyen")

        time.sleep(1)

        job = driver.find_element_by_id("job-title")
        job.send_keys("Tester")

        time.sleep(1)

        driver.find_element_by_css_selector("input#radio-button-3").click() 

        time.sleep(1)

        driver.find_element_by_css_selector("input#checkbox-2").click() 

        time.sleep(1)

        select = Select(driver.find_element_by_id('select-menu'))
        select.select_by_value('3')

        time.sleep(1)

        day = driver.find_element_by_id("datepicker")
        day.send_keys("7/20/2011")

        time.sleep(1)

        driver.find_element_by_link_text("Submit").click()

        time.sleep(5)
        
        
        
        
        
if  __name__ == "__main__":
    unittest.main()