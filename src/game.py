# test changes 2
PAPER = "Paper"
ROCK = "Rock"
SCISSORS = "Scissors"

def get_winning_player(player1_hand, player2_hand, player3_hand = None):
    if player3_hand == None:
        return get_two_player_winner(player1_hand, player2_hand)
    else:
        return 0


def get_two_player_winner(player1_hand, player2_hand):
    outcomes = {(SCISSORS,ROCK):2,(ROCK,PAPER):2}
    if player1_hand == player2_hand:
        return 0
    try:
        result = outcomes[(player1_hand, player2_hand)]
        return result
    except:
        return 1
