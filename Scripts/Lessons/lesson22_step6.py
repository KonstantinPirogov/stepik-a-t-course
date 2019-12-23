from selenium import webdriver
import chromedriver_binary
import time
import math

# расчет функции
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # находим х, считаем функцию вводим ответ
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)

    # скроллим попиксельно
    browser.execute_script("window.scrollBy(0, 120);")

    # ищем чекбокс и кликаем
    option1 = browser.find_element_by_id('robotCheckbox')
    option1.click()

    # ищем радиобаттон и кликаем
    option1 = browser.find_element_by_id('robotsRule')
    option1.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()