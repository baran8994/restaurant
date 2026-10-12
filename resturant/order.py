class Order:
    def __init__(self, id_order, details, order_type,
                 customer, delivery, menu):
        self.id_order = id_order
        self.details = details
        self.order_type = order_type
        self.customer = customer
        self.delivery = delivery
        self.menu = menu

    def process_debit(self):
        print("processed")