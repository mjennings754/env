import json
game = []
name_input = input("What's the name of the game? ")
genre_input = input("What's the genre? ")
release_date_input = input("What's the release date? ")
game_input = name_input, genre_input, release_date_input
game.append(game_input)
with open('game.json', 'w') as f:
    json.dump(game, f)

print(game)