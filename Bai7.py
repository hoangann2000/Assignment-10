import unittest
from selenium import webdriver
import time

class Test(unittest.TestCase):
    def testName(self):
        chrome_driver_path = "G:\seledriver\chromedriver.exe"
        driver = webdriver.Chrome(chrome_driver_path)

        driver.get("http://practice.automationtesting.in/")
        title = driver.title
        print('assert title home:')
        self.assertTrue(title == "Automation Practice Site")
        
        driver.find_element_by_link_text("My Account").click()
        
        username = driver.find_element_by_id("reg_email")
        username.send_keys("lcm02180@bcaoo.com")

        passs = driver.find_element_by_id("reg_password")
        passs.send_keys("3KVfE7BvLaTc@7E")

        time.sleep(10)

        driver.find_element_by_name('register').click()
        
        
if  __name__ == "__main__":
    unittest.main()