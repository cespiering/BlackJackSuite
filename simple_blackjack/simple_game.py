# Create a basic black jack game with CLI, one deck, no cards removed, no betting
import random as r

def deal_card():
    """returns a random card from the available options"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return r.choice(cards)

def calculate_score(lst):
    """calculates running score, 0 is representing blackjack"""
    score =  sum(lst)
    if len(lst) == 2 and score == 21:
        return 0
    elif score > 21 and 11 in lst:
        lst.remove(11)
        lst.append(1)
        score = sum(lst)
    return score

def determine_winner(dealer_score, player_score):
    """compares scores after game play is over, determines the winner"""
    if dealer_score == 0 and player_score == 0:
        print("You and the dealer both have blackjack. Push")
    elif dealer_score == 0:
        print('Dealer gets Blackjack')
    elif player_score == 0:
        print("You got Blackjack")
    elif dealer_score > 21:
        print("Dealer busts")
    elif dealer_score == player_score:
        print(f'You and the dealer both have {player_score}. Push')
    elif dealer_score > player_score:
        print(f"Dealer wins with {dealer_score}")
    else:
        print(f"You win with {player_score}")

def play_game():
    """game play function"""
    dealer_hand = []
    player_hand = []
    #initial deal
    for i in range(2):
        dealer_hand.append(deal_card())
        player_hand.append(deal_card())

    player_turn_over = False

    while not player_turn_over:
        player_score = calculate_score(player_hand)
        dealer_score = calculate_score(dealer_hand)

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            player_turn_over = True
        else:
            print(f"You have {player_score} and the dealer has a {dealer_hand[1:]} showing")
            action = input("Hit or Stay? (h or s): ")
            if action == 'h':
                player_hand.append(deal_card())
            else:
                print(f"You are staying at {player_score}")
                player_turn_over = True
    if player_score > 21:
            print("You bust")
    else:
        while dealer_score !=0 and dealer_score < 17:
            dealer_hand.append(deal_card())
            dealer_score = calculate_score(dealer_hand)
        determine_winner(dealer_score, player_score)


while input("Would you like to play? y or n: ") == 'y':
    
    play_game()

