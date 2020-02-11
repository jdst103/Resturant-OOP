class Food():
    def __init__(self, item, price, ingredients=None):
        self.items = item
        self.price = price
        if ingredients is None:
            ingredients = []
        else:
        self.ingredients = ingredients