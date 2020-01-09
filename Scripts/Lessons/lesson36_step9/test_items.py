import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#time.sleep(10)

def test_check_add_to_bucket_button(browser):
    browser.get(link)
    check_message = browser.find_element_by_css_selector("#add_to_basket_form button")
    print("\n", check_message.text)
    assert "Añadir al carrito" in check_message.text, f"Текст сообщения {check_message.text}"
    time.sleep(10)