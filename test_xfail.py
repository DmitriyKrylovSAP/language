from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

url = "http://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome(executable_path=r"E:\Programmaz\chromedriver\chromedriver.exe")
    browser.get(url)

    input1 = browser.find_element_by_css_selector('div.first_block div.first_class input')
    input1.send_keys('Пудге')
    try:
        input2 = browser.find_element_by_css_selector('div.first_block div.second_class input')
        input2.send_keys('Фрешмитов')
    except NoSuchElementException:
        pass
    input3 = browser.find_element_by_css_selector('div.first_block div.third_class input')
    input3.send_keys('pudge2004@mail.ru')
    input4 = browser.find_element_by_css_selector('div.second_block div.first_class input')
    input4.send_keys('+623528255226')
    input5 = browser.find_element_by_css_selector('div.second_block div.second_class input')
    input5.send_keys('Улица Пушкина, Дом Колотушкина')
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    time.sleep(10)
    browser.quit()
