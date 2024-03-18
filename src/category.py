class Category:
    cnt_category = 0
    cnt_unique_item = 0

    def __init__(self, name: str, description: str, products: list, cnt_category: int, cnt_unique_item: int):
        self.name = name
        self.description = description
        self.products = products
        self.cnt_category = cnt_category
        self.cnt_unique_item = cnt_unique_item + 1


    # def add_category(self, products):
    #     return products in self.cnt_category
