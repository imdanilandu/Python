import pytest
from EmployeeApi import EmployeeApi
from EmployeeTable import EmployeeTable

api = EmployeeApi("http://5.101.50.27:8000")
db = EmployeeTable("postgresql://qa:skyqa@5.101.50.27:5432/x_clients")

def test_get_employee():
    employee_id = 1
    api_result = api.get_employee(employee_id)
    db_result = db.get_employee(employee_id)
    assert api_result["first_name"] == db_result[0]["first_name"]

def test_get_employee_without_employee_id():
    with pytest.raises(TypeError):
        api.get_employee()

def test_create_employee():
    api_result = api.create_employee("Данил", "Стафейчук", "Романович", 2, "stafeychuk@gmail.com", "+79999999999", "1997-08-16", False)
    db_result = db.get_employee(api_result["id"])
    db.delete(api_result["id"])
    assert api_result["first_name"] == db_result[0]["first_name"]
    assert api_result["last_name"] == db_result[0]["last_name"]
    assert api_result["middle_name"] == db_result[0]["middle_name"]
    assert api_result["company_id"] == db_result[0]["company_id"]
    assert api_result["email"] == db_result[0]["email"]
    assert api_result["phone"] == db_result[0]["phone"]
    assert api_result["birthdate"] == str(db_result[0]["birthdate"])
    assert api_result["is_active"] == db_result[0]["is_active"]

def test_create_employee_without_body():
     with pytest.raises(TypeError):
        api.create_employee()

def test_get_employee_list():
    company_id = 1
    api_result = api.get_employee_list(company_id)
    db_result = db.get_employee_list(company_id)
    assert api_result[0]["id"] == db_result[0]["id"]

def test_get_employee_list_without_company_id():
    with pytest.raises(TypeError):
        api.get_employee_list()

def test_change_employee():
    token = {}
    token["client_token"] = api.get_token()
    api_result = api.create_employee("Данил", "Стафейчук", "Романович", 2, "stafeychuk@gmail.com", "+79999999999", "1997-08-16", False)
    api_change_result = api.change_employee(api_result["id"], token, "Петров","petrov@gmail.com","+70000000001", False)
    db_result = db.get_employee(api_result["id"])
    db.delete(api_result["id"])
    assert api_change_result["last_name"] == db_result[0]["last_name"]
    assert api_change_result["email"] == db_result[0]["email"]
    assert api_change_result["phone"] == db_result[0]["phone"]
    assert api_change_result["is_active"] == db_result[0]["is_active"]

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