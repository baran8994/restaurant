class Menu:
    def __init__(self, id_menu, details, items):
        self.id_menu = id_menu
        self.details = details
        self.list = items

    def update(self):
        print("updated")