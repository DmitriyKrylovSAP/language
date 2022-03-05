link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
def test_search_busket_button(browser):
    browser.get(link)
    assert len(browser.find_elements_by_class_name("btn-add-to-basket")) > 0,  "Кнопка не найдена"
    browser.quit()