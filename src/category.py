class Category:
    cnt_category = 0
    cnt_unique_item = 0
    name: str
    description: str
    products: list

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products

        Category.cnt_category = 1
        Category.cnt_unique_item = self.cnt_category
