from PokerGame import *

#testing player creation
huey = Player("Huey", 0, 10000)
riley = Player("Riley", 1, 10000)
grandad = Player("Grandad", 2, 10000)
uncle_ruckus = Player("Uncle Ruckus", 3, 10000)

players = [huey, riley, grandad, uncle_ruckus]

# print(huey, riley, grandad, uncle_ruckus)




#testing assign_blinds
uncle_ruckus.isDealer = True
test_blind_state = State("test_blind", 0, players)
test_blind_state.assign_blinds()

# for player in players:
#     print(player)






