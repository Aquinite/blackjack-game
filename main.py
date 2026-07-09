from art import logo
import random

#
# Problem: Create a blackjack game with the ff rules:
#     Unli deck size
#     no jokers
#     jack, queen, king is all 10
#     ace is either 11 or 1
#     cards in list have equal probability of being drawn
#     cards not removed from deck
#     computer deals cards to you

# Features
# 1. Asks player if they wanna play blackjack.
# 2. If yes, Needs to be able to randomly select 2 cards from a "deck of cards" then deal you and itself that card, without revealing more than
# 1 of the cards that it dealt to the computer. If no, then aborts the game.
# 3. Game must show you your 2 cards and show how much it adds up to.
# 4.Game must ask you if you want to hit or not:
#     a. if you go over 21, force game to end, show your own cards but not the dealer's cards'
#     b. if not over 21, then ask if you want to hit again or not.
#         b1. if not, then let dealer show his cards (after hitting).
# 5. During the end:
#     a.if the computer's cards add up to less than 17, force dealer to hit.
#     b.if computer cards more than 17, make computer randomly decide to hit or not.
# 6. Game must show that you've lost or won or drew:'
    # a. if you win, must have more points than computer, or got blackjack, or dealer busts.
    # b. If you lose, fewer pts than computer or dealer blackjacks.
    # c. Draw if points are the same.
# 7. Game must loop back to the start if player wants to play again.
#   a. if not, then end game.

# 1. Ask player if they want to play blackjack.


def blackjack():
    """Function to run blackjack program. Determines whether play runs or not."""
    blackjack_start = input("Do you want to play blackjack? Type y for yes, n for nah:\n").lower()
    if blackjack_start == "y":
        play()
    if blackjack_start == "n":
        print("K. Bye.")
    else:
        blackjack()

def deal_card():
    """Deals the cards to use for blackjack. Returns a random card from the list 'cards'."""
    # This works because of the return function. We do not need the "cards" list in other functions as we never use
    # it as a reference in other functions.
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards_in_hand):
    """Calculates the score of one's cards and returns its sum."""
    # Ace can equal 11 or 1 depending on the circumstance.
    # The while function ensures that no matter how many cards are inside your hand, it will keep converting aces into
    # 1 while it is advantageous to you.
    while sum(cards_in_hand) > 21 and 11 in cards_in_hand:
        cards_in_hand[cards_in_hand.index(11)] = 1
#    this line of code above does the ff:
#           - inside parenthesis, it is outputting the position of the number 11 card
#           - in doing so, it allows cards_in_hand[] to output where number 11 is at all times, then turn it into 1
    return sum(cards_in_hand)

def play():
    """Function to play the actual game."""
    print(logo)
    # If yes, Needs to be able to randomly select 2 cards from the "deck of cards" (cards)
    #   then deal you and itself (the computer) cards from the deck.
    your_cards = [deal_card() for _ in range(2)]
    computer_cards = [deal_card() for _ in range(2)]
    def print_cards():
        """Prints your current cards and its sums."""
        # 3. Game must show you your 2 cards and show how much it adds up to.
        print("Your cards:",your_cards,f"Current score: {calculate_score(your_cards)}")
        print("Computer's first card:",computer_cards[0])

    def print_cards_final():
        """Prints the computer and your final cards and their respective sums."""
        print("Your cards:",your_cards,f"Current score: {calculate_score(your_cards)}")
        print("Computer's cards:",computer_cards,f"Computer score: {calculate_score(computer_cards)}")

    print_cards()

# If player does not want to hit anymore, then computer must hit so we can have a win condition.
    def computer_hits():
        """Determines whether the computer hits or not."""
        sum_of_computer_cards = calculate_score(computer_cards)
        if sum_of_computer_cards < 17:
            # a.if the computer's cards add up to less than 17, force dealer to hit.
            computer_cards.append(deal_card())
            computer_hits()
        elif 17 <= sum_of_computer_cards < 21:
        # b.if computer cards is equal or more than 17, make computer randomly decide to hit or not.
        # Only stops when the computer randomly decides not to hit does it stop hitting.
            hit_or_not = random.randint(1,3)
            if hit_or_not == 1:
               computer_cards.append(deal_card())
               computer_hits()
        return None

    def win_condition():
        """Determines who wins blackjack based on sum of your cards and the computer's cards."""
        #  Game must show that you've lost or won or drew:
        #     # a. if you win, must have more points than computer, or got blackjack, or dealer busts.
        #     # b. If you lose, must have fewer points than computer or dealer blackjacks.
        #     # c. Draw if points are the same.
        sum_of_your_cards = calculate_score(your_cards)
        sum_of_computer_cards = calculate_score(computer_cards)
        if sum_of_your_cards == sum_of_computer_cards:
            print("Draw!")
        elif sum_of_your_cards == 21:
            print("Blackjack! You win!")
        elif sum_of_computer_cards == 21:
            print("Computer got blackjack. You lose!")
        elif sum_of_your_cards > 21:
           print("You went over. Bust!")
        elif sum_of_computer_cards > 21:
           print("Computer went over. Bust! You win!")
        elif sum_of_your_cards > sum_of_computer_cards:
            print("You won!")
        elif sum_of_your_cards < sum_of_computer_cards:
            print("You lost!")

    def lets_keep_hitting():
        """Allows user to keep adding cards if desired. If not, then ends the game and starts blackjack again."""
        # if not over 21 or equal 21, then ask if you want to hit again or not.
        # You should be able to do this while not over 21 yet.
        hit_again = input("Do you want to hit again? Type y for yes, n for nah:\n").lower()
        if hit_again == "y":
            your_cards.append(deal_card())
            if calculate_score(your_cards) <= 21:
                print_cards()
                lets_keep_hitting()
            elif calculate_score(your_cards) > 21:
                # a. if you go over 21, force game to end, show your own cards but not the dealer's cards.
                print_cards_final()
                win_condition()
                blackjack()
        elif hit_again == "n":
            #   If player doesn't want to hit again, then let dealer show his cards (after letting dealer hit depending on below).
            #  Then compare the scores.
            computer_hits()
            print_cards_final()
            win_condition()
            blackjack()
            # 7. Game must loop back to the start if player wants to play again.
    lets_keep_hitting()

blackjack()


