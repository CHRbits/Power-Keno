
import random

# Game constants
BASE_BET = 1  # Base bet amount in dollars
MAX_NUMBERS = 10  # Maximum numbers chosen
NUM_POOL = 50  # Range of numbers (1-50)
POWER_BONUS_PROBABILITY = 0.1  # 10% chance of Power Bonus
RT_P = 0.96  # RTP: Return to Player percentage (96%)

# Paytable based on number of hits (number of matched numbers)
PAYTABLE = {
    1: 3,    # Matching 1 number pays 3x the bet
    2: 10,   # Matching 2 numbers pays 10x the bet
    3: 50,   # Matching 3 numbers pays 50x the bet
    4: 200,  # Matching 4 numbers pays 200x the bet
    5: 1000, # Matching 5 numbers pays 1000x the bet
    6: 5000, # Matching 6 numbers pays 5000x the bet
    7: 10000,# Matching 7 numbers pays 10000x the bet
    8: 15000,# Matching 8 numbers pays 15000x the bet
    9: 20000,# Matching 9 numbers pays 20000x the bet
    10: 25000,# Matching 10 numbers pays 25000x the bet
}

# Function to calculate the winnings based on the number of matches
def calculate_winnings(matches, power_bonus=False):
    if matches in PAYTABLE:
        payout = PAYTABLE[matches]
        if power_bonus:
            payout *= 2  # Power Bonus doubles the payout
        return payout
    return 0

# Function to play the Power Keno game
def play_game():
    # Player selects up to 10 random numbers (can be customized later for player input)
    chosen_numbers = random.sample(range(1, NUM_POOL + 1), random.randint(1, MAX_NUMBERS))
    print(f"Chosen numbers: {chosen_numbers}")

    # The game randomly selects the drawn numbers (usually 20)
    drawn_numbers = random.sample(range(1, NUM_POOL + 1), 20)
    print(f"Drawn numbers: {drawn_numbers}")

    # Calculate the number of matches
    matches = len(set(chosen_numbers) & set(drawn_numbers))
    print(f"Matches: {matches}")

    # Determine if the player wins the Power Bonus
    power_bonus = random.random() < POWER_BONUS_PROBABILITY
    if power_bonus:
        print("Power Bonus activated! Winnings doubled.")

    # Calculate winnings based on the matches and power bonus
    winnings = calculate_winnings(matches, power_bonus)
    
    # Final result
    if winnings > 0:
        print(f"Congratulations! You won {winnings * BASE_BET}$")
    else:
        print("Sorry, no matches this time. Better luck next time!")

# Run the game
if __name__ == "__main__":
    play_game()
