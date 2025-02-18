import requests

class EmployeeApi:
    def __init__(self, url):
        self.url = url
    
    def get_employee(self, employee_id):
        resp = requests.get(self.url + '/employee/info/' + str(employee_id))
        return resp.json()

    def create_employee(self, first_name, last_name, middle_name, company_id, email, phone,  birthdate, is_active):
        employee = {
        "first_name": first_name,
        "last_name": last_name,
        "middle_name": middle_name,
        "company_id": company_id,
        "email": email,
        "phone": phone,
        "birthdate": birthdate,
        "is_active": is_active
        }
        resp = requests.post(self.url + '/employee/create/', json = employee)
        return resp.json()
    
    def get_employee_list(self, company_id):
        resp = requests.get(self.url + '/employee/list/' + str(company_id))
        return resp.json()

    def get_token(self, username = "harrypotter", password = "expelliarmus"):
        creds = {
            "username": username,
            "password": password
            }
        resp = requests.post(self.url + '/auth/login/', json = creds)
        return resp.json()["user_token"]
    
    def change_employee(self, employee_id, token, last_name, email , phone, is_active):
        new_employee = {
            "last_name": last_name,
            "email": email,
            "phone": phone,
            "is_active": is_active
            }
        resp = requests.patch(self.url + '/employee/change/' + str(employee_id), json = new_employee, params = token)
        return resp.json()