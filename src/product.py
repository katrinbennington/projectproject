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
        Product.items = []

    @classmethod
    def add_product(cls, args):
        new_product = cls(**args)
        return new_product

    @property
    def new_price(self, value):
        if value <= 0:
            print("Введена некорректная цена")
            return value


    @property
    def new_price(self, value):
        self._price = value
        return self._price

