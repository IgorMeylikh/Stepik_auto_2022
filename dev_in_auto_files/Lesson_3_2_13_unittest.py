from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time



try:
    class TestRegistration(unittest.TestCase):
        def test_registration_1(self):
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
            self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Error_1")

        def test_registration_2(self):
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
            self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Error_2")


    if __name__ == "__main__":
        unittest.main()
finally:
    time.sleep(5)
    browser.quit()




