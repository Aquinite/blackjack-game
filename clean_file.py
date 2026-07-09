from art import logo
import random


def blackjack():
    """Function to run blackjack program. Determines whether function play runs or not."""
    blackjack_start = input("Do you want to play blackjack? Type y for yes, n for no:\n").lower()
    if blackjack_start == "y":
        play()
    if blackjack_start == "n":
        print("K. Bye.")
    else:
        blackjack()

def deal_card():
    """Deals the cards to use for blackjack. Returns a random card from the list 'cards'."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards_in_hand):
    """Calculates the score of one's cards and returns its sum."""
    while sum(cards_in_hand) > 21 and 11 in cards_in_hand:
        cards_in_hand[cards_in_hand.index(11)] = 1
    return sum(cards_in_hand)

def play():
    """Function to play the actual game."""
    print(logo)
    your_cards = [deal_card() for _ in range(2)]
    computer_cards = [deal_card() for _ in range(2)]
    def print_cards():
        """Prints your current cards and it's sums, together with the computer's first card."""
        print("Your cards:",your_cards,f"Current score: {calculate_score(your_cards)}")
        print("Computer's first card:",computer_cards[0])

    def print_cards_final():
        """Prints the computer's and your final cards together with their respective sums."""
        print("Your cards:",your_cards,f"Current score: {calculate_score(your_cards)}")
        print("Computer's cards:",computer_cards,f"Computer score: {calculate_score(computer_cards)}")

    print_cards()

    def computer_hits():
        """Determines whether the computer adds more cards to their deck or not."""
        sum_of_computer_cards = calculate_score(computer_cards)
        if sum_of_computer_cards < 17:
            computer_cards.append(deal_card())
            computer_hits()
        elif 17 <= sum_of_computer_cards < 21:
            hit_or_not = random.randint(1,3)
            if hit_or_not == 1:
               computer_cards.append(deal_card())
               computer_hits()
        return None

    def win_condition():
        """Determines who wins the game based on sum of your cards and the computer's cards."""
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
        """Allows user to keep adding cards to their deck if desired. If not, then ends the game and starts blackjack again."""
        hit_again = input("Do you want to hit again? Type y for yes, n for no:\n").lower()
        if hit_again == "y":
            your_cards.append(deal_card())
            if calculate_score(your_cards) <= 21:
                print_cards()
                lets_keep_hitting()
            elif calculate_score(your_cards) > 21:
                print_cards_final()
                win_condition()
                blackjack()
        elif hit_again == "n":
            computer_hits()
            print_cards_final()
            win_condition()
            blackjack()
    lets_keep_hitting()

blackjack()


