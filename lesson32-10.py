from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
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
    assert "Congratulations! You have successfully registered!" == wellkome_text
finally:
    time.sleep(5)
    browser.quit()

