class MenuItem:
    def __init__(self, name, water, milk, coffee, price):
        self.name = name
        self.price = price
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    def __init__(self):
        self.menu = [
            MenuItem("latte", 200, 150, 24, 2.5),
            MenuItem("espresso", 50, 0, 18, 1.5),
            MenuItem("cappuccino", 250, 50, 24, 3)
        ]

    def get_drinks(self):
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def get_drink(self, order):
        for item in self.menu:
            if item == order:
                return item
        print(f"Sorry, {order} in not available in the menu list." +
              "Please, try again.")
