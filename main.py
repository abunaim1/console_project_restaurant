from menu import *
from restaurant import*
from users import*
def main():
    #create menu
    menu = Menu()
    #add pizzas to the manue
    pizza_1 = Pizza('Rustom Pizza', 1000, 'Large', ['Meat', 'Onion', 'Mashroom'])
    pizza_2 = Pizza('Chiken Pizza', 850, 'Medium', ['Chicken', 'Cheez', 'Paparuni'])
    pizza_3 = Pizza('Gaza Pizza', 1200, 'Extra Large', ['Oil', 'Onion', 'Mashroom'])
    menu.add_items(pizza_1, 'pizza')
    menu.add_items(pizza_2, 'pizza')
    menu.add_items(pizza_3, 'pizza')
    
    #add burger to the menue
    burger_1 = Burger('Chiken Burger', 310, 'chiken', ['chiken', 'tmatoo', 'onion'])
    burger_2 = Burger('Beef Burger', 400, 'beef', ['beef', 'oil', 'tomatoo'])
    burger_3 = Burger('Kabutor Burger', 200, 'Kabutor', ['Kabutor', 'onion'])
    menu.add_items(burger_1, 'burger')
    menu.add_items(burger_2, 'burger')
    menu.add_items(burger_3, 'burger')

    #add drinks to the menue
    drinks_1 = Drinks('Mojo', 20, True)
    drinks_2 = Drinks('Hot cofee', 250, False)
    menu.add_items(drinks_1, 'drinks')
    menu.add_items(drinks_2, 'drinks')

    #show menu
    menu.show_menu()

    #create restuarant
    hotel = Restaurant('Fahad''s Vater Hotel',5000, menu)

    #add employees
    manager = Manager('Fahad', 2324, 'fahad@hossain.com', 'Cumilla', 2000, '12 Nov, 2001', 'Manager')
    chef = Chef('Tonmoy', 1356, 'tonmoy_kitchen@gmail.com', 'Gopali', 10000000, '31 Dec, 2002', 'Main Chef', ['Burgers', 'Pizzas'])
    server = Server('naim', 334422, 'naim@naim.com', 'Barishal', 100, '10 March, 2001', 'Cleaning')
    hotel.add_employee('manager', manager)
    hotel.add_employee('chef', chef)
    hotel.add_employee('server', server)

    #showing employee
    hotel.show_employee()

if __name__ == '__main__':
    main()
