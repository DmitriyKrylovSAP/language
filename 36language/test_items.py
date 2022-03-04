from selenium import webdriver
import time
import pytest
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('links', ["895", "896", "897", "898", "899", "903", "904", "905"])
def test_ufo(browser, links):
    answer = math.log(int(time.time()))
    link = f"https://stepik.org/lesson/236{links}/step/1"
    browser.get(link)
    browser.implicitly_wait(5)
    browser.find_element_by_class_name("string-quiz__textarea").send_keys(str(answer))
    browser.find_element_by_class_name("submit-submission").click()
    well = browser.find_element_by_class_name("smart-hints__hint").text
    assert well == "Correct!", "значения одинковые"

 







