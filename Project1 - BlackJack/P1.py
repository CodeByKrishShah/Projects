import p1_random as P1
rng = P1.P1Random()
option = 1
hand = 0
dealer_hand = 0
player_win = 0
dealer_win = 0
tie_games = 0
total_games = 0
Percentage = 0
card = 0


def menu():
    print("1. Get another card")
    print("2. Hold hand")
    print("3. Print statistics")
    print("4. Exit")
    print()
def cards(hands, card):
    global card_value
    if card in [2, 3, 4, 5, 6, 7, 8, 9, 10]:
        hands += card
        card_value = str(card)
    elif card == 1:
        card_value = "ACE"
        hands += 1
    elif card == 11:
        card_value = "JACK"
        hands += 10
    elif card == 12:
        card_value = "QUEEN"
        hands += 10
    elif card == 13:
        card_value = "KING"
        hands += 10
    return hands, card_value



print(f"START GAME #{total_games + 1}")

while(option != 4):
    print()
    if(option == 1):
        card = rng.next_int(13) + 1
        card_value = str(card)
        hand, card_value = cards(hand, card)
        print(f"Your card is a {card_value}!")
        print(f"Your hand is: {hand}")
        if (dealer_hand > 21):
            print("You win!!")
            player_win += 1
            total_games += 1
            option = 1
            hand = 0
            dealer_hand = 0
            print()
            print(f"START GAME #{total_games + 1}")
            print()
            card = rng.next_int(13) + 1
            card_value = str(card)
            hand, card_value = cards(hand, card)
            print(f"Your card is a {card_value}!")
            print(f"Your hand is: {hand}")
        elif (dealer_hand == 21):
            print("Dealer wins!")
            dealer_win += 1
            total_games += 1
            option = 1
            hand = 0
            dealer_hand = 0
            print()
            print(f"START GAME #{total_games + 1}")
            print()
            card = rng.next_int(13) + 1
            card_value = str(card)
            hand, card_value = cards(hand, card)
            print(f"Your card is a {card_value}!")
            print(f"Your hand is: {hand}")
        elif (hand == 21):
            print("BLACKJACK! You win!")
            player_win += 1
            total_games += 1
            option = 1
            hand = 0
            dealer_hand = 0
            print()
            print(f"START GAME #{total_games + 1}")
            print()
            card = rng.next_int(13) + 1
            card_value = str(card)
            hand, card_value = cards(hand, card)
            print(f"Your card is a {card_value}!")
            print(f"Your hand is: {hand}")
        elif (hand>21):
            print("Dealer Win!")
            dealer_win +=1
            total_games +=1
            option = 1
            hand = 0
            dealer_hand = 0
            print()
            print(f"START GAME #{total_games + 1}")
            print()
            card = rng.next_int(13) + 1
            card_value = str(card)
            hand, card_value = cards(hand, card)
            print(f"Your card is a {card_value}!")
            print(f"Your hand is: {hand}")
        menu()
        option = int(input("Choose an option: "))

    elif(option==2):
        dealer_hand = rng.next_int(11) + 16
        print(f"Dealer's hand: {dealer_hand}")
        print(f"Your hand is: {hand}")
        if(dealer_hand > 21):
            print("You win!")
            player_win +=1
            total_games+=1
            option = 1
            hand = 0
            dealer_hand = 0
            print()
            print(f"START GAME #{total_games + 1}")
        elif(dealer_hand == 21):
            print("Dealer wins!")
            dealer_win += 1
            total_games += 1
            option = 1
            hand = 0
            dealer_hand = 0

            print()
            print(f"START GAME #{total_games + 1}")
        elif(hand == 21):
            print("You win!!")
            player_win += 1
            total_games += 1
            option = 1
            hand = 0
            dealer_hand = 0

            print()
            print(f"START GAME #{total_games + 1}")
        elif(dealer_hand > hand) or (hand>21):
            print("Dealer wins!")
            dealer_win += 1
            total_games+=1
            option = 1
            hand = 0
            dealer_hand = 0

            print()
            print(f"START GAME #{total_games + 1}")

        elif(dealer_hand < hand):
            print("You win!!")
            player_win += 1
            total_games+=1
            option = 1
            hand = 0
            dealer_hand = 0

            print()
            print(f"START GAME #{total_games + 1}")

        elif (dealer_hand == hand):
            print("It's a tie! No one wins!")
            tie_games +=1
            total_games+=1
            option = 1
            hand = 0
            dealer_hand = 0
            print()
            print(f"START GAME #{total_games + 1}")


    elif(option == 3):

        percentage = float((player_win/total_games)*100)
        print(f"Number of Player wins: {player_win}")
        print(f"Number of Dealer wins: {dealer_win}")
        print(f"Number of tie games: {tie_games}")
        print(f"Total # of games played is: {total_games}")
        print(f"Percentage of Player wins: {percentage:.1f}%")
        menu()
        option = int(input("Choose an option: "))

    else:
        print("Invalid input!")
        print("Please enter an integer value between 1 and 4.")
        menu()
        option = int(input("Choose an option: "))
