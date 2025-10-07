jigglypoff = {"name": "jigglypoff",
              "type": ["normal", "fairy"],
              "moves": ["sing", "defence curl", "pound"],
              "pokedex": '''Jigglypuff, known as the Balloon Pokémon,
                is a Normal/Fairy-type Pokémon introduced in Generation I.
                It is recognized for its ability to lull opponents to sleep
                by singing a soothing melody.''',
              "eveluation": 1,
              "hp": 115,
              "atk": 40,
              "defence": 25}

print(f"{jigglypoff['name']} has {len(jigglypoff['moves'])} moves:")
for move in jigglypoff['moves']:
    print(f"- {move}")
    
print(f"The pokemon I chose is {jigglypoff['name']}, and it has {jigglypoff['hp']} hp, {jigglypoff['atk']} \
atk, and {jigglypoff['defence']} defence.")
