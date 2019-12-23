from selenium import webdriver
import chromedriver_binary
import time
import math

# расчет функции
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # переключаемся на другую вкладку
    button = browser.find_element_by_css_selector("button.btn")
   # time.sleep(2) # короче хз, если не редиректит - раскомментируй тайм
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

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