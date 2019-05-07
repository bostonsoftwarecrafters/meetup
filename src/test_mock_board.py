from mock_game_class import MockGame

def test_nearby():
    mock_board_game = MockGame("A1")
    start_cell = mock_board_game.get_action_history()[0].result
    assert start_cell.nearby == ""

def test_nearby_bats():
    mock_board_game = MockGame("A1")
    mock_board_game.add_bat("F3")
    f4_cell = mock_board_game.make_mock_cell("F4")
    f2_cell = mock_board_game.make_mock_cell("F2")
    e3_cell = mock_board_game.make_mock_cell("E3")
    g3_cell = mock_board_game.make_mock_cell("G3")
    g2_cell = mock_board_game.make_mock_cell("G2")

    assert g2_cell.nearby == ""
    assert f4_cell.nearby == "Bats"
    assert f2_cell.nearby == "Bats"
    assert g3_cell.nearby == "Bats"
    assert e3_cell.nearby == "Bats"
