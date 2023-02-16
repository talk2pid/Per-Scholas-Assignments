Game Code
# Set up initial game state
score = [0, 0]  # [Player score, Computer score]
possessor = random.choice(['player', 'computer'])  # Randomly choose who gets to start with the ball

# Define function to simulate a shot
def shoot():
    return random.choice(['scored', 'missed'])

# Define function to simulate a pass
def pass_ball():
    return random.choice(['successful', 'intercepted'])

# Main game loop
while True:
    # Display game state
    print(f"Score: Player {score[0]} - {score[1]} Computer")
    print(f"The {possessor} has the ball. What do you want to do?")
    action = input("Enter 'p' to pass or 's' to shoot: ")
    
    # Handle player action
    if action == 'p':
        outcome = pass_ball()
        if outcome == 'successful':
            print("You successfully passed the ball.")
            possessor = 'computer'  # Change possession to the computer
        else:
            print("Your pass was intercepted!")
            possessor = 'player'  # Change possession back to the player
        
    elif action == 's':
        outcome = shoot()
        if outcome == 'scored':
            print("GOAL!! You scored!")
            score[0] += 1  # Increase player score
        else:
            print("Aww, you missed.")
            possessor = 'computer'  # Change possession to the computer
        
    else:
        print("Invalid action. Please enter 'p' or 's'.")
        continue
        
    # Handle computer action
    if possessor == 'computer':
        print("The computer has the ball.")
        action = random.choice(['p', 's'])
        
        if action == 'p':
            outcome = pass_ball()
            if outcome == 'successful':
                print("The computer successfully passed the ball.")
                possessor = 'player'  # Change possession to the player
            else:
                print("The computer's pass was intercepted!")
                possessor = 'computer'  # Change possession back to the computer
        
        elif action == 's':
            outcome = shoot()
            if outcome == 'scored':
                print("GOAL!! The computer scored.")
                score[1] += 1  # Increase computer score
            else:
                print("The computer missed.")
                possessor = 'player'  # Change possession to the player
    
    # Check for game end
    if score[0] >= 3:
        print("Congratulations, you win!")
        break
    elif score[1] >= 3:
        print("Sorry, you lost.")
        break