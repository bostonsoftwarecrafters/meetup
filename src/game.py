PAPER = "Paper"
SCISSORS = "Scissors"
ROCK = "Rock"

def get_winning_player(player1_hand, player2_hand):
    if player1_hand == SCISSORS and player2_hand == ROCK:
        return 2
    elif player1_hand == player2_hand:
        return 0
    return 1