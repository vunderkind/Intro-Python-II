from room import Room
from player import Player

# Declare all the rooms



room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", None, None, None, None),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", None, None, None, None),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", None, None, None, None),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", None, None, None, None),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", None, None, None, None),
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

#
# Main
#



# Make a new player object that is currently in the 'outside' room.
name = input(str('Enter your name: '))
initial_room = room['outside']
new_player = Player(name, initial_room)




# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
print(f'Hello {new_player.name}')
print('You are lost in the jungle in search of rare treasures. Three days ago, you and your team lost contact on all your communication devices. A monster wakes up at night and feasts on your colleagues. You are the lone survivor here. The only man alive on Nightmare Jungle.')
print(f'{new_player.current_room}')

while True:
    current_room = new_player.current_room
    print('========')
    print('Where do you go next?')
    # print(current_room)
    move_player = str(input("[n] North  [s] South   [e] East [w] West   [q] Quit\n"))
    ## Define north-bound action
    if move_player == 'n':
        if current_room.n_to is not None:
            new_player.current_room = current_room.n_to
            print(new_player)
        else:
            print("Whoopsie. There's a dragon lurking about. Aborting mission.")

    ## Define south-bound action
    if move_player == 's':
        if current_room.s_to is not None:
            new_player.current_room = current_room.s_to
            print(new_player)
        else:
            print("Blood-sucking vampires are hissing close to you. You turn back in fright. Good call.")
    
        ## Define West-bound action
    if move_player == 'w':
        if current_room.w_to is not None:
            new_player.current_room = current_room.w_to
            print(new_player)
        else:
            print("You cannot turn West at this time. There is a broken bridge and down below, the mounting skulls of those before you. The skulls of those foolish enough to try to leap the Cursed Bridge of Ptolemy.")
    
        ## Define east-bound action
    if move_player == 'e':
        if current_room.e_to is not None:
            new_player.current_room = current_room.e_to
            print(new_player)
        else:
            print("Snakes. It's just a writhing floor of snakes. Run while you still can!")
    elif move_player == 'q':
        print('You have chosen to quit this adventure. You coward. Goodbye.')
        exit()