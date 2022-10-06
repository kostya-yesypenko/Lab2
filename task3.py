class Product:
    def __init__(self, price, description):
        if price < 0:
            raise ValueError
        if not isinstance(price, (int, float)):
            raise TypeError("Wrong price number")
        self.price = price
        self.description = description


class Customer:
    def __init__(self, surname, name, mobile_phone):
        if not isinstance(mobile_phone, (int, float)):
            raise TypeError("Wrong phone number")
        self.surname = surname
        self.name = name
        self.mobile_phone = mobile_phone


class Order:
    def __init__(self, customer, *product):
        if not isinstance(customer, Customer):
            raise TypeError("There is no customer")
        for i in product:
            if not isinstance(i, Product):
                raise TypeError("Wrong products")
        self.customer = customer
        self.products = product
        self.money = 0

    def __calculate_order(self):
        self.money = 0
        for i in self.products:
            self.money += i.price
        return self.money

    def __str__(self):
        return f'The price of order for {self.customer.surname} {self.customer.name} costs {self.__calculate_order()}'


customer1 = Customer("Yesypenko", "Kostia", 380971610252)
plane = Product(10, "Plane")
book = Product(5, "Book")
guitar = Product(12, "Guitar")
order = Order(customer1, guitar, plane)
print(order)
