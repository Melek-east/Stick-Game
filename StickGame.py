import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_rules():
    print("=== NIM GAME RULES ===")
    print("1. The player will choose how many sticks he want to play with and also the player"
          "\n   can choose the maximum number of sticks to be removed from the pile of sticks.")
    print("2. The game then will start with a pile of sticks.")
    print("3. Players take turns removing 1 to the maximum number of sticks chosen by the player.")
    print("4. The player who takes the last stick wins.")

def display_sticks(sticks):
    row = 1
    while sticks > 0:
        group = min(10, sticks)
        print("Row {:>2}: ".format(row) + "|  " * group)
        sticks -= group
        row += 1

def stick_game():
    clear_screen()
    while True:
        try:
            sticks = int(input("\nHow many stick you want to play with: "))
            break
        except ValueError:
            print("\nPlease enter a number.")
    while True:
        try:
            max_num_stick = int(input("\nHow many stick you want to be removed when playing the game: "))
            break
        except ValueError:
            print("\nPlease enter a number.")
    while sticks <= 0:
        print("\nPlease insert a valid number of stick which is greater than 0 or positive number.\n")
        stick_game()
    clear_screen()
    print(f"\nThere are {sticks} sticks:")
    display_sticks(sticks)
    print(f"\nChoose the number of sticks you want to remove.\nYou can only move 1 - {max_num_stick} sticks\n")
    choice = input("Do you want to go first, say yes or no: ")
    while sticks != 0:
        if choice.lower()[0] == "y":
            human = int(input("How many sticks you want to remove: "))
            while 0 >= human or human > max_num_stick or human > sticks:
                print(f"\nPlease insert valid integer which is in the range of 1 - {max_num_stick}. "
                      "\nAnd also you can't take sticks that are not available.")
                human = int(input("How many sticks you want to remove: "))
            sticks -= human
            if sticks == 0:
                print("\n" + "|" + "-" * 40 + "|")
                print("|{:^39}|".format("🎉 CONGRATULATION YOU WIN 🎉"))
                print(f"|" + "-" * 40 + "|")
                print("|{:^40}|".format("Well played!!"))
                print("|" + "_" * 40 + "|")
                break
            clear_screen()
            print(f"\nThere are {sticks} sticks:")
            display_sticks(sticks)
            if sticks % (max_num_stick + 1) == 0:
                computer = random.randrange(1, (max_num_stick + 1))
            else:
                computer = sticks % (max_num_stick + 1)
            print(f"\nOk the computer choose {computer}")
            sticks -= computer
            if sticks == 0:
                print("\n" + "|" + "-" * 40 + "|")
                print("|{:^40}|".format("UNFORTUNATELY YOU LOST"))
                print("|" + "-" * 40 + "|")
                print("|{:^40}|".format("NEVER GIVE UP!!"))
                print("|" + "_" * 40 + "|")
                break
            print(f"\nThere are {sticks} sticks:")
            display_sticks(sticks)
        else:
            if sticks % (max_num_stick + 1) == 0:
                computer = random.randrange(1, (max_num_stick + 1))
            else:
                computer = sticks % (max_num_stick + 1)
            print(f"\nOk the computer choose {computer}")
            sticks -= computer
            if sticks == 0:
                print("\n" + "|" + "-" * 40 + "|")
                print("|{:^40}|".format("UNFORTUNATELY YOU LOST"))
                print("|" + "-" * 40 + "|")
                print("|{:^40}|".format("NEVER GIVE UP!!"))
                print("|" + "_" * 40 + "|")
                break
            clear_screen()
            print(f"\nThere are {sticks} sticks:")
            display_sticks(sticks)
            human = int(input("How many sticks you want to remove: "))
            while 0 >= human or human > max_num_stick or human > sticks:
                print(f"\nPlease insert valid integer which is in the range of 1 - {max_num_stick}. "
                      "\nAnd also you can't take sticks that are not available.")
                human = int(input("How many sticks you want to remove: "))
            sticks -= human
            if sticks == 0:
                print("\n" + "|" + "-" * 40 + "|")
                print("|{:^39}|".format("🎉 CONGRATULATION YOU WIN 🎉"))
                print("|" + "-" * 40 + "|")
                print("|{:^40}|".format("Well played!!"))
                print("|" + "_" * 40 + "|")
                break
            print(f"\nThere are {sticks} sticks:")
            display_sticks(sticks)
    main()

def stick_game_with_friend():
    clear_screen()
    while True:
        try:
            sticks = int(input("\nHow many stick you want to play with: "))
            break
        except ValueError:
            print("Please enter a number.")
    while True:
        try:
            max_num_stick = int(input("\nHow many stick you want to be removed when playing the game: "))
            break
        except ValueError:
            print("\nPlease enter a number.")
    while sticks <= 0:
        print("\nPlease insert a valid number of stick which is greater than 0 or positive number.")
        stick_game()
    clear_screen()
    print(f"\nThere are {sticks} sticks:")
    display_sticks(sticks)
    print(f"\nChoose the number of sticks you want to remove.\nYou can only move 1 - {max_num_stick} sticks")

    while sticks != 0:
        player1 = int(input("PLAYER1: How many sticks you want to remove: "))
        while 0 >= player1 or player1 > max_num_stick or player1 > sticks:
            print(f"\nPlease insert valid integer which is in the range of 1 - {max_num_stick}. "
                  "\nAnd also you can't take sticks that are not available.")
            player1 = int(input("PLAYER 1: How many sticks you want to remove: "))
        sticks -= player1
        if sticks == 0:
            print("\n" + "|" + "-" * 40 + "|")
            print("|{:^39}|".format("🎉 PLAYER 1 WINS 🎉"))
            print("|" + "-" * 40 + "|")
            print("|{:^40}|".format("Well played, Player 1!"))
            print("|" + "_" * 40 + "|")
            break
        clear_screen()
        display_sticks(sticks)
        player2 = int(input("PLAYER 2: How many sticks you want to remove: "))
        while 0 >= player2 or player2 > max_num_stick or player2 > sticks:
            print(f"\nPlease insert valid integer which is in the range of 1 - {max_num_stick}. "
                  "\nAnd also you can't take sticks that are not available.")
            player2 = int(input("\nPLAYER2: How many sticks you want to remove: "))
        sticks -= player2
        if sticks == 0:
            print("\n" + "|" + "-" * 40 + "|")
            print("|{:^39}|".format("🎉 PLAYER 2 WINS 🎉"))
            print("|" + "-" * 40 + "|")
            print("|{:^40}|".format("Well played, Player 2!"))
            print("|" + "_" * 40 + "|")
            break
        clear_screen()
        print(f"\nThere are {sticks} sticks:")
        display_sticks(sticks)
    main()

def main():
    clear_screen()
    print("=== STICK GAME ===")
    print("1. Play against Computer")
    print("2. Play against Friend")
    print("3. Game Rules")
    print("4. Exit")
    co = input("\nEnter your choice (1-4): ")
    if co == "1":
        stick_game()
    elif co == "2":
        stick_game_with_friend()
    elif co == "3":
        show_rules()
    elif co == "4":
        print("Goodbye! 👋")
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
        main()

main()
