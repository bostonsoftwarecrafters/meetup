# test changes 2
PAPER = "Paper"
ROCK = "Rock"
SCISSORS = "Scissors"

def get_winning_player(player1_hand, player2_hand, player3_hand = None):
    if player3_hand == None:
        return get_two_player_winner(player1_hand, player2_hand)
    else:
        return get_three_player_winner(player1_hand, player2_hand, player3_hand)


def get_three_player_winner(player1_hand, player2_hand, player3_hand):
    player1v2 = get_two_player_winner(player1_hand, player2_hand)
    player1v3 = get_two_player_winner(player1_hand, player3_hand)
    player2v3 = get_two_player_winner(player2_hand, player3_hand)
    if (player1v2 == 1 and player1v3 == 1):
        return 1
    elif (player1v2 == 2 and player2v3 == 1): #change this!
        return 2
    else:
        return 0


def get_two_player_winner(player1_hand, player2_hand):
    PLAYER2_WINS = {(SCISSORS,ROCK):True,(ROCK,PAPER):True,(PAPER,SCISSORS):True}
    if player1_hand == player2_hand:
        return 0
    try:
        does_player2_win = PLAYER2_WINS[(player1_hand, player2_hand)]
        return 2
    except:
        return 1
