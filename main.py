from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#Classes and Global vars
menu = Menu()
coffemaker = CoffeeMaker()
machine = MoneyMachine()

while True:
#Displaying menu
    user_input = input(f'What woould you like: {menu.get_items()}? ')


    #report
    if user_input == 'report':
        coffemaker.report()
        machine.report()
    elif user_input == 'off':
        print('Coffee Machine is turned off')
        break
    #cheking input
    else:
        user_drink = menu.find_drink(user_input)
        if user_drink is not None:
        #isresource enough
            if coffemaker.is_resource_sufficient(user_drink) and machine.make_payment(user_drink.cost):
                coffemaker.make_coffee(user_drink)
            
        
            
