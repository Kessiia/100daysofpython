import random

def roll_dice(num_dice, num_sides):
    # Simulate rolling each die and store the results in a list
    results = [random.randint(1, num_sides) for _ in range(num_dice)]
    return results

def main():
    print("Welcome to the Dice Rolling Simulator!")

    # Prompt user for input
    num_dice = int(input("Enter the number of dice to roll: "))
    num_sides = int(input("Enter the number of sides on each die: "))

    # Simulate rolling dice
    dice_results = roll_dice(num_dice, num_sides)

    # Display results
    print("Results:")
    for i, result in enumerate(dice_results, start=1):
        print(f"Die {i}: {result}")

if __name__ == "__main__":
    main()
