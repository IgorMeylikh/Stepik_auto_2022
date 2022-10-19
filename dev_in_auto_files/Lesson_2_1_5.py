from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Получаем значение Х
    x_value = (browser.find_element(By.ID, 'input_value')).text
    print(x_value)
    # Делаем подсчёт
    calc_result = calc(x_value)



    # Ваш код, который заполняет обязательные поля
    input = browser.find_element(By.ID, 'answer')
    input.send_keys(calc_result)

    # Кликаем по чек боксу
    checkbox = browser.find_element(By.CSS_SELECTOR, '[for ="robotCheckbox"]')
    checkbox.click()

    # Кликаем по радиобаттону
    radiobutton = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
    radiobutton.click()

    time.sleep(3)
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(3)

    # находим элемент, содержащий текст
    # welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    # welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    # assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()