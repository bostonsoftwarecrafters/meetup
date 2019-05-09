from dnd_constants import DND_OBJECT
from mock_game_class import MockGame

def test_nearby():
    mock_board_game = MockGame("A1")
    start_cell = mock_board_game.get_actions()[0].result
    assert start_cell.nearby == ""

def test_object_nearby_functions():
    for dnd_object in DND_OBJECT:
        functest_object_nearby(dnd_object)


def assert_using_nearby_function(cell, dnd_object):
    if dnd_object == DND_OBJECT.BAT:
        assert cell.is_bat_nearby()
    elif dnd_object == DND_OBJECT.DRAGON:
        return cell.is_dragon_nearby()
    elif dnd_object == DND_OBJECT.MAGIC_ARROW:
        return cell.is_magic_arrow_nearby()
    elif dnd_object == DND_OBJECT.PIT:
        return cell.is_pit_nearby()
    elif dnd_object == DND_OBJECT.ROPE:
        return cell.is_rope_nearby()
    else:
        assert False




def functest_object_nearby(dnd_object):
    mock_game = MockGame("A1")
    mock_game.add_object_location(dnd_object, "F3")
    g2_cell = mock_game.make_mock_cell("G2")
    assert g2_cell.nearby == ""
    for location in mock_game.get_adjacent_locations("F3"):
        cell = mock_game.make_mock_cell(location)
        assert_using_nearby_function(cell, dnd_object)



