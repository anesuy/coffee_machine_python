from resources import RESOURCES


class CoffeeMachine:
    def __init__(self):
        self.resources = RESOURCES

    def report(self):
        for item in self.resources:
            print(f"{item}: {item.par}")

    def food_resource_verified(self, drink_chosen):
        ingredients_not_available = []
        can_make_drink = True
        for item in self.resources:
            if drink_chosen is not None and self.resources[item][0] < drink_chosen.ingredients[
                item]:
                ingredients_not_available.append(item)
        if len(ingredients_not_available) > 0:
            can_make_drink = False
            for ingredient in ingredients_not_available:
                print(f"Ingredient not available: {ingredient}")
        return can_make_drink

    def make_coffee(self, order):
        for item in order.ingredients:
            self.resources[item][0] -= order.ingredients[item]
            print(self.resources[item])
            print(self.resources[item][0])
        print(f"Here is your {order.name} ☕️. Enjoy!")
