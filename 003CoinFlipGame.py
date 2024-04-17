import random

options = ['head', 'tails']

flip = True

while flip:
    user_input = input("Flip? (y/n)\n").lower()

    if user_input == 'n':
        print('Okay BYE THEN!! :( ')
    elif user_input == 'y':
        answer = input("heads or tails? (head/tails)\nAnswer:").lower()
        result = random.choice(options)
        print("Result:", result)
        if answer == result:
            print("WINNER!\n")
        else:
            print("LOSER HAHA, better luck next time\n")
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
