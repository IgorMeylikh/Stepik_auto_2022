from selenium import webdriver
from selenium.webdriver.common.by import By

def test_registration_1():
    browser = webdriver.Chrome()
    link_1 = "http://suninjuly.github.io/registration1.html"
    browser.get(link_1)

    # Ваш код, который заполняет обязательные поля
    first_field = browser.find_element(By.XPATH, "//input[@placeholder = 'Input your first name']")
    first_field.send_keys("First name")
    second_field = browser.find_element(By.XPATH, "//input[@placeholder = 'Input your last name']")
    second_field.send_keys("Last name")
    third_field = browser.find_element(By.XPATH, "//input[@placeholder = 'Input your email']")
    third_field.send_keys("mail@mail.ru")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы


    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    assert welcome_text == "Congratulations! You have successfully registered!", "Error_1"

def test_registration_2():
    browser = webdriver.Chrome()
    link_2 = "http://suninjuly.github.io/registration2.html"
    browser.get(link_2)
    # Ваш код, который заполняет обязательные поля
    first_field = browser.find_element(By.XPATH, "//input[@placeholder = 'Input your name']")
    first_field.send_keys("First name")

    second_field = browser.find_element(By.XPATH, "//input[@placeholder = 'Input your last name']")
    second_field.send_keys("Last name")

    third_field = browser.find_element(By.XPATH, "//input[@placeholder = 'Input your email']")
    third_field.send_keys("mail@mail.ru")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы


    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    assert welcome_text == "Congratulations! You have successfully registered!", "Error_2"






