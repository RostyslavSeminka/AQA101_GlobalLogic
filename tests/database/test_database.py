import pytest
from modules.common.database import Database


@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()


@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()

    print(users)


@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user = db.get_user_address_by_name('Sergii')

    assert user[0][0] == 'Maydan Nezalezhnosti 1'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '3127'
    assert user[0][3] == 'Ukraine'


@pytest.mark.database
def test_productqnt_update():
    db = Database()
    db.update_product_qnt_by_id(1, 25)
    water_qnt = db.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25


@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, 'Печиво', 'Солодке', 30)
    water_qnt = db.select_product_qnt_by_id(4)

    assert water_qnt [0][0] == 30


@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, 'Тест', 'ТестовийОпис', 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)

    assert len(qnt) == 0


@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    print("Замовлення", orders)
    # Перевірка що кількість замовленнь рівне "1"
    assert len(orders) == 1

    # Перевірка структури даних
    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'
    assert orders[0][2] == 'солодка вода'
    assert orders[0][3] == 'з цукром'


@pytest.mark.database
def test_user_list_is_not_empty():
    db = Database()
    users = db.get_all_users()
    assert len(users) >= 1
    #Перевірка що повертається хочаб 1 юзер


@pytest.mark.database
def test_get_user_not_exist_():
    db = Database()
    result = db.get_user_address_by_name('Anatoliiii')
    assert result == []
    #Перевірка повернення пустого списку при виклику за неймом неіснуючого юзера


@pytest.mark.database
def test_update_big_qnt():
    db = Database()
    db.insert_product(66, 'Сірники', 'Поштучно', 100)
    db.update_product_qnt_by_id(66, 1000000000000000)
    qnt = db.select_product_qnt_by_id(66)
    assert qnt[0][0] == 1000000000000000
    #Перевірка апдейту на дуууже велику кількість товару


@pytest.mark.database
def test_product_names_is_not_empty():
    db = Database()
    orders = db.get_detailed_orders()
    for order in orders:
        assert order[2] != ''
    #Перевірка що заповнені всі назви товарів


@pytest.mark.database
def test_insert_product_not_in_stock():
    db = Database()
    db.insert_product(33, 'Товару немає на складі', 'Очікуйте поставку', 0)
    qnt = db.select_product_qnt_by_id(33)
    assert qnt[0][0] == 0
    #Перевірка що запишеться товар із нульовою кількістю
