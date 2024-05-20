from resources import RESOURCES


class CoffeeMachine:
    def __init__(self):
        self.resources = RESOURCES

    def report(self):
        for item in self.resources:
            print(f"{item}: {item[0]}{item[1]}")

    def food_resource_verified(self, drink_chosen):
        ingredients_not_available = []
        can_make_drink = False
        for item in self.resources:
            if drink_chosen[item] > self.resources[item][0]:
                ingredients_not_available.append(item)
        if len(ingredients_not_available) == 0:
            can_make_drink = True
        return can_make_drink, ingredients_not_available

    def make_coffee(self, order):
        for item in order.ingredients:
            self.resources[item][0] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")
