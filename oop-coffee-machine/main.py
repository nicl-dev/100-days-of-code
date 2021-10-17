from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
machine = CoffeeMaker()
money_machine = MoneyMachine()



def make_coffee():
    """
    Runs the coffee machine.

    :return: None
    """
    is_on = True

    while is_on:
        options = menu.get_items()
        order = input(f"What would you like? ({options}): ")
        if order == "off":
            is_on = False
        elif order == "report":
            machine.report()
        else:
            if menu.find_drink(order):
                drink = menu.find_drink(order)
                if machine.is_resource_sufficient(drink):
                    is_enough_ingredients = machine.is_resource_sufficient(drink)
                    is_payment_successful = money_machine.make_payment(drink.cost)
                    if is_enough_ingredients and is_payment_successful:
                        machine.make_coffee(drink)


make_coffee()
