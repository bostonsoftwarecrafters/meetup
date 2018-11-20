PAPER = "Paper"
SCISSORS = "Scissors"
ROCK = "Rock"

def get_winning_player(player1_hand, player2_hand):
    outcomes = {(SCISSORS,ROCK):2,(ROCK,PAPER):2}

    if player1_hand == player2_hand:
        return 0
    try:
        result = outcomes[(player1_hand,player2_hand)]
        return result
    except:
        return 1

    # elif player1_hand == SCISSORS and player2_hand == ROCK:
    #     return 2
    # elif player1_hand == ROCK and player2_hand == PAPER:
    #     return 2
