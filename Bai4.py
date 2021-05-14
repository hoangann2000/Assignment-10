import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        chrome_driver_path = "G:\seledriver\chromedriver.exe"
        driver = webdriver.Chrome(chrome_driver_path)

        driver.get("http://practice.automationtesting.in/")
        title = driver.title
        driver.maximize_window()

        print(title)
        self.assertTrue(title == "Automation Practice Site")
        
if  __name__ == "__main__":
    unittest.main()