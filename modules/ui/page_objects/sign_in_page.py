from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class SignInPage(BasePage):
    URL = 'https://github.com/login'

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(SignInPage.URL)

    def try_login(self, username, password):
        #Знаходимо поле, в яке будемо вводити неправильний логін
        login_elem = self.driver.find_element(By.ID, "login_field")

        #Вводимо неправильний логін
        login_elem.send_keys(username)
    
        #Знаходимо поле, в яке будемо вводити пароль
        pass_elem = self.driver.find_element(By.ID, "password")

        #Вводимо неправильний пароль
        pass_elem.send_keys(password)
    
        #Шукаємо кнопку Sign-In
        button_elem = self.driver.find_element(By.NAME, "commit")

        #Емулюємо клік на кнопку Sign-In
        button_elem.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title