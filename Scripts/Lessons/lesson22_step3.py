from selenium import webdriver
from selenium.webdriver.support.ui import Select
import chromedriver_binary
import time
import math


try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # находим х и у, складываем
    x_element = browser.find_element_by_id('num1')
    x = x_element.text
    y_element = browser.find_element_by_id('num2')
    y = y_element.text
    num1 = int(x)
    num2 = int(y)
    result = num1 + num2
    sum12 = str(result)

    # находим нужное значение в дропдауне
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(sum12)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()