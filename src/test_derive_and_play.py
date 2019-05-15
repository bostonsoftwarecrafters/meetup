from dnd_constants import MAGIC_ARROW_STR, ROPE_STR, DRAGON_STR
from game_direction_class import NORTH, EAST
from mock_game_class import MockGame
from mock_game_utility import derive_mock_game


def test_mock_pick_up_arrow(safe_mock_game_g3_setup_teardown):
    game_orig = safe_mock_game_g3_setup_teardown
    assert_move_to_obj(game_orig, MAGIC_ARROW_STR)

def test_mock_pick_up_rope(safe_mock_game_g3_setup_teardown):
    game_orig = safe_mock_game_g3_setup_teardown
    assert_move_to_obj(game_orig, ROPE_STR)

def test_mock_move_to_dragon(safe_mock_game_g3_setup_teardown):
    game_orig = safe_mock_game_g3_setup_teardown
    assert_move_to_obj(game_orig, DRAGON_STR)

def test_mock_move_to_pit(safe_mock_game_g3_setup_teardown):
    game_orig = safe_mock_game_g3_setup_teardown
    assert_move_to_obj(game_orig, DRAGON_STR)

def assert_move_to_obj(game_orig, obj_str):
    game_orig.set_mock_object_location(obj_str, "F5")
    game_orig.do_action_move(EAST, "Go to G4")
    game_orig.do_action_move(EAST, "Go to G5")
    game_orig.do_action_move(NORTH, "Go to F5 pick up "+obj_str)
    game_orig.do_action_move(EAST, "Go to F6")
    game_derived: MockGame = derive_mock_game(game_orig)
    assert game_derived.get_mock_object_location(obj_str) == ["F5"]
    orig_action_objs = game_orig.get_actions()
    for action_index in range(1, len(orig_action_objs)):
        action = game_orig.get_action(action_index)
        game_derived.do_action_move(action.direction, "Test mock simple game")
    for action_index in range(0, len(orig_action_objs)):
        orig_action_obj = game_orig.get_action(action_index)
        derived_action_obj = game_derived.get_action(action_index)
        assert orig_action_obj.key_field_equals(derived_action_obj)


def test_derive_mock_game_start(safe_mock_game_g3_setup_teardown):
    original_game = safe_mock_game_g3_setup_teardown
    original_action = original_game.get_actions()[0]
    original_location = original_action.result.location
    mock_game = derive_mock_game(original_game)
    mock_action_and_result = mock_game.get_actions()[0]
    cell_visited = mock_game.get_cells_visited()[original_location]
    assert mock_action_and_result.action == "restart"
    assert cell_visited.location == original_location
    assert mock_action_and_result.result.location == original_location