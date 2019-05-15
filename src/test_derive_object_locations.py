from dnd_constants import MAGIC_ARROW_STR, ROPE_STR, DRAGON_STR, PIT_STR
from game_direction_class import EAST
from mock_game_class import MockGame


def test_derive_bat_visited(safe_mock_game_g3_setup_teardown):
    mock_game = safe_mock_game_g3_setup_teardown
    mock_game.set_mock_bat(move=3, location="G6", fly_to="C7")
    action_1 = mock_game.do_action_move(EAST,"G4 - not near bats")
    action_2 = mock_game.do_action_move(EAST,"G5 - not near bats")
    action_3 = mock_game.do_action_move(EAST,"G6 - bat will fly to C7")
    mock_game.derive_contents()
    assert mock_game.get_derived_fly_to(action_index=3, bat_location="G6") == "C7"
    assert len(mock_game.get_derived_fly_tos()) == 1


def test_derive_visited_dragon():
    mock_game:MockGame = MockGame("G3")
    mock_game.set_mock_object_location(DRAGON_STR, "G5")
    mock_game.do_action_move(EAST,"G4 - empty cell")
    mock_game.do_action_move(EAST,"G5 - Dragon")
    mock_game.derive_contents()
    assert mock_game.get_derived_contents()["G5"] == [DRAGON_STR]

def test_derive_visited_pit():
    mock_game:MockGame = MockGame("G3")
    mock_game.set_mock_object_location(PIT_STR, "G5")
    mock_game.do_action_move(EAST,"G4 - empty cell")
    mock_game.do_action_move(EAST,"G5 - Dragon")
    mock_game.derive_contents()
    assert mock_game.get_derived_contents()["G5"] == [PIT_STR]

def test_derive_picked_up_inventory():
    mock_game:MockGame = MockGame("G3")
    mock_game.set_mock_object_location(MAGIC_ARROW_STR, "G5")
    mock_game.set_mock_object_location(ROPE_STR, "G7")
    mock_game.do_action_move(EAST,"G4 - empty cell")
    mock_game.do_action_move(EAST,"G5 - Magic Arrow")
    mock_game.do_action_move(EAST,"G6 - Empty Cell")
    mock_game.do_action_move(EAST,"G7 - Rope")
    mock_game.do_action_move(EAST,"G8 - Empty cell")
    mock_game.derive_contents()
    assert mock_game.get_derived_contents()["G4"] == []
    assert mock_game.get_derived_contents()["G5"] == [MAGIC_ARROW_STR]
    assert mock_game.get_derived_contents()["G6"] == []
    assert mock_game.get_derived_contents()["G7"] == [ROPE_STR]
    assert mock_game.get_derived_contents()["G8"] == []
