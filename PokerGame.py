#declaring fields
dealer = 0
pot = 0
players = []

small_blind_amount = 50
big_blind_amount = 100

#TODO: figure out a seating arrangment algorithm
class Player:
    def __init__(self, name, seat, chips):
        self.name = name
        self.chips = chips
        self.seat = seat
        self.isDealer = False
        self.bet = 0

    def __str__(self):
        print(" ")
        return (f"Name: {self.name} \n Position: {self.seat} \n Chips: {self.chips} \n Bet: {self.bet} \n IsDealer: {self.isDealer}\n")


class State:

    def __init__(self, name, pot, players):
        self.name = name
        self.pot = pot
        self.players = players

    def assign_blinds(self):
        players_length = len(self.players)
        for player in self.players:
            if player.isDealer == True:
                dealer_pos = player.seat
        for player in self.players:
            if player.seat == (dealer_pos + 1) % players_length:
                player.bet = small_blind_amount
            elif player.seat == (dealer_pos + 2) % players_length:
                player.bet = big_blind_amount


#running the game itself, procedural for now


if __name__ == "__main__":
    pass



