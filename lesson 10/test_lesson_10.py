import allure
import pytest
from EmployeeApi import EmployeeApi
from EmployeeTable import EmployeeTable

api = EmployeeApi("http://5.101.50.27:8000")
db = EmployeeTable("postgresql://qa:skyqa@5.101.50.27:5432/x_clients")

@allure.title("Получение данных о сотруднике")
@allure.description("")
@allure.feature("READ")
@allure.severity("CRITICAL")
def test_get_employee():
    employee_id = 1
    with allure.step("Получить данные о сотруднике через API"):
        api_result = api.get_employee(employee_id)
    with allure.step("Получить данные о сотруднике из БД"):
        db_result = db.get_employee(employee_id)
    with allure.step("Сравнить имена полученных сотрудников"):
        assert api_result["first_name"] == db_result[0]["first_name"]

@allure.title("Получение данных о сотруднике без его ID")
@allure.description("")
@allure.feature("READ")
@allure.severity("MINOR")
def test_get_employee_without_employee_id():
    with pytest.raises(TypeError):
        with allure.step("Получить данные о сотруднике без его ID"):
            api.get_employee()

@allure.title("Создание сотрудника")
@allure.description("")
@allure.feature("CREATE")
@allure.severity("BLOCKER")
def test_create_employee():
    with allure.step("Создать сотрудника через API"):
        api_result = api.create_employee("Данил", "Стафейчук", "Романович", 2, "stafeychuk@gmail.com", "+79999999999", "1997-08-16", False)
    with allure.step("Получить данные о сотруднике из БД"):
        db_result = db.get_employee(api_result["id"])
    with allure.step("Сравнить имена созданного и полученного сотрудников"):
        assert api_result["first_name"] == db_result[0]["first_name"]
    with allure.step("Сравнить фамилии созданного и полученного сотрудников"):
        assert api_result["last_name"] == db_result[0]["last_name"]
    with allure.step("Сравнить отчества созданного и полученного сотрудников"):
        assert api_result["middle_name"] == db_result[0]["middle_name"]
    with allure.step("Сравнить ID компаний созданного и полученного сотрудников"):
        assert api_result["company_id"] == db_result[0]["company_id"]
    with allure.step("Сравнить email созданного и полученного сотрудников"):
        assert api_result["email"] == db_result[0]["email"]
    with allure.step("Сравнить номера телефонов созданного и полученного сотрудников"):
        assert api_result["phone"] == db_result[0]["phone"]
    with allure.step("Сравнить даты рождения созданного и полученного сотрудников"):
        assert api_result["birthdate"] == str(db_result[0]["birthdate"])
    with allure.step("Сравнить активность компаний созданного и полученного сотрудников"):
        assert api_result["is_active"] == db_result[0]["is_active"]
    with allure.step("Удалить сотрудника из БД"):
        db.delete(api_result["id"])

@allure.title("Создание сотрудника без тела запроса")
@allure.description("")
@allure.feature("CREATE")
@allure.severity("MINOR")
def test_create_employee_without_body():
     with pytest.raises(TypeError):
        with allure.step("Создать сотрудника без тела запроса"):
            api.create_employee()

@allure.title("Получение списка сотрудников компании")
@allure.description("")
@allure.feature("READ")
@allure.severity("CRITICAL")
def test_get_employee_list():
    company_id = 1
    with allure.step("Получить список сотрудников компании через API"):
        api_result = api.get_employee_list(company_id)
    with allure.step("Получить список сотрудников компании из БД"):
        db_result = db.get_employee_list(company_id)
    with allure.step("Сравнить ID первых сотрудников из списка"):
        assert api_result[0]["id"] == db_result[0]["id"]

@allure.title("Получение списка сотрудников компании без ее ID")
@allure.description("")
@allure.feature("READ")
@allure.severity("MINOR")
def test_get_employee_list_without_company_id():
    with pytest.raises(TypeError):
        with allure.step("Получить список сотрудников компании без ее ID"):
            api.get_employee_list()

@allure.title("Изменение информации о сотруднике")
@allure.description("")
@allure.feature("UPDATE")
@allure.severity("BLOCKER")
def test_change_employee():
    token = {}
    with allure.step("Получить токен авторизации"):
        token["client_token"] = api.get_token()
    with allure.step("Создать сотрудника через API"):
        api_result = api.create_employee("Данил", "Стафейчук", "Романович", 2, "stafeychuk@gmail.com", "+79999999999", "1997-08-16", False)
    with allure.step("Изменить информацию о сотруднике через API"):
        api_change_result = api.change_employee(api_result["id"], token, "Петров","petrov@gmail.com","+70000000001", False)
    with allure.step("Получить данные о сотруднике из БД"):
        db_result = db.get_employee(api_result["id"])
    with allure.step("Сравнить фамилии измененного и полученного сотрудников"):
        assert api_change_result["last_name"] == db_result[0]["last_name"]
    with allure.step("Сравнить email измененного и полученного сотрудников"):
        assert api_change_result["email"] == db_result[0]["email"]
    with allure.step("Сравнить номера телефонов измененного и полученного сотрудников"):
        assert api_change_result["phone"] == db_result[0]["phone"]
    with allure.step("Сравнить активность компаний измененного и полученного сотрудников"):
        assert api_change_result["is_active"] == db_result[0]["is_active"]
    with allure.step("Удалить сотрудника из БД"):
        db.delete(api_result["id"])

@allure.title("Изменение информации о сотруднике без токена авторизации")
@allure.description("")
@allure.feature("UPDATE")
@allure.severity("MINOR")
def test_change_employee_without_token():
    with pytest.raises(TypeError):
        with allure.step("Изменить информацию о сотруднике без токена авторизации"):
            api.change_employee(1, "Петров","petrov@gmail.com","+70000000001", False)

@allure.title("Изменение информации о сотруднике без его ID")
@allure.description("")
@allure.feature("UPDATE")
@allure.severity("MINOR")
def test_change_employee_without_employee_id():
     with pytest.raises(TypeError):
        token = {}
        with allure.step("Получить токен авторизации"):
            token["client_token"] = api.get_token()
        with allure.step("Изменить информацию о сотруднике без его ID"):
            api.change_employee(token, "Петров","petrov@gmail.com","+70000000001", False)

@allure.title("Изменение информации о сотруднике без тела запроса")
@allure.description("")
@allure.feature("UPDATE")
@allure.severity("MINOR")
def test_change_employee_without_body():
    with pytest.raises(TypeError):
        token = {}
        with allure.step("Получить токен авторизации"):
            token["client_token"] = api.get_token()
        with allure.step("Изменить информацию о сотруднике без тела запроса"):
            api.change_employee(1, token)