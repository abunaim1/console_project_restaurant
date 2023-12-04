class Restaurant:
    def __init__(self, name, rent, manu) -> None:
        self.name = name
        self.chef = None
        self.manager = None
        self.server = None
        self.menu = manu
        self.rent = rent
        self.balance = 0
        self.profit = 0

    def add_employee(self, employee_type, employee):
        if employee_type == 'manager':
            self.manager = employee        
        elif employee_type == 'chef':
            self.chef = employee
        elif employee_type == 'server':
            self.server = employee
    
    def recieve_payment(self, amount, order, customer):
        if amount >= order.bill:
            customer.due_amount = 0
            self.balance += order.bill
            return order.bill - amount
    
    def pay_salary(self, employee):
        if employee.salary < self.balance:
            employee.recieve_salary()

    def show_employee(self):
        print('------------Showing Employees----------')
        if self.manager is not None:
            print(f'Manager: {self.manager.name}, Phone: {self.manager.phone}, Department: {self.manager.department}, Salary: {self.manager.salary}, Joinig Date: {self.manager.starting_date}')
        if self.chef is not None:
            print(f'Chef Name: {self.chef.name}, Joining Date: {self.chef.starting_date}, Salary: {self.chef.salary}')
        if self.server is not None:
            print(f'Server Name: {self.server.name}, Phone Number: {self.server.phone}')
        
        print()