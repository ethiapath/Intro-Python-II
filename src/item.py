
class Item:
    def __init__(self, name, discription):
        self.name = name
        self.discription = discription

    def __str__(self):
        return self.name

    def on_get(self):
        print(f'{self.discription}')

    def on_drop(self):
        print(f'{self.name} falls to the ground')
