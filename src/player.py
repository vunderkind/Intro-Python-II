# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, current_room=None):
        self.current_room = current_room

    def __str__(self):
        output= ''
        output += f'[{self.current_room}]'
        if self.current_room == None:
            return f'The player is not in a room yet. Consider putting them in a room!'
        else:
            return f'Player is now in room {self.current_room}.'


player1 = Player()
print(player1)
