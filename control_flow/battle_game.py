import random
#Make a 2 player Battle game game, using Python!

#Player selects a character/fighter (from 4-6) or gets one assigned to them randomly.

#If Player 2, let them pick the character/fighter they want. If CPU assign a character/fighter randomly.

#The two Pokemon need to fight.

#A winner must be declared via some sort of calculation.

#Bonus: Want to play again?#

fighters = {
    "Ryu" : {"Strength" : 120, "Speed" : 75, "IQ" : 55},
    "Ramon Rossi" : {"Strength" : 80, "Speed" : 95, "IQ" : 120},
    "Batman" : {"Strength" : 100, "Speed" : 55, "IQ" : 85},
    "Attack Titan" : {"Strength" : 150, "Speed" : 75, "IQ" : 95},
    "Spiderman" : {"Strength" : 70, "Speed" : 1105, "IQ" : 105},
    "Harry Potter" : {"Strength" : 30, "Speed" : 40, "IQ" : 75}
}
player_1 = input(f"Player 1, Select your Fighter... {fighters.keys()} ")
if player_1 is None:
    random.choice(list(fighters.list()))
print(f"Player 1: {player_1}")
player_2 = input(f"Player 2, Select your Fighter... {fighters.keys()} ")
print(f"Player_2: {player_2}")


for ability in fighters.values():
    for specific_ability in ability.values():
        random_ability_player_1 = (random.choices(list(ability.items())))
        #if ability[1]









