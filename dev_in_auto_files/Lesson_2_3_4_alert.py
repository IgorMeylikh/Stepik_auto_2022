from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button_first = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button_first.click()

    alert_window = browser.switch_to.alert
    alert_window.accept()

    input_value = browser.find_element(By.ID, 'input_value')
    input_value = int(input_value.text)

    result = calc(input_value)

    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(result)

    time.sleep(1)

    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')

    # Отправляем заполненную форму

    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(3)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()