class Orders():

    def __init__(self, customer):
        self.tab = []
        self.customer = customer
        self.status = 'Open'

    def add_items_order(self, item):
        self.tab.append(item)

        #method to cal total
        #have a method to pay, and change status