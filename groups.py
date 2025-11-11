


def create_collection(collections):
    name = input("Enter collection title: ")
    collections.append(Collection(name))

class Collection:
    def __init__(self, name, subcollections=[]):
        self.name = name
        self.subcollections = subcollections






 