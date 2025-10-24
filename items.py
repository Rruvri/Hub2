

items = []

def create_item(name, col, subcol):
    new_item = Item(name, col, subcol)

class Item:
    def __init__(self, name, col, subcol):
        self.name = name
        self.col = col
        self.subcol = subcol


class Volume(Item):
    pass

class Count(Item):
    pass