from art import logo, vs 
from game_data import data
import random
from replit import clear

# Select insta account randomly
def select_insta_account():
    """Randomly selects install account from data"""
    return random.choice(data)

# Check of user choise is correct
def get_high_followers(a, b):
    """Returns account with highest followers"""
    if a["follower_count"] > b["follower_count"]:
        return "A"
    else:
        return "B"

def format_data(account):
    """Takes the account data and returns the printable format."""
    return f"{account['name']}, a {account['description']}, from {account['country']}"
    
def high_low():
    is_game_over = False
    A = select_insta_account()
    score = 0
    print(logo)
    while not is_game_over:
        B = select_insta_account()
        if A == B:
            B = select_insta_account()
        answer = get_high_followers(A, B)
        print(f"Pssst, correct answer is {answer}")

        print(f"Compare A: {format_data(A)}")
        print(vs)
        print(f"Against B: {format_data(B)}")
        
        guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        clear()
        print(logo)
        
        if guess == answer:
            score += 1
            print(f"You're right! Current Score: {score}")
        else:
            print(f"Sorry, that's wrong. Final Score: {score}")
            is_game_over = True
            
        A = B

high_low()



