import random

def hangman():
    words = ['devesh', 'yash', 'ankit', 'anu', 'sunshine']
    chosen_word = random.choice(words)
    guessed_letters = []
    attempts = 6

    while True:
        print("\n")
        display_word = ""
        for letter in chosen_word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_ "

        print(display_word)

        if display_word == chosen_word:
            print("Congratulations! You guessed the word:", chosen_word)
            break

        if attempts == 0:
            print("You ran out of attempts! The word was:", chosen_word)
            break

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again!")
            continue

        guessed_letters.append(guess)

        if guess not in chosen_word:
            attempts -= 1
            print("Wrong guess! Attempts remaining:", attempts)

hangman()