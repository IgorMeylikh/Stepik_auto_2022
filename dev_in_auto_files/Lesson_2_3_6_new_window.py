from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button_first = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button_first.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

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