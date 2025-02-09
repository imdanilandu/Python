import pytest
from EmployeeApi import EmployeeApi

api = EmployeeApi("http://5.101.50.27:8000")

def test_get_employee():
    result = api.get_employee(1)
    assert len(result) > 0

def test_get_employee_without_employee_id():
    with pytest.raises(TypeError):
        api.get_employee()

def test_create_employee():
    result = api.create_employee("Данил", "Стафейчук", "Романович", 2, "stafeychuk@gmail.com", "+79999999999", "1997-08-16", False)
    first_name = result["first_name"]
    last_name = result["last_name"]
    middle_name = result["middle_name"]
    company_id = result["company_id"]
    email = result["email"]
    phone = result["phone"]
    birthdate = result["birthdate"]
    is_active = result["is_active"]
    assert len(result) > 0
    assert first_name == "Данил"
    assert last_name == "Стафейчук"
    assert middle_name == "Романович"
    assert company_id == 2
    assert email == "stafeychuk@gmail.com"
    assert phone == "+79999999999"
    assert birthdate == "1997-08-16"
    assert is_active == False

def test_create_employee_without_body():
     with pytest.raises(TypeError):
        api.create_employee()

def test_get_employee_list():
    result = api.get_employee_list(1)
    assert len(result) > 0

def test_get_employee_list_without_company_id():
    with pytest.raises(TypeError):
        api.get_employee_list()

def test_change_employee():
    token = {}
    token["client_token"] = api.get_token()
    result = api.change_employee(1, token, "Петров","petrov@gmail.com","+70000000001", False)
    new_last_name = result["last_name"]
    new_email = result["email"]
    new_phone = result["phone"]
    new_is_active = result["is_active"]
    assert len(result) > 0
    assert new_last_name == "Петров"
    assert new_email == "petrov@gmail.com"
    assert new_phone == "+70000000001"
    assert new_is_active == False

def test_change_employee_without_token():
    with pytest.raises(TypeError):
        api.change_employee(1, "Петров","petrov@gmail.com","+70000000001", False)

def test_change_employee_without_employee_id():
     with pytest.raises(TypeError):
        token = {}
        token["client_token"] = api.get_token()
        api.change_employee(token, "Петров","petrov@gmail.com","+70000000001", False)

def test_change_employee_without_body():
    with pytest.raises(TypeError):
        token = {}
        token["client_token"] = api.get_token()
        api.change_employee(1, token)