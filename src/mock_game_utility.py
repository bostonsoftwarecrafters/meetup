from d_and_d_class import DNDGame
from mock_game_class import MockGame

def derive_mock_game(game: DNDGame):
    mock_game = MockGame(game.get_action(0).result.location)
    # TODO: Add functions to find objects
    # mock_game.find_pits_and_dragon()
    return mock_game



