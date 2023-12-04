class Restaurant:
    def __init__(self, name) -> None:
        self.name = name
        self.chef = None
        self.manager = None
        self.server = None
        self.menu = []
        self.balance = 0
        self.profit = 0

    def add_employee(self, employee_type, employee):
        if employee_type == 'chef':
            self.chef = employee
        elif employee_type == 'server':
            self.server = employee
        elif employee_type == 'manager':
            self.manager = employee
    
    def recieve_payment(self, amount, order, customer):
        if amount >= order.bill:
            customer.due_amount = 0
            self.balance += order.bill
            return order.bill - amount
    
    def pay_salary(self, employee):
        if employee.salary < self.balance:
            employee.recieve_salary()

        
