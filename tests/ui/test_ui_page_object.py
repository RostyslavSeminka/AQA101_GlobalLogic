from modules.ui.page_objects.sign_in_page import SignInPage
import pytest


@pytest.mark.ui
def test_check_incorrect_username_page_object():
    #Створення обєкту сторінки
    sign_in_page = SignInPage()

    #Відкриваємо сторінку "https://github.com/login"
    sign_in_page.go_to()

    #Виконуємо спробу увійти в систему
    sign_in_page.try_login("page_object@testmail.com", "wrong_password")

    #Перевіряємо що назва сторінки є очікуваною
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")

    #Закриваємо браузер
    sign_in_page.close