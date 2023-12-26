import random

# Define initial variables
game_title = "Word Raider"

# Set up the list of words to choose from
word_bank = []

# Open file for loading in the word bank
with open("words.txt") as word_file:
    word_bank = [line.rstrip().lower() for line in word_file]

# Select the word to guess
word_to_guess = random.choice(word_bank)

# Define the remaining game variables
misplaced_guesses = []
incorrect_guesses = []
max_turns = 5
turns_taken = 0

# Print the current game state
print("Welcome to", game_title)
print(f"The word has {len(word_to_guess)} letters.")
print(f"You have {max_turns - turns_taken} turns left.")

# Build the game loop
while turns_taken < max_turns:
    # Get the player's guess
    guess = input("Guess a word: ").lower()

    # Check if the guess length equals the word length and is all alpha letters
    if len(guess) != len(word_to_guess) or not guess.isalpha():
        print(f"Please enter {len(word_to_guess)}-letter word.")
        continue

    # Check each letter in the guess against the word's letters
    for c, target_char in zip(guess, word_to_guess):
        if c == target_char:
            print(c, end=" ")
            if c in misplaced_guesses:
                misplaced_guesses.remove(c)
        elif c in word_to_guess:
            if c not in misplaced_guesses:
                misplaced_guesses.append(c)
            print("_", end=" ")
        else:
            if c not in incorrect_guesses:
                incorrect_guesses.append(c)
            print("_", end=" ")

    print("\n")
    print("Misplaced letters:", misplaced_guesses)
    print("Incorrect letters:", incorrect_guesses)
    turns_taken += 1

    # Check if the player has won
    if guess == word_to_guess:
        print("Congratulations, you win!")
        break

    # Check if the player has lost
    if turns_taken == max_turns:
        print(f"Sorry, you lost. The word was {word_to_guess}")
        break

    # Display the number of turns left
    print(f"You have {max_turns - turns_taken} turns left.")
