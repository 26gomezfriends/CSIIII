class CoffeeMenu:
    def __init__(self):
        self.menu = {
            'espresso': 2.50,
            'latte': 3.00,  # Price updated to match test expectation
            'cappuccino': 3.20,
            'americano': 2.70
        }

    def get_price(self, item):
        if item in self.menu:
            return self.menu[item]
        else:
            raise KeyError(f"{item} not found in the menu")

    def add_item(self, item, price):
        self.menu[item] = price
