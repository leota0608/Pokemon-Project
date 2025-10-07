###############################################################################
#Title: Pokemon Selecting
#Class: CS 30
#Assignment: Pokemon part 3 assignment
#Coder: Leo
#version: 5
#Last date modified: 10/3/2025
###############################################################################
'''
This program lets the user selects their pokemon for their game,
including pokemon selection, moves and nickname picking.
'''
###############################################################################
#Imports & Global Variables----------------------------------------------------
pokemon_db = {"Blaziken": {"name":"Blaziken",
                        "type": ["fire"],
                        "moves": ["Swords dance", "Flare blitz", "Low kick",
                                 "Stone edge"],
                        "evolution": 3,
                        "pokedex": """when facing a tough foe, it 
                        looses flames from its wrists. Its powerful legs 
                        let it jump clear over buildings.""",
                        "hp": 80,  "atk": 120, "def": 70},
           "Jigglypuff": {"name":"Jigglypuff",
                        "type": ["water"],
                        "moves": ["Sing", "Def curl", "Pound"],
                        "evolution": 1,
                        "pokedex": """Jigglypuff, known as the Balloon Pokémon
                        is a Normal type Pokémon introduced in Generation I.
                        It is recognized for its ability to lull opponents
                        to sleep by singing a soothing melody.""",
                        "hp": 115, "atk": 40,"def": 25},
           "Froakie": {"name":"Froakie",
                        "type": ["water"],
                        "moves":["Pound", "Growl", "Water Gun",\
                                 "Quick Attack"],
                        "evolution": 1,
                        "pokedex": """Small blue frog Pokemon.
                        Evolves into Frogadier.""",
                        "hp": 41, "atk": 56, "def": 40},
           "Blastoise": {"name":"Blastoise",
                        "type": ["water"],
                        "moves": ["Torrent", "Rain Dish"],
                        "evolution": 3, 
                        "pokedex": """Blastoise is a large, bipedal,
                        reptilian Pokémon. It has a blue body with small purple
                        eyes, alight brown belly, and a stubby tail.
                        It has a large brown shell with two powerful
                        watercannons on either side, which can be withdrawn""",
                        "hp": 79, "atk": 83, "def": 100}}
available_choices = ["pick pokemon", "pick move", "pick nickname", "setting"]
player = {"name": "", "active": None}
pokemon = {}
pokemon_nickname = None
pokemon_move = None
pokemon_name = None

skip_start = False
setting_options = ["start game", "quit game", "reselect pokemon", "reselect move", "rename pokemon",\
                   "reset all selections", "quit setting"]


#Functions---------------------------------------------------------------------
def picksth(output, input_range = "none"):
    '''
    Thsi function lets the user picks anything, parameters include n output,
    asking the user for input and input range is if there is a certain range
    required for the input.
    '''
    while True:
        _input = input(output)
        if input_range == "none" or _input in input_range:
            break
        else:
            print("invalid input")
    while True:
        confirm = input("confirm? yes/no\n")
        if confirm == "yes":
            return _input
        elif confirm == "no":
            return picksth(output, input_range)
        else:
            print("invalid input")


def pick_username():
    '''This function lets thre user choose its username.'''
    name = picksth("Enter your name: ")
    player["name"] = name
    print(f"Hello {name}!")
    
    
def pick_pokemon():
    '''This function lets the user picks their pokemon.'''
    global player, pokemon, pokemon_nickname, pokemon_name
    pokemon_choices = ""
    for i in pokemon_db:
        pokemon_choices += f"- {i}\n"
    pokemon_name = picksth(f"Pick your Pokemon: \n{pokemon_choices}", pokemon_db.keys())
    player["active"] = pokemon_name
    print(f"Pokemon [{pokemon_name}] succesfully picked...")

def pick_move():
    global player, pokemon, pokemon_move
    # pick move
    move_choices = ""
    for i in pokemon_db[player["active"]]["moves"]:
        move_choices += f"- {i}\n"
    pokemon_move = picksth(f"Pick a move for the pokemon: \n{move_choices}", pokemon_db[player["active"]]["moves"])
    #temp_storage["moves"].append(pokemon_move)
    '''
    pokemon[player["active"]]["moves"].append(pokemon_move)
    '''
    print(f"Move [{pokemon_move}] successfully added...")
    
    
def pick_nickname():
    global player, pokemon, pokemon_nickname
    # pick nickname
    pokemon_nickname = str(picksth("Pick a nickname for the pokemon: "))
    '''
    pokemon[player["active"]]["nickname"] = pokemon_nickname
    '''
    print(f"Nickname [{pokemon_nickname}] successfully picked.")


