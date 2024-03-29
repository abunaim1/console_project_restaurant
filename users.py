from abc import ABC, abstractmethod

class Users(ABC):
    def __init__(self, name, phone, email, address) -> None:
        self.name = name
        self.email = email
        self.phone = phone
        self.email = email
        self.address = address

class Customer(Users):
    def __init__(self, name, phone, email, address, money) -> None:
        self.wallet = money
        self.__order = None
        self.due_amount = 0
        super().__init__(name, phone, email, address, )
    
    @property
    def order(self):
        return f'{self.__order}'
    
    @order.setter
    def order(self, order):
        self.__order = order

    def place_order(self, order):
        self.due_amount += order.bill
        print(f'{self.name} placed an order with bill {order.bill}')

    def eat_food(self, order):
        print(f'{self.name} eat {order.items}')

    def pay_for_order(self, amount):
        pass

    def give_tips(self, tips_amount):
        pass

    def write_review(self, starts):
        pass

class Employee(Users):
    def __init__(self, name, phone, email, address, salary, starting_date, department) -> None:
        self.salary = salary
        self.starting_date = starting_date
        self.department = department
        super().__init__(name, phone, email, address)
    

class Chef(Employee):
    def __init__(self, name, phone, email, address, salary, starting_date, department, cooking_items) -> None:
        super().__init__(name, phone, email, address, salary, starting_date, department)
        self.cooking_items = cooking_items
        self.wallet = 0

    def salary_wallet_chef(self, amount):
        self.wallet += amount
        return f'{self.wallet}'

class Server(Employee):
    def __init__(self, name, phone, email, address, salary, starting_date, department) -> None:
        self.tips_earning = 0
        self.wallet = 0
        super().__init__(name, phone, email, address, salary, starting_date, department)

    def salary_wallet_server(self, amount):
        self.wallet += amount
        return f'{self.wallet}'
    
    def take_order(self, order):
        pass

    def transfer_order(self, order):
        pass

    def serve_order(self, order):
        pass

    def receive_tips(self, amount):
        self.tips_earning += amount

class Manager(Employee):
    def __init__(self, name, phone, email, address, salary, starting_date, department) -> None:
        super().__init__(name, phone, email, address, salary, starting_date, department)
        self.wallet = 0

    def salary_wallet_manager(self, amount):
        self.wallet += amount
        return f'{self.wallet}'