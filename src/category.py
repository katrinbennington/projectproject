
class Category:
    cnt_category = 0
    cnt_unique_item = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products
        Category.cnt_category += 1
        Category.cnt_unique_item += len(self.__products)
        Category.items = []

    def add_product(self, value):
        """добавление продукта с новой ценой"""
        self.__products.append(value)

    @property
    def products(self, items=''):
        for product in self.__products:
            items += f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n'
        return items

    def __str__(self):
        return f'{self.name}, количество продуктов: {len(self)} шт.'

    def __len__(self) -> int:
        return len(self.__products)
