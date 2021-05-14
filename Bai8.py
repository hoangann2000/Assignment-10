import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Test(unittest.TestCase):
    def testName(self):
        chrome_driver_path = "G:\seledriver\chromedriver.exe"
        driver = webdriver.Chrome(chrome_driver_path)

        driver.get("https://the-internet.herokuapp.com/")
        title = driver.title
        print('assert title home:')
        self.assertTrue(title == "The Internet")
        
        driver.find_element_by_link_text("Form Authentication").click()
        
        username = driver.find_element_by_name("username")
        username.send_keys("tomsmith")

        passs = driver.find_element_by_name("password")
        passs.send_keys("SuperSecretPassword!")

        passs.send_keys(Keys.ENTER)

        print(driver.title) 
        
        
        
        
if  __name__ == "__main__":
    unittest.main()