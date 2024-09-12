
class Coffee:
    all_coffees = []  # Class-level list to keep track of all Coffee instances

    def __init__(self, name):
        if not isinstance(name, str) or len(name) < 3:
            raise ValueError("Name must be a string with at least 3 characters.")
        self.name = name
        Coffee.all_coffees.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value

    def orders(self):
        from oder import Order
        return [order for order in Order.all_orders if order.coffee == self]

    def customers(self):
        return list(set(order.customer for order in self.orders()))

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        orders = self.orders()
        if not orders:
            return 0
        total_price = sum(order.price for order in orders)
        return total_price / len(orders)
    
coffee = Coffee("latte")
print(coffee.name)