############### Our Blackjack House Rules #####################
# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.

from art import logo
import os
import random


def deal_cards(user_cards, k=1):
    """
    Deals cards at random from cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] and adds to the user cards 
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    drawn_cards = random.choices(cards, k=k)
    if k == 2:
        if drawn_cards[0] == 11 and drawn_cards[1] == 11:
            user_cards.extend([11, 1])
    user_cards.extend(drawn_cards)


def calculate_score(user_cards):
    """Calculates score for given hand of cards """
    if len(user_cards) == 2 and sum(user_cards) == 21:
        return 0
    elif 11 in user_cards and sum(user_cards) > 21:
        user_cards.remove(11)
        user_cards.append(1)
    return sum(user_cards)


def outcome(player_score, computer_score):
    """ Returns a message of outcome of the game based on the player and computer scores. """
    messages = {
        "computer blackjack": "Opponent got Blackjack, You Lose 😤",
        "player blackjack": "You win with Blackjack 😎",
        "win": "You Win 😀",
        "lose": "You Lose 😤",
        "draw": "Draw 🙃",
        "player over": "You Went Over, You Lose 😤",
        "computer over": "Opponent Went Over. You Win 😁",
    }

    if computer_score == player_score:
        return messages["draw"]
    elif computer_score == 0:
        return messages["computer blackjack"]
    elif player_score == 0:
        return messages["player blackjack"]
    elif player_score > 21:
        return messages["player over"]
    elif computer_score > 21:
        return messages["computer over"]
    elif player_score > computer_score:
        return messages["win"]
    else:
        return messages["win"]


def blackjack():

    print(logo)
    player = {
        "cards": [],
        "score": 0,
    }
    computer = {
        "cards": [],
        "score": 0,
    }

    is_game_over = False

    deal_cards(player["cards"], 2)
    deal_cards(computer["cards"], 2)

    while not is_game_over:
        player["score"] = calculate_score(player["cards"])
        computer["score"] = calculate_score(computer["cards"])
        print(
            f"Your cards: {player['cards']}, current score: {player['score']}"
        )
        print(f"Computer's first card: {computer['cards'][0]}")
        if player["score"] == 0 or computer[
                "score"] == 0 or player["score"] > 21:
            is_game_over = True
        else:
            hit = input("Type 'y' to get another card, type 'n' to pass: ")
            if hit == "y":
                deal_cards(player["cards"])
            else:
                is_game_over = True

    while computer["score"] != 0 and computer["score"] < 17:
        deal_cards(computer["cards"])
        computer["score"] = calculate_score(computer["cards"])

    print(
        f"Your final hand: {player['cards']}, final score: {player['score']}"
    )
    print(
        f"Computer's final hand: {computer['cards']}, final score: {computer['score']}"
    )

    print(outcome(player["score"], computer["score"]))
    print(
        "===============================================================")


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    os.system("cls")
    blackjack()
