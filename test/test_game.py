from src.game import get_winning_player, PAPER, SCISSORS, ROCK

def test_player1_wins():
    assert 1 == get_winning_player(ROCK, SCISSORS)
    assert 1 == get_winning_player(SCISSORS, PAPER)


def test_player2_wins():
    assert 2 == get_winning_player(SCISSORS, ROCK)
    assert 2 == get_winning_player(ROCK, PAPER)


def test_two_way_tie():
    assert 0 == get_winning_player(PAPER, PAPER)


def test_three_way_tie():
    assert 0 == get_winning_player(ROCK, PAPER, SCISSORS)

def test_player1_of_3_wins():
    assert 1 == get_winning_player(ROCK, SCISSORS, SCISSORS)

def test_player2_of_3_wins():
    assert 2 == get_winning_player(PAPER, SCISSORS, PAPER)
