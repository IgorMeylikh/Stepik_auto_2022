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

    # peopleRule = browser.find_element(By.ID, 'peopleRule')
    peopleRule = browser.find_element(By.ID, 'robotsRule')
    peopleRuleState = peopleRule.get_attribute("checked")

    # Ваш код, который заполняет обязательные поля
    # input = browser.find_element(By.ID, 'answer')
    # input.send_keys(peopleRuleState)

    print("value of people radio: ", peopleRuleState)
    # assert peopleRuleState, 'People radio is not selected by default'
    assert peopleRuleState is not None, "People radio is not selected by default"
    # assert peopleRuleState == "true", "People radio is not selected by default"

    # time.sleep(3)
    # Отправляем заполненную форму
    # button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    # button.click()

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
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()