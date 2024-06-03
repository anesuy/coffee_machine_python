from menu import Menu
from coffee_machine import CoffeeMachine
from payment_machine import PaymentMachine
from order_process import OrderProcess

payment_machine = PaymentMachine()
coffee_machine = CoffeeMachine()
menu = Menu()
order_process = OrderProcess()


while order_process.order_process:
    menu_list = menu.get_drinks()
    command = input(f"Please, choose your order among the shown options: ({menu_list})")
    if command == "off":
        order_process.exit_order_process()
    elif command == "report":
        coffee_machine.report()
        payment_machine.report()
    else:
        order = menu.get_drink(command)
        order_available = coffee_machine.food_resource_verified(order)
        print(order_available)
        if (order is not None and order_available and
                payment_machine.process_payment(
                order.price)):
            coffee_machine.make_coffee(order)


