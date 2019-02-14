# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room:
    def __init__(self, name, discription):
        self.name = name
        self.discription = discription
        self.items = []

    def set_items(self, items):
        self.items = items

    def remove_item(self, item):
       del self.items[item]
