from selenium import webdriver
import chromedriver_binary
import time
import math

# расчет функции
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # клик для вызова модалки
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # подтверждаем модалку
    confirm = browser.switch_to.alert
    confirm.accept()

    # находим х, считаем функцию вводим ответ
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()