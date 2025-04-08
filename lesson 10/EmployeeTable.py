from sqlalchemy import create_engine
from sqlalchemy.sql import text

class EmployeeTable:
    def __init__(self, connection_string):
        self.db = create_engine(connection_string)
    
    def get_employee(self, id: int) -> list:
        """Получение данных о сотруднике из БД"""
        return self.db.execute(text("select * from employee where id = :employee_id"), employee_id = id).fetchall()
    
    def get_employee_list(self, id: int) -> list:
        """Получение списка сотрудников компании из БД"""
        return self.db.execute(text("select * from employee where company_id = :company_id"), company_id = id).fetchall()
    
    def delete(self, id: int) -> None:
        """Удаление сотрудника из БД"""
        return self.db.execute(text("delete from employee where id = :id_to_delete"), id_to_delete = id)