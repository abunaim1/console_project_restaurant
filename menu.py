class Food:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price
        self.cooking_time = 15

class Burger(Food):
    def __init__(self, name, price, meat, ingredients) -> None:
        self.meat = meat
        self.ingredients = ingredients
        super().__init__(name, price)

class Pizza(Food):
    def __init__(self, name, price, size, toppings) -> None:
        self.size = size
        self.toppings = toppings
        super().__init__(name, price)

class Drinks(Food):
    def __init__(self, name, price, isCold = True) -> None:
        self.isCold = isCold
        super().__init__(name, price)

class Menu:
    def __init__(self) -> None:
        self.burgers = []
        self.pizzas = []
        self.drinks = []

    def add_items(self, item, item_type):
        if item_type == 'burger':
            self.burgers.append(item)
        if item_type == 'pizza':
            self.pizzas.append(item)
        if item_type == 'drinks':
            self.drinks.append(item)
    
    def removes_item(self, item):
        if item in self.burgers:
            self.burgers.remove(item)
        if item in self.pizzas:
            self.pizzas.remove(item)
        if item in self.drinks:
            self.drinks.remove(item)
        else:
            print(f'This {item} is not in your list already')
    
    def show_menu(self):
        print('-----------------------------------')
        for burger in self.burgers:
            print(f'Burger name: {burger.name} price: {burger.price}')
        print()
        for pizza in self.pizzas:
            print(f'Pizza name: {pizza.name} price: {pizza.price}')
        print()
        for drink in self.drinks:
            print(f'Drinks: {drink.name} price {drink.price}')
        print('-----------------------------------')

