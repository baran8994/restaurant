class Customer:
    def __init__(self, address, payment):
        self.address = address
        self.payment = payment

    def create(self):
        print("created")