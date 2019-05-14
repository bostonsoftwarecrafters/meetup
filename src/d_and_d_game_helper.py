from d_and_d_class import DNDGame


def get_game_with_no_dangers_near_start(uid) -> DNDGame:
    game: DNDGame = DNDGame(uid)
    while True:
        nearby = game.get_action(0).result.nearby
        if "Pit" not in nearby and "Bat" not in nearby and "Dragon" not in nearby:
            break
        game = DNDGame(uid)
    return game

