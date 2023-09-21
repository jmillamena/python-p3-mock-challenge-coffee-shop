class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) >= 3 and not hasattr(self, 'name'):
            self._name = name

    def orders(self):
        return [order for order in Order.all if order.coffee is self]

    def customers(self):
        return list(set([order.customer for order in Order.all if order.coffee is self]))

    def num_orders(self):
        pass

    def average_price(self):
        pass


class Customer:
    all = []

    def __init__(self, name):
        self.name = name
        self.__class__.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) in range(1, 16):
            self._name = name

    def orders(self):
        return [order for order in Order.all if order.customer is self]

    def coffees(self):
        return [order.coffee for order in Order.all if order.customer is self]

    def create_order(self, coffee, price):
        pass


class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        self.__class__.all.append(self)

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, coffee):
        if isinstance(coffee, Coffee):
            self._coffee = coffee

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if (isinstance(price, float) and price in range(1, 11) and not hasattr(self, 'price')):
            self._price = price
