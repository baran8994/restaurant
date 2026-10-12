class Delivery:
    def __init__(self, id_delivery, name, date, address):
        self.id_delivery = id_delivery
        self.name = name
        self.date = date
        self.address = address

    def update(self):
        print("updated")