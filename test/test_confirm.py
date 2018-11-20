from src.game import does_player1_win

PAPER = "Paper"
SCISSORS = "Scissors"
ROCK = "Rock"


def test_pass():
    assert 1==1

def test_player1_wins():
    assert does_player1_win(ROCK, SCISSORS) == True
    assert does_player1_win(SCISSORS, PAPER) == True


