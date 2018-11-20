from src.game import get_winning_player

PAPER = "Paper"
SCISSORS = "Scissors"
ROCK = "Rock"


def test_pass():
    assert 1==1

def test_player1_wins():
    assert get_winning_player(ROCK, SCISSORS) == 1
    assert get_winning_player(SCISSORS, PAPER) == 1


