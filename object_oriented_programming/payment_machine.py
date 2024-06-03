class PaymentMachine:
    CURRENCY = "$"
    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.total_bill = 0
        self.profit = 0
        self.value_paid = 0
        self.change_value = 0

    def reset_payment_info(self):
        self.value_paid = 0
        self.profit = 0
        self.total_bill = 0
        self.change_value = 0

    def report(self):
        print(f"Total order: {self.CURRENCY} {self.total_bill}")
        print(f"Total inserted: {self.CURRENCY} {self.value_paid}")
        print(f"Total difference: {self.CURRENCY} {self.profit}")

    def process_coins(self):
        print("Please, insert the coin(s) for payment")
        for coin in self.COIN_VALUES:
            value_inputted = input(f"How many {coin}")
            self.value_paid = self.value_paid + int(value_inputted) * self.COIN_VALUES[coin]
        self.change_value = self.value_paid - self.total_bill
        return self.value_paid

    def process_payment(self, total_bill):
        self.total_bill = total_bill
        self.process_coins()
        i = 0
        limit_tries = 2
        while self.change_value < 0 and i <= limit_tries:
            add_value = input(
                f"The cost is higher than the value inserted, for ${self.change_value * (-1)}. "
                f"Would you like to provide the additional value (Y/N)?")

            if add_value == "Y":
                self.process_coins()
                i += 1
            else:
                print("Your money would be refunded. " +
                      "Please, start again. Or, until next time!")
                self.reset_payment_info()
                return False
        if self.change_value < 0 and i > limit_tries:
            print("You exceeded all the available payment processes. Your money would be refunded.")
            self.reset_payment_info()
            return False
        elif self.change_value > 0:
            change = round(self.change_value, 2)
            print(f"Your change is {self.CURRENCY}{change}")
            self.profit += total_bill
            self.value_paid = 0
            return True
        else:
            print("Your order is on the way!")
            self.reset_payment_info()
            return True
