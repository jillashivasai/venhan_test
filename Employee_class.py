class Employee:
    employee_count = 0

    def __init__(self, employee_id):
        self.employee_id = employee_id
        Employee.employee_count += 1

    @classmethod
    def get_employee_count(cls):
        return cls.employee_count

    @staticmethod
    def validate_employee_id(employee_id):
        return employee_id.isdigit()
