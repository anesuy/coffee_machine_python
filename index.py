from menu import MENU
from resources import RESOURCES

# core input/output

machine_on = True
total_bill = 0.0
available_drinks = ["espresso", "latte", "cappuccino"]


def food_resource_verified(drink_chosen):
    ingredients_not_available = []
    for i in RESOURCES:
        if drink_chosen[i] > RESOURCES[i]:
            ingredients_not_available.append(i)
    if len(ingredients_not_available) > 0:
        return False, ingredients_not_available
    return True, ingredients_not_available


def process_coins(previous_total):
    quarters = int(input(f"Please, insert of quarters to be used for payment")) * 0.25
    dimes = int(input(f"Please, insert of dimes to be used for payment")) * 0.1
    nickles = int(input(f"Please, insert of nickles to be used for payment")) * 0.05
    pennies = int(input(f"Please, insert of pennies to be used for payment")) * 0.01
    global total_bill
    total_bill = previous_total + round(quarters + dimes + nickles + pennies, 2)
    return total_bill


def process_payment(drink_chosen):
    global total_bill
    total_bill = drink_chosen["cost"]
    total_payed = process_coins(0.0)
    cost_diff = total_payed - total_bill
    i = 0
    while cost_diff < 0 and i <= 2:
        provide_additional_value = print(
            f"The cost is higher than the value inserted, for ${cost_diff * (-1)}. "
            f"Would you like to provide the additional value (Y/N)?")
        if provide_additional_value == "Y":
            total_payed = process_coins(total_payed)
            cost_diff = total_payed - total_bill
            i += 1
        else:
            return False
    if cost_diff < 0 and i > 2:
        print("You exceeded all the available payment processes. Your money would be refunded.")
        total_bill = 0
        return False
    elif cost_diff > 0:
        print(f"Thank you! Here's your charge: {cost_diff}")
    else:
        print("Your order is on the way!")
        return True


def make_coffe(drink_chosen):
    for coffee_item in RESOURCES:
        RESOURCES[coffee_item] -= drink_chosen[coffee_item]
    print(f"Water: {RESOURCES['water']}ml")
    print(f"Milk: {RESOURCES['milk']}ml")
    print(f"Coffe: {RESOURCES['coffee']}")
    print(f"Total: {total_bill}")


while machine_on:
    global MENU
    global RESOURCES
    command = input("Chose the drink you would like (espresso, latte, cappuccino)")
    if command == "off":
        machine_on = False
    elif command == "report":
        print(f"Water: {RESOURCES['water']}ml")
        print(f"Milk: {RESOURCES['milk']}ml")
        print(f"Coffe: {RESOURCES['coffee']}")
        print(f"Total: {total_bill}")
    elif available_drinks.__contains__(command):
        chosen_drink = MENU[command]
        chosen_drink_result = food_resource_verified(chosen_drink["ingredients"])
        if not chosen_drink_result[0]:
            print("Some resources below are not available:")
            for item in chosen_drink_result[1]:
                print(f"{item}")
            print("Please, restart the order choose another item")
        else:
            if process_payment(chosen_drink):
                make_coffe(chosen_drink["ingredients"])
    else:
        command = print("Please, select an option. Chose the drink you would like (espresso, latte, cappuccino)")
