###############################################################################
#Title: Pokemon Data Base
#Class: CS 30
#Assignment: Pokemon data base assignment
#Coder: Leo,  Atticus, james, Brody
#version: 1
#Last date modified: 9/18/2025
###############################################################################
'''
This program creates a data base, outputs 4 sentences using the data base,
and prints all the moves of Pokemons
'''
###############################################################################
#Imports & Global Variables----------------------------------------------------
pokemon_db = {"Blaziken": {"name":"Blaziken",
                        "type": ["wire"],
                        "moves": ["Swords dance", "Flare blitz", "Low kick",
                                 "Stone edge"],
                        "evelution": 3,
                        "pokedex": """when facing a tough foe, it 
                        looses flames from its wrists. Its powerful legs 
                        let it jump clear over buildings.""",
                        "hp": 80,  "atk": 120, "def": 70},
           "jigglypuff": {"name":"Jigglypuff",
                        "type": ["water"],
                        "moves": ["Sing", "Def curl", "Pound"],
                        "evelution": 1,
                        "pokedex": """Jigglypuff, known as the Balloon Pokémon
                        is a Normal type Pokémon introduced in Generation I.
                        It is recognized for its ability to lull opponents
                        to sleep by singing a soothing melody.""",
                        "hp": 115, "atk": 40,"def": 25},
           "froakie": {"name":"Froakie",
                        "type": ["water"],
                        "moves":["Pound", "Growl", "Water Gun",\
                                 "Quick Attack"],
                        "evolution": 1,
                        "pokedex": """Small blue frog Pokemon.
                        Evolves into Frogadier.""",
                        "hp": 41, "atk": 56, "def": 40},
           "blastoise": {"name":"Blastoise",
                        "type": ["water"],
                        "moves": ["Torrent", "Rain Dish"],
                        "evolution": 3, 
                        "pokedex": """Blastoise is a large, bipedal,
                        reptilian Pokémon. It has a blue body with small purple
                        eyes, alight brown belly, and a stubby tail.
                        It has a large brown shell with two powerful
                        watercannons on either side, which can be withdrawn""",
                        "hp": 79, "atk": 83, "def": 100}}
pokemon_number = 1


#Main--------------------------------------------------------------------------
print(f"1. Blaziken has evelution {pokemon_db['Blaziken']['evelution']}.")
print(f"2. Jigglypuff has an hp of {pokemon_db['Blaziken']['hp']}.")
print(f"3. Froakie pokedex: {pokemon_db['froakie']['pokedex']}")
print(f"4. {'froakie'.title()} is the same type as {'blastoise'.title()},\
they are both {pokemon_db['blastoise']['type']}.")

for pokemon in pokemon_db:
    print(f"{pokemon_number}. {pokemon_db[pokemon]['name']}'s moves:")
    move_number = 1
    for move in pokemon_db[pokemon]["moves"]:
       print(f"  {move_number}. {move}")
       move_number += 1
    pokemon_number += 1











