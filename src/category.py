class Category:
    cnt_category = 0
    cnt_unique_item = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.products = products
        #self.cnt_category = len.products
        #self.cnt_unique_item = self.cnt_category
        Category.cnt_category += 1
        Category.cnt_unique_item += len(self.products)


    # def add_category(self, products):
    #     return products in self.cnt_category
