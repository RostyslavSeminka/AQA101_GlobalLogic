import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
#import time


@pytest.mark.ui
def test_check_incorrect_username():
    #Створення об'єкту для керування браузером
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    #Відкриваємо сторінку GitHub
    driver.get("https://github.com/login")

    #Знаходимо поле, в яке будемо вводити неправильний логін
    login_elem = driver.find_element(By.ID, "login_field")

    #Вводимо неправильний логін
    login_elem.send_keys("abbrakadabraaaaaaa@testmail.com")
    
    #Знаходимо поле, в яке будемо вводити пароль
    pass_elem = driver.find_element(By.ID, "password")

    #Вводимо неправильний пароль
    pass_elem.send_keys("wrong_password")
    
    #Шукаємо кнопку Sign-In
    button_elem = driver.find_element(By.NAME, "commit")

    #Емулюємо клік на кнопку Sign-In
    button_elem.click()
    #time.sleep(3)

    #Перевіряємо що назва сторінки та, на яку ми очікували
    assert driver.title == "Sign in to GitHub · GitHub"

    #Закриваємо браузер
    driver.close()