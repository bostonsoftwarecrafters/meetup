from d_and_d_class import DNDGame
from mock_game_class import MockGame

def derive_mock_game(game: DNDGame):
    mock_game:MockGame = MockGame(game.get_action(0).result.location)
    game.derive_contents()
    derived_location_objects = game.get_derived_contents()
    mock_game.copy_location_objects_to_mock_object_locations(derived_location_objects)
    # TODO: Add functions to find objects
    # mock_game.find_pits_and_dragon()
    return mock_game



