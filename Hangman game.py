import random

words = ["apple", "tiger", "house", "plant", "water"]

word = random.choice(words)
guessed_letters = []
wrong_guesses = 0

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")
print("You have 6 wrong guesses.")

while wrong_guesses < 6:

    for letter in word:
        if letter in guessed_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")

    print()

    if all(letter in guessed_letters for letter in word):
        print("Congratulations! You guessed the word!")
        break

    guess = input("Enter a letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
    elif guess in guessed_letters:
        print("You already guessed that letter.")
    else:
        guessed_letters.append(guess)

        if guess in word:
            print("Correct guess!")
        else:
            wrong_guesses += 1
            print("Wrong guess!")
            print("Wrong guesses:", wrong_guesses, "/ 6")

if wrong_guesses == 6:
    print("\nGame over!")
    print("The correct word was:", word)
    print("Thanks for playing!")

