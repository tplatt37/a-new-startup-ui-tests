"""
UI Tests for A New Startup application.
A simple selenium test example written in python
"""

import unittest
import time
import string
import random
import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import sys

class TestTemplate(unittest.TestCase):
    """Include test cases on a given url"""

    def setUp(self):
        """Start web driver"""
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--disable-dev-shm-usage");
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(10)
    
    def tearDown(self):
        """Stop web driver"""
        self.driver.quit()
    
    def test_case_1(self):
        """Submit duplicate name and email for updates"""
        try:
            
            print("TEST URL=", os.environ['URL'])
            
            self.driver.get(os.environ['URL'])
            
            # Click the "Sign up today" link and submit details.
            el = self.driver.find_element(By.CLASS_NAME, 'btn-success')
            el.click()
            self.driver.find_element(By.ID, 'name').send_keys("function test")
            self.driver.find_element(By.NAME, 'email').send_keys("test@example.com")
            el = self.driver.find_element(By.CLASS_NAME, 'btn-primary')
            el.click()
            
            print("Sleeping...wait 3 seconds for status to update.")
            time.sleep(3)
            
            # If the user is already in the list, the signupDuplicate
            # div becomes visible by clearing the style. 
            # We expect this to happen, and this tells us the post worked
            # and the database was checked successfully.
            eld = self.driver.find_element(By.ID, "signupDuplicate")
            if eld.get_attribute("style") != "display: none":
                print("signupDuplicate is displayed")
            else:
                print("signupDuplicate is not displayed")
                
            self.assertTrue(self.driver.find_element(By.ID,"signupDuplicate").get_attribute("style") != "display:none;")
            
            
            # Sometimes, an error can happen, and if so, it will be displayed.
            ele = self.driver.find_element(By.ID, "signupError")
            if ele.get_attribute("style") != "display: none;":
                print("signupError is displayed")
            else:
                print("signupError is not displayed")
                
            self.assertFalse(self.driver.find_element(By.ID,"signupError").get_attribute("style") == "display:none;")
            
            # If Sign up email was unique, this will be displayed with a success message.
            els = self.driver.find_element(By.ID,"signupSuccess")
            if els.get_attribute("style") != "display: none;":
                print("signupSuccess is displayed")
            else:
                print("signupSuccess is not displayed")
            
        except NoSuchElementException as ex:
            self.fail(ex.msg)
            
    def test_case_2(self):
        """Submit unique email address for updates"""
        try:
            
            print("TEST URL=", os.environ['URL'])
            
            self.driver.get(os.environ['URL'])
            
            # Click the "Sign up today" link and submit details.
            el = self.driver.find_element(By.CLASS_NAME,'btn-success')
            el.click()
            self.driver.find_element(By.ID,"name").send_keys("function test")
          
            # Generate a random email address - should succeed most times. 
            letters = string.ascii_lowercase
            randomemail = "test" + ''.join(random.choice(letters) for i in range(6)) + "@example.com"
            print("Random Email=",randomemail)
            self.driver.find_element(By.NAME,"email").send_keys(randomemail)
            
            el = self.driver.find_element(By.CLASS_NAME,'btn-primary')
            el.click()
            
            print("Sleeping...wait 3 seconds for status to update.")
            time.sleep(3)
            
            eld = self.driver.find_element(By.ID,"signupDuplicate")
            if eld.get_attribute("style") != "display: none":
                print("signupDuplicate is displayed")
            else:
                print("signupDuplicate is not displayed")
            
            # Sometimes, an error can happen, and if so, it will be displayed.
            ele = self.driver.find_element(By.ID,"signupError")
            if ele.get_attribute("style") != "display: none;":
                print("signupError is displayed")
            else:
                print("signupError is not displayed")
                
            self.assertFalse(self.driver.find_element(By.ID,"signupError").get_attribute("style") == "display:none;")
            
            
            # If Sign up email was unique, this will be displayed with a success message.
            # This is what we expect in this test case.
            els = self.driver.find_element(By.ID,"signupSuccess")
            if els.get_attribute("style") != "display: none;":
                print("signupSuccess is displayed")
            else:
                print("signupSuccess is not displayed")
                
            self.assertTrue(self.driver.find_element(By.ID,"signupSuccess").get_attribute("style") != "display:none;")
            
        except NoSuchElementException as ex:
            self.fail(ex.msg)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    testloader = unittest.TestLoader()
    testnames = testloader.getTestCaseNames(TestTemplate)
    for name in testnames:
        suite.addTest(TestTemplate(name))
    runner = unittest.TextTestRunner(verbosity=2)
    testResult=runner.run(suite)
    print(testResult)
    #
    # We exit with non-0 if any tests failed.
    # This will be the return code that "docker run" returns - so we can fail the build.
    sys.exit(not testResult.wasSuccessful())
    