def start_gaming():
    '''
    This function determins if the user can start the game. If not, it
    prints the optinos remaining and if yes, the game starts and it updates all the values
    to the dictionary. It also returns true or false to let the main code knows whether or
    not to stop the program
    '''
    global pokemon
    if pokemon_name and pokemon_nickname and pokemon_move:
        print("Game started\nCurrent status:")
        print(f"Player: {player['name']}\nActive pokemon: {player['active']}")
        pokemon[pokemon_nickname] = {}
        pokemon[pokemon_nickname]["name"] = pokemon_name
        pokemon[pokemon_nickname]["species"] = pokemon_db[pokemon_name]["type"]
        pokemon[pokemon_nickname]["hp"] = pokemon_db[pokemon_name]["hp"]
        pokemon[pokemon_nickname]["atk"] = pokemon_db[pokemon_name]["atk"]
        pokemon[pokemon_nickname]["def"] = pokemon_db[pokemon_name]["def"]
        pokemon[pokemon_nickname]["move"] = pokemon_move
        for p,q in pokemon.items():
            print(f"{p}:")
            for i,j in q.items():
                print(f"	{i}: {j}")
        return True
    else:
        print("Task needed to be completed: ")
        for i in range(0, 3):
            if not "(done)" in available_choices[i]:
                print(f"- {available_choices[i]}")
        print("- setting")
        return False
        
        
def settings():
    '''This function is the setting menu, including:
    start game, quit game, quit setting, reselect: pokemon,
    move, nick name.
    '''
    global pokemon, skip_start, player, pokemon_nickname				#add more setting options
    print("**settings**")
    for setting in setting_options:
        print(f"- {setting}")
    choice = picksth("Choice: ", setting_options)
    choice_num = setting_options.index(choice)
    if choice_num == 0:# start game
        if start_gaming():
            return "game_started"
        else:
            skip_start = True
    elif choice_num == 1:# quit
        print("Game ended")
        return "quit_game"
    elif choice_num == 2:# reselect pokemon
        if not "(done)" in available_choices[0]:
            print("**You haven't choose a pokemon yet.**")
            return
        pokemon_name = None
        pokemon_move = None
        pokemon_nickname = None
        available_choices[1] = "pick move"
        available_choices[2] = "pick nickname"
        player["active"] = None
        pick_pokemon()
    elif choice_num == 3:# reselect move
        if not "(done)" in available_choices[1]:
            print("**You haven't choose a move yet.**")
            return
        pokemon_move = None
        pick_move()
        
    elif choice_num == 4:# rename pokemon
        if not "(done)" in available_choices[2]:
            print("**You haven't name your pokemon yet.**")
            return
        pokemon_nickname = None
        pick_nickname()
    elif choice_num == 5:# reset all selections
        
        player["active"] = None
        pokemon_nickname = None
        pokemon_name = None
        pokemon_move = None
        available_choices[0] = "pick pokemon"
        available_choices[1] = "pick move"
        available_choices[2] = "pick nickname"
        print("**All selections are reset**")
    elif choice_num == 6:# quit setting
        return
    return
#available_choices = ["pick pokemon", "pick move", "pick nickname", "setting"]
    
#Main--------------------------------------------------------------------------
print("Welcome!")
pick_username()
while True:
    if not skip_start:
        print(f"Avalable choices: ")
    _quit = True
    for i in range(len(available_choices)):
        if i <= 2 and not "(done)" in available_choices[i]:
            _quit = False
        if not skip_start:
            print(f"- {available_choices[i]}")
    if not skip_start:
        choice = picksth("Choice: ", available_choices)#"pick pokemon", "pick move", "pick nickname"
    else:
        not_done = []
        for i in range(0, 3):
            if not "(done)" in available_choices[i]:
                not_done.append(available_choices[i])
        choice = picksth("Choice: ", not_done)
    choice_num = available_choices.index(choice)
    #print(f"number: {choice_num}")
    if choice_num == 0:
        skip_start = False
        pick_pokemon()
        available_choices[0] += "(done)"
    elif not "(done)" in available_choices[0] and not choice_num == 3:
        print("**Pick a Pokemon first**")   
    elif choice_num == 1:
        skip_start = False
        pick_move()
        available_choices[1] += "(done)"
    elif choice_num == 2:
        skip_start = False
        pick_nickname()
        available_choices[2] += "(done)"
    elif choice_num == 3:
        result = settings()
        if result == "game_started" or result == "quit_game":
            break



