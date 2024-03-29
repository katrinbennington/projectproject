class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        Product.items = []

    @classmethod
    def add_product(cls, args):
        new_product = cls(**args)
        return new_product

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            return("Введена некорректная цена")
        else:
            self.__price = value

    def __add__(self, other):
        return self.price * self.quantity + other.price * other.quantity

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'
