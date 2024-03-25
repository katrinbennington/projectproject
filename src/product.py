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




