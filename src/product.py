class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity
        Product.value = []

    @classmethod
    def add_product(cls, args):
        new_product = cls(**args)
        return new_product

    @property
    def price(self):
        return self._price

    @property
    def new_price(self, value):
        if value <= 0:
            print("Введена некорректная цена")
            return value

