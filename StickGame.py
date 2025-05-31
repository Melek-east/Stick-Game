print('''{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}
{}██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗    ████████╗ ██████╗ {}
{}██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝    ╚══██╔══╝██╔═══██╗{}
{}██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗         ██║   ██║   ██║{}
{}██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝         ██║   ██║   ██║{}
{}╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗       ██║   ╚██████╔╝{}
{} ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝       ╚═╝    ╚═════╝ {}
{}████████╗██╗  ██╗███████╗                                                           {}
{}╚══██╔══╝██║  ██║██╔════╝                                                           {}
{}   ██║   ███████║█████╗                                                             {}
{}   ██║   ██╔══██║██╔══╝                                                             {}
{}   ██║   ██║  ██║███████╗                                                           {}
{}   ╚═╝   ╚═╝  ╚═╝╚══════╝                                                           {}
{}███████╗████████╗██╗ ██████╗██╗  ██╗ ██████╗  █████╗ ███╗   ███╗███████╗            {}
{}██╔════╝╚══██╔══╝██║██╔════╝██║ ██╔╝██╔════╝ ██╔══██╗████╗ ████║██╔════╝            {}
{}███████╗   ██║   ██║██║     █████╔╝ ██║  ███╗███████║██╔████╔██║█████╗              {}
{}╚════██║   ██║   ██║██║     ██╔═██╗ ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝              {}
{}███████║   ██║   ██║╚██████╗██║  ██╗╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗            {}
{}╚══════╝   ╚═╝   ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝            {}
{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}''')

import random
import os

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_sticks(count):
    """Display sticks with better visualization."""
    print(f"\nSticks remaining: {count}")
    print("🔴 " * count)
    print("=" * 40)

def get_valid_stick_count(prompt, max_sticks):
    """Get valid stick count from user input."""
    while True:
        try:
            count = int(input(prompt))
            if 1 <= count <= 3 and count <= max_sticks:
                return count
            print(f"Invalid input. Choose 1-3 sticks (not more than {max_sticks} remaining).")
        except ValueError:
            print("Please enter a valid number.")

def get_computer_move(sticks, difficulty):
    """Get computer move based on difficulty level."""
    if difficulty == "easy":
        return random.randint(1, min(3, sticks))
    elif difficulty == "medium":
        # 70% chance of optimal move, 30% chance of random move
        if random.random() < 0.7:
            return sticks % 4 if sticks % 4 != 0 else random.randint(1, min(3, sticks))
        else:
            return random.randint(1, min(3, sticks))
    else:  # hard
        return sticks % 4 if sticks % 4 != 0 else random.randint(1, min(3, sticks))

def play_with_computer():
    """Play Stick Game against the computer with difficulty levels."""
    clear_screen()
    print("=== PLAY AGAINST COMPUTER ===")
    
    # Get number of sticks
    while True:
        try:
            sticks = int(input("\nHow many sticks do you want to play with? "))
            if sticks > 0:
                break
            print("Please enter a positive number of sticks.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Get difficulty level
    while True:
        difficulty = input("\nChoose difficulty (easy/medium/hard): ").strip().lower()
        if difficulty in ["easy", "medium", "hard"]:
            break
        print("Invalid choice. Please enter 'easy', 'medium', or 'hard'.")
    
    # Determine who goes first
    choice = input("\nDo you want to go first? (yes/no): ").strip().lower()
    user_turn = choice.startswith("y")
    
    display_sticks(sticks)
    
    while sticks > 0:
        if user_turn:
            human = get_valid_stick_count("Your turn. How many sticks do you want to remove? ", sticks)
            sticks -= human
            clear_screen()
            print(f"You removed {human} stick(s).")
            if sticks == 0:
                print("\n🎉 You win! 🎉")
                break
            display_sticks(sticks)
        else:
            computer = get_computer_move(sticks, difficulty)
            sticks -= computer
            print(f"\nComputer removes {computer} stick(s).")
            if sticks == 0:
                print("\n😢 Computer wins! You lost. 😢")
                break
            display_sticks(sticks)
        user_turn = not user_turn

def play_with_friend():
    """Play Stick Game against a friend."""
    clear_screen()
    print("=== PLAY AGAINST FRIEND ===")
    
    # Get number of sticks
    while True:
        try:
            sticks = int(input("\nHow many sticks do you want to play with? "))
            if sticks > 0:
                break
            print("Please enter a positive number of sticks.")
        except ValueError:
            print("Please enter a valid number.")

    display_sticks(sticks)
    
    player = 1
    while sticks > 0:
        move = get_valid_stick_count(f"PLAYER {player}: How many sticks do you want to remove? ", sticks)
        sticks -= move
        clear_screen()
        print(f"Player {player} removed {move} stick(s).")
        if sticks == 0:
            print(f"\n🎉 PLAYER {player} WINS! 🎉")
            break
        display_sticks(sticks)
        player = 2 if player == 1 else 1

def show_rules():
    """Display game rules."""
    clear_screen()
    print("=== STICK GAME RULES ===")
    print("1. The game starts with a pile of sticks.")
    print("2. Players take turns removing 1, 2, or 3 sticks.")
    print("3. The player who takes the last stick wins.")
    print("4. The computer has different difficulty levels:")
    print("   - Easy: Makes random moves")
    print("   - Medium: Sometimes makes optimal moves")
    print("   - Hard: Always makes optimal moves when possible")
    input("\nPress Enter to return to the main menu...")

def main():
    """Main game loop."""
    while True:
        clear_screen()
        print("=== STICK GAME ===")
        print("1. Play against Computer")
        print("2. Play against Friend")
        print("3. Game Rules")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            play_with_computer()
        elif choice == "2":
            play_with_friend()
        elif choice == "3":
            show_rules()
        elif choice == "4":
            print("\nGoodbye! 👋")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
            continue
        
        if choice in ["1", "2"]:
            again = input("\nDo you want to play again? (yes/no): ").strip().lower()
            if not again.startswith("y"):
                print("\nGoodbye! 👋")
                break

if __name__ == "__main__":
    main()
