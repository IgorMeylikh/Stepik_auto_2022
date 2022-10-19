from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input_value = browser.find_element(By.ID, 'input_value')
    input_value = int(input_value.text)
    print(input_value)

    result = calc(input_value)

    input = browser.find_element(By.ID, 'answer')
    input.send_keys(result)

    # Кликаем по чекбоксу
    iAmTheRobot = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
    iAmTheRobot.click()

    # Делвем скролл до кнопки Submit, так как рядом с ней радиобаттон нам нужный
    # Можно было бы до радиобаттона проекрутить
    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    # Кликаем по радиобаттону
    robotsRule = browser.find_element(By.CSS_SELECTOR, '[for ="robotsRule"]')
    robotsRule.click()


    time.sleep(1)
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