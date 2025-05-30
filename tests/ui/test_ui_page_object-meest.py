from modules.ui.page_objects.sign_in_page_meestshopping import SignInPage
import pytest
import time


@pytest.mark.meest
def test_check_incorrect_username_page_object():
    #Створення обєкту сторінки
    sign_in_page = SignInPage()

    #Відкриваємо сторінку
    sign_in_page.go_to()

    #Очікуємо поки повністю завантажиться сторінка
    time.sleep(3)

    #Виконуємо спробу увійти в систему під кредами юзера якого немає
    sign_in_page.try_login_for_non_exist_user("page_object@testmail.com", "wrong_password")

    #Закриваємо браузер
    sign_in_page.close

@pytest.mark.meest
def test_switch_login_to_sso():
    #Створення обєкту сторінки
    sign_in_page = SignInPage()

    #Відкриваємо сторінку
    sign_in_page.go_to()

    #Очікуємо поки повністю завантажиться сторінка
    time.sleep(3)

    sign_in_page.try_switch_login_to_sso()

    #Перевіряємо що назва сторінки є очікуваною
    assert sign_in_page.check_url("https://web.meest.shopping/sso-login")

    sign_in_page.try_switch_sso_to_login()

    #Перевіряємо що назва сторінки є очікуваною
    assert sign_in_page.check_url("https://web.meest.shopping/login")

@pytest.mark.meest
def test_language_switching_by_login_button_text():
    sign_in_page = SignInPage()
    sign_in_page.go_to()
    #Очікуємо поки повністю завантажиться сторінка
    time.sleep(3)

    #Визначаємо мову сторінки за текстом в кнопці
    first_lang = sign_in_page.get_login_button_text()

    #Змінюємо мову
    sign_in_page.switch_language()
    
    time.sleep(3)

    #Перевіряємо що мова змінилась
    second_lang = sign_in_page.get_login_button_text()
    assert first_lang != second_lang