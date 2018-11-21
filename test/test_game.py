from src.game import get_winning_player, PAPER, SCISSORS, ROCK

def test_player1_wins():
    assert get_winning_player(ROCK, SCISSORS) == 1
    assert get_winning_player(SCISSORS, PAPER) == 1

def test_player2_wins():
    assert get_winning_player(SCISSORS, ROCK) == 2
    assert get_winning_player(ROCK,PAPER) == 2

def test_tie():
    assert get_winning_player(PAPER, PAPER) == 0
