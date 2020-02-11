from People_class import People

class Customer(People):
    def __init__(self, name, payment_details, address=None):
        super().__init__(name)
        if address is None:
            address = []
        else:
            self.address = []
        self.__payment_details = {}

    def add_payment_details(self, address, card_no):
        self.__payment_details['address'] = address
        self.__payment_details['card no'] = card_no

    def send_payment_details(self):
        return self.__payment_details