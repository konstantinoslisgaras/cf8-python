import random

"""
Simple rock paper scissors game that is 33% "rigged" in favor of the computer.
"""

def print_welcome_message() -> None:
    """
    Simple welcome message.
    """
    print("\n" + "="*10, "Welcome to my Rock/Paper/Scissors app!!!", "="*10)
    print("Are you ready to beat the 'Computer'?")

def get_total_win_points() -> int:
    """
    Takes as input from the player the victory points required for the win. Range is between 3 and 10.

    Returns:
        points (int): The points required for the winner.
    """
    while True:
        try:
            points = int(input("Set the victory points (3-10): "))
            if 2 < points <= 10:
                return points
            else:
                print("Invalid Input.")
                continue
        except ValueError:
            print("Please enter a number between 3 and 10 to set the victory points.")
            continue

def is_valid(input) -> bool:
    """
    Strips and lowers user input and then checks if it is in the list of the valid options.
    Added more options for simplicity (eg. For 'Rock', invalid inputs can be ROCK, rOck, r, 1)

    Params:
        input (str): The user's choice between rock, paper, scissors.

    Returns:
        bool: True if the choice is in the list of valid options, False otherwise.
    """
    options = ['rock', 'paper', 'scissors', 'r', 'p', 's', "1", "2", "3"]
    return input.lower().strip() in options

def get_player_choice() -> str:
    """
    Check if player's choice is valid and then normalizes the player's choice. (eg. For 'r' or '1' or 'ROCK' returns 'Rock')

    Returns:
        choice (str): The normalized player's choosen option between Rock, Paper, Scissors.
    """    
    while True:
        try:
            choice = input("1.Rock/2.Paper/3.Scissors (r,p,s)?: ")
            if is_valid(choice):
                if choice in ('rock', 'r', '1'):
                    return 'Rock'
                elif choice in ('paper', 'p', '2'):
                    return 'Paper'
                else:
                    return 'Scissors'
            else:
                print("Invalid choice.")
        except ValueError:
            continue

def get_computer_choice(player_input) -> str:
    """
    Here is where the cheat happens with the help of two functions.

    1.The first one legit and randomly picks one of the 3 valid options (Rock, Paper, Scissors) and returns that option. Probability for this scenario: 66%.

    2.The second one takes as a parameter the normalized players option and picks the one that beats it. For example if player has picked 'Rock' computers picks 'Paper'.
    Probability for this scenario: 33%

    Params:
        player_input (str): The normalized user's choice between rock, paper, scissors.

    Returns:
        computer_choice (str): A randomly picked function between the cheat pick one (33%) and the random legit one (66%).
    """    
    players_choice = player_input

    def get_computer_choice_random() -> str:
        options = ['Rock', 'Paper', 'Scissors']
        return random.choice(options)

    def get_computer_choice_cheat() -> str:
        nonlocal players_choice
        if players_choice == 'Rock':
            return 'Paper'
        elif players_choice == 'Paper':
            return 'Scissors'
        else:
            return 'Rock'
    
    computer_choices = [get_computer_choice_random, get_computer_choice_random, get_computer_choice_cheat]
    return random.choice(computer_choices)()

def is_game_finished(player_points: int, computer_points: int, victory_points: int) -> bool:
    """
    Control function that checks at every game round if the game has finished which means if the Player or the Computer has reached the necessary winning points.

    Params:
        player_points (int): The Player's points.
        computer_points (int): The Computer's points.
        victory_points (int): The points necessary to win the game (range is 3 - 10).

    Returns:
        bool: False if the game is not finished, True otherwise.
    """    
    return player_points == victory_points or computer_points == victory_points

def get_round_winner(player_input: str, computer_choice: str) -> str:
    """
    Takes as input the Player's and the Computer's choices between Rock, Paper, Scissors for every round and 'calculates' the winner or the tie if both Player and Computer made the same choice; Constructs a string as key and returns the value from a dictionary of all the possible 9 outcomes.

    Params:
        player_input (str): The Player's input.
        computer_choice (str): The Computer's choice.

    Returns:
        outcome (str)): The outcoume of the round (e.g. "Tie").
    """      
    outcome = f"{player_input}, {computer_choice}"
    possible_outcomes = {
        "Rock, Rock" : "Tie",
        "Rock, Paper" : "Computer",
        "Rock, Scissors" : "Player",
        "Paper, Paper" : "Tie",
        "Paper, Rock" : "Player",
        "Paper, Scissors" : "Computer",
        "Scissors, Scissors" : "Tie",
        "Scissors, Rock" : "Computer",
        "Scissors, Paper" : "Player" 
    }
    return possible_outcomes[outcome]

def add_winner_points(winner: str) -> tuple:
    """
    Simple function that takes the winner as the parameter and awards the point to accordingly. Returns 0, 0 if the round was a "Tie".

    Params:
        winner (str): The winner of the round (e.g. "Computer").

    Returns:
        tuple: 0-1, 0-1 according to the winner to get unpacked in main.
    """       
    match winner:
        case "Tie":
            return 0, 0
        case "Player":
            return 1, 0
        case "Computer":
            return 0, 1
    
def print_round(round_number: int) -> None:
    """
    Simple round counter print function to easily separate the rounds.

    Params:
        round_number (str): The round number of the game.
    """           
    print(f"========== ROUND {round_number} ==========")

def print_status(player_input: str, player_points: int, computer_choice: str, computer_points: int, round_winner: str) -> None:
    """
    Simple status print function to announce the round winner and to show the points of the Player and the Computer.

    Params:
        player_input (str): Player's choice to show in console.
        player_points (str): Player's points to show in console.
        computer_input (str): Computer's choice to show in console.
        computer_points (str): Computer's points to show in console.
        round_winner (str): Round winner to show in console.        
    """  
    if round_winner == "Tie":
        print(f"\n**TIE** |PLAYER| {player_input} VS {computer_choice} |Computer|")
    else:
        print(f"\n**{round_winner} WINS** |Player| {player_input} VS {computer_choice} |Computer|")
    print(f"PLAYER points: {player_points} - Computer points: {computer_points}", end="\n\n")

def print_winner_message(victory_points, player_points, computer_points):
    """
    Simple end game print function to announce the final winner with the appropriate emoji. Easter egg for a tie if rounds**2 have been played and there is still no winner. 

    Params:
        victory_points (str): The points required for the winner.
        player_points (str): Player's final points to show in console.
        computer_points (str): Computer's final points to show in console.   
    """
    print("="*45)
    print(f"\tReached winning points(?)({victory_points})")
    print(f"\tWinner is {
        'PLAYER 🙎' if player_points > computer_points 
        else 'Computer 🤖' if computer_points > player_points 
        else 'NOONE ⛓️‍💥'} !!!")
    print("="*45)
            
def main():
    print_welcome_message()
    victory_points = get_total_win_points()
    player_points = 0
    computer_points = 0
    round_number = 0

    while not (is_game_finished(player_points, computer_points, victory_points)):
        if (round_number == victory_points ** 2):
            print("Max rounds reached... Game ending...")
            break
        round_number +=1
        print_round(round_number)
        player_input = get_player_choice()
        computer_choice = get_computer_choice(player_input)
        round_winner = get_round_winner(player_input, computer_choice)
        points_to_add = add_winner_points(round_winner)
        player_points += points_to_add[0]
        computer_points += points_to_add[1]
        print_status(player_input, player_points, computer_choice, computer_points, round_winner)
    
    print_winner_message(victory_points, player_points, computer_points)
        
if __name__ == "__main__":
    main()