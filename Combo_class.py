from Food_class import Food

class Combo(Food):
    def __init__(self, items, price, list_indivdual_items=None, ingredients=None):
        super().__init__(items, price, ingredients)
        if list_indivdual_items is None:
            list_indivdual_items = []
        else:
            self.list_indivdual_items = list_indivdual_items