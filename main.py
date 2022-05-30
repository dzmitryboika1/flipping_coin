import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

def flip_coin():
    if random.randint(0, 1):
        heads_or_trails = 'Heads'
    else:
        heads_or_trails = 'Trails'
    return heads_or_trails


while True:
    user_choice = input("\nHeads or Trails? ").title()
    if user_choice != "Heads" and user_choice != "Trails":
        print("Incorrect input. Try again")
        continue
    computer_choice = flip_coin()
    if user_choice == computer_choice:
        print(f'Flipping the coin...{computer_choice}!\nYou are win!!!')
    else:
        print(f'Flipping the coin...{computer_choice}! You are lose!!!')
    again = input('\nWanna play again? y/n  ').lower()
    while again != 'y' and again != 'n':
        again = input('Incorrect input. Wanna play again? y/n  ').lower()
    if again == 'n':
        print("See you next time.")
        break
