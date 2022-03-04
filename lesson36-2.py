from selenium import webdriver
import time
import unittest
import pytest

def put(link):
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_class_name("first_block").find_element_by_class_name("first")
    input1.send_keys("12")
    input2 = browser.find_element_by_class_name("first_block").find_element_by_class_name("second")
    input2.send_keys("12")
    input3 = browser.find_element_by_class_name("first_block").find_element_by_class_name("third")
    input3.send_keys("12")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)
    wellkome_text_elt = browser.find_element_by_tag_name("h1")
    wellkome_text = wellkome_text_elt.text
    time.sleep(1)
    browser.quit()
    return wellkome_text

class tests(unittest.TestCase):
    def test_wellkome1(self):
        well = put("http://suninjuly.github.io/registration1.html")
        self.assertEqual("Congratulations! You have successfully registered!", well, "text not found")

    def test_wellkome2(self):
        well2 = put("http://suninjuly.github.io/registration2.html")
        self.assertEqual("Congratulations! You have successfully registered!", well2, "text not found")

if __name__ == "__main__":
    unittest.main()

