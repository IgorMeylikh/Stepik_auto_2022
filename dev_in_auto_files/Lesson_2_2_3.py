from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, 'num1')
    num1 = int(num1.text)
    print(num1)

    num2 = browser.find_element(By.ID, 'num2')
    num2 = int(num2.text)
    print(num2)
    result = num1 + num2

    print(result)

    select = Select(browser.find_element(By.ID, 'dropdown'))
    select.select_by_value(str(result))

    time.sleep(3)
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(3)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()