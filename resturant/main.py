
from customer import *
from delivery import *
from menu import *
from order import *

# Create objects
customer = Customer("Tehran, Iran", "Online Payment")

delivery = Delivery(
    1,
    "Ali",
    "2026-10-12",
    "Tehran, Iran"
)

menu = Menu(
    1,
    "Fast Food Menu",
    ["Pizza", "Burger", "French Fries"]
)

order = Order(
    101,
    "Customer food order",
    "Online",
    customer,
    delivery,
    menu
)


# Call methods
print("===== CUSTOMER =====")
customer.create()

print("\n===== DELIVERY =====")
delivery.update()

print("\n===== MENU =====")
menu.update()

print("\n===== ORDER =====")
order.processDebit()
