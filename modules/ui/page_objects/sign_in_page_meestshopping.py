from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class SignInPage(BasePage):
    URL = 'https://web.meest.shopping/login'

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(SignInPage.URL)

    def try_login_for_non_exist_user(self, username, password):
        #Знаходимо поле, в яке будемо вводити неправильний логін
        login_elem = self.driver.find_element(By.NAME, "email")

        #Вводимо неправильний логін
        login_elem.send_keys(username)
    
        #Знаходимо поле, в яке будемо вводити пароль
        pass_elem = self.driver.find_element(By.NAME, "password")

        #Вводимо неправильний пароль
        pass_elem.send_keys(password)

        # Очікуємо завантаження iframe із капчею і переходимо в нього
        WebDriverWait(self.driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[title='reCAPTCHA']"))
            )

        # Очікуємо доступність чекбокса
        checkbox = WebDriverWait(self.driver, 10).until(
             EC.element_to_be_clickable((By.CLASS_NAME, "recaptcha-checkbox-border"))
             )

        #Імітуємо людський рух миші та клік
        actions = ActionChains(self.driver)
        actions.move_to_element(checkbox).pause(1).click().perform()

        # Повертаємось з iframe назад
        self.driver.switch_to.default_content()

        # Чекаємо на результат (за необхідності збільшити якщо з'являється додаткова перевірка капчі)
        time.sleep(35)

        #Шукаємо кнопку "Увійти"
        button_elem = self.driver.find_element(By.CLASS_NAME, "button.btn.button.-primary")

        #Емулюємо клік на кнопку "Увійти"
        button_elem.click()

        # Чекаємо на заголовок у модалці
        modal_title = WebDriverWait(self.driver, 10).until(
             EC.visibility_of_element_located((By.CSS_SELECTOR, "h3.title"))
             )
        
        #Перевіряємо заголовок модалки
        assert modal_title.text.strip() == "Неправильні облікові дані"


    def try_switch_login_to_sso(self):

        #Шукаємо кнопку "Вхід без паролю"
        button_elem = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/section/div/div/main/section/div/div[2]/form/div/a/button")

        #Емулюємо клік на кнопку "Вхід без паролю"
        button_elem.click()

    def check_url(self, expected_url):
        return self.driver.current_url == expected_url
    
    def try_switch_sso_to_login(self):

        #Шукаємо кнопку "Увійти з паролем"
        button_elem = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/section/div/div/main/section/div/div[2]/div/form/div[1]/a/button")

        #Емулюємо клік на кнопку "Увійти з паролем"
        button_elem.click()
        
    def check_url(self, expected_url):
        return self.driver.current_url == expected_url
    

    def get_login_button_text(self):
        login_button = self.driver.find_element(By.CLASS_NAME, "button.btn.button.-primary")
        return login_button.text.strip()

    def switch_language(self):
        wait = WebDriverWait(self.driver, 10)

        # Натискаємо на іконку мови
        language_icon = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "languages-icons")))
        language_icon.click()

        # Чекаємо на появу списку мов
        lang_options = wait.until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "profile-item-name")))

        current_text = self.get_login_button_text()

        if "Увійти" in current_text:
            target_language = "English"
        else:
            target_language = "Українська"

        for option in lang_options:
            if option.text.strip() == target_language:
                option.click()
                break