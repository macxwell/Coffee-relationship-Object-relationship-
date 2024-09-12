class Customer:
    all_customers = []  # Class-level list to keep track of all Customer instances

    def __init__(self, name):
        if not isinstance(name, str) or not (1 <= len(name) <= 15):
            raise ValueError("Name must be a string with 1 to 15 characters.")
        self._name = name
        Customer.all_customers.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 15):
            raise ValueError("Name must be a string with 1 to 15 characters.")
        self._name = value

    def create_order(self, coffee, price):
        return Order(self, coffee, price)

    def orders(self):
        return [order for order in Order.all_orders if order.customer == self]

    def coffees(self):
        return list(set(order.coffee for order in self.orders()))

    @classmethod
    def most_aficionado(cls, coffee):
        if not isinstance(coffee, Coffee):
            raise ValueError("Expected a Coffee instance.")
        customer_spending = {}
        for order in Order.all_orders:
            if order.coffee == coffee:
                if order.customer not in customer_spending:
                    customer_spending[order.customer] = 0
                customer_spending[order.customer] += order.price
        if customer_spending:
            return max(customer_spending, key=customer_spending.get)
        return None
    
cust = Customer("Max")
print(cust.name)