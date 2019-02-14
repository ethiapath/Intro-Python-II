# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item

class Player:
    def __init__(self, currentRoom):
        self.currentRoom = currentRoom
        self.items = []

    def move(self, room):
        self.currentRoom = room

    def add_item(self, item):
        self.items.append(item)
        print(f'Picked up {item.name}!')
