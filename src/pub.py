class Pub:

    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def increase_till(self, amount):
        self.till += amount

    def check_age(self, age, drink_price):
        if age >= 18:
            self.increase_till(drink_price)
        else:
            return "Not old enough"

    # def sell_drink(self, drink_price, customer_wallet, age):
    #     if age < 18:
    #         return "You're not old enough"
    #     else:
    #         self.increase_till(drink_price)
    #         self.decrease_wallet(customer_wallet)


            


        

    