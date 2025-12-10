from datetimetracking import *
from sysfuncs import menu_hold, clear_console


class MasterItems:
    def __init__(self):
        self.collections = {}

    def create_item_collection(self, name=None):
        if not name:
            name = input("Enter item collection name: ").title()
        self.collections[name] = ItemCollection(name)

    def create_item(self):
        name = input("Enter item name: ").title()
        col = input("Enter item collection: ").title()
        subcol = input("Enter item subcollection: ").title()
        #check if this is smart structuring
        self.add_item(name, col, subcol)
    
    def add_item(self, name, col, subcol):
        new_item = Item(name, col, subcol)
        if not col in self.collections:
            self.create_item_collection(col)
        self.collections[col].items_dict[name] = new_item 

    

    def view_collections(self):
        col_list = self.collections.keys()
        indexer = 1
        for c in col_list:
            print(f"[{indexer}] {c}")
        menu_choice = int(input('Enter collection number to access: '))
        #add view funcs
        col_list[menu_choice-1].view_col()
        
        

    


class ItemCollection:
    def __init__(self, name):
        self.name = name
        self.items_dict = {}
    
    def view_col(self):
        #do this one 
        pass


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

    def view_dict(self, dictionary): #check what you can do with the dict built in 
		
        clear_console()
        index_num = 1
		
        for key, value in dictionary.items():
            print(f'[{index_num}] {key}: {value}')
            index_num +=1	
			
        edit_choice = input('Enter entry number to edit, add a new entry with "[key name] [value]", [return] to exit: ')
		
        if edit_choice == '':
            clear_console()
            return
			
        elif ' ' in edit_choice:
            add_entry = edit_choice.split(' ')
            dictionary[add_entry[0]] = add_entry[1]
            return #this works fine but needs a sort + update method
			
        key_list = list(dictionary)
        selected_key = dictionary[key_list[int(edit_choice)-1]]
		
		
        if isinstance(selected_key, dict):
            return self.view_dict(selected_key) #need to add option for adding entries (i.e. missed a day)
			
			
		#could use a lambda here
        new_value = input('Enter new value: ')
        if isinstance(selected_key, int):
            new_value = int(new_value)
        elif isinstance(selected_key, float):
            new_value = float(new_value)
        elif isinstance(selected_key, tuple):
            new_value = tuple(new_value)
			
			
        dictionary[key_list[int(edit_choice)-1]] = new_value


class Volume(Item):
    pass

class Count(Item):
    pass