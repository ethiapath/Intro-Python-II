from room import Room
from player import Player
from item import Item
import sys

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
                    passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
                    into the darkness. Ahead to the north, a light flickers in
                    the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
                    to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
                    chamber! Sadly, it has already been completely emptied by
                    earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

roomKeys = [name for name in room]

print(roomKeys)

# print(room['narrow'].w_to.n_to)

#
# Main
#

# def tryMove()

def parser(user_input):
    # direction = user_input + '_to'
    # player.move(player.currentRoom[direction])

    
    inputs = user_input.split(' ')
    # player.move(player.currentRoom.n_to)
    # if direction in player.currentRoom:
    #     print('this is working')

    if len(inputs) < 2:
        if user_input == 'n':
            try:
                player.move(player.currentRoom.n_to)
            except AttributeError:
                print('There is nothing!')
        elif user_input == 'e':
            try:
                player.move(player.currentRoom.e_to)
            except AttributeError:
                print('There is nothing!')
        elif user_input == 's':
            try:
                player.move(player.currentRoom.s_to)
            except AttributeError:
                print('There is nothing!')
        elif user_input == 'w':
            try:
                player.move(player.currentRoom.w_to)
            except AttributeError:
                print('There is nothing!')
        elif user_input == 'q':
            print('You have given up')
            sys.exit()
        else:
            print('ERROR! Thous\'t cannout goest!')
    else:
        print('more then one word', inputs)

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])

sword = Item('sword', 'A sharpend piece of steel')

player.add_item(sword)

# player.currentRoom['n' + '_to']
# Write a loop that:
#

while True:

    # * Prints the current room name
    # print('player.currentRoom', player.currentRoom)
    print(player.currentRoom.name, '\n')

    # * Prints the current description (the textwrap module might be useful here).
    print(player.currentRoom.discription, '\n')

    print(player.currentRoom.items)

    # * Waits for user input and decides what to do.
    action = input('doues\'t what?\n')
    #
    # If the user enters a cardinal direction, attempt to move to the room there.

    parser(action)

    # # Print an error message if the movement isn't allowed.
    #
    # If the user enters "q", quit the game.
