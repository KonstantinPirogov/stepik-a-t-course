from selenium import webdriver
import chromedriver_binary
import math
import time
import pytest

# фикстура для открытия и закрытия браузера
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()


# фикстура для расчета ответа
@pytest.fixture(scope="function")
def prepare_data():
    answer = math.log(int(time.time()))
    answer_string = str(answer)
    return answer_string

@pytest.mark.parametrize('pages', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_pages(browser, pages, prepare_data):
    link = f"https://stepik.org/lesson/{pages}/step/1"
    browser.get(link)
    input1 = browser.find_element_by_css_selector(".ember-text-area")
    input1.send_keys(prepare_data)
    button = browser.find_element_by_css_selector(".submit-submission")
    button.click()
    check_message = browser.find_element_by_css_selector(".ember-view pre")
    print("\n", check_message.text)
    assert "Correct!" in check_message.text, f"Текст сообщения {check_message.text}"
