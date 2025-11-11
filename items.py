

def create_item(name, col, subcol):
    new_item = Item(name, col, subcol)

class Item:
    def __init__(self, name, col, subcol):
        self.name = name
        self.col = col
        self.subcol = subcol

        self.item_dict = {"Name": self.name,
		"Collection": self.col,
		"Subcollection": self.subcol,
		"Measure Type": "N/A"}
		
        self.stock = 0
		
        self.item_variants = [] #List of dicts
        self.item_history = []
        self.active_item = {}


class Volume(Item):
    pass

class Count(Item):
    pass