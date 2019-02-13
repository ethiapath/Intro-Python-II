# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item

class Player:
    def __init__(self, location):
        self.location = location

    def move(self, room):
        self.location = room

    def add_item(self, item):
        self.item = item
        print(f'Picked up {item.name}!')
