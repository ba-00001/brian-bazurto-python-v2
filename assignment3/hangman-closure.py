# Task 4: Closure Practice

def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        # guesses lives in the enclosing scope, so it remembers every call
        guesses.append(letter)
        shown = "".join(ch if ch in guesses else "_" for ch in secret_word)
        print(shown)
        return "_" not in shown

    return hangman_closure


if __name__ == "__main__":
    secret_word = input("Enter the secret word: ").strip().lower()
    while not secret_word.isalpha():
        secret_word = input("Please use letters only. Enter the secret word: ").strip().lower()

    # push the secret word off the screen so the other player can't see it
    print("\n" * 50)

    game = make_hangman(secret_word)
    tries = 0
    done = False
    while not done:
        guess = input("Guess a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        tries += 1
        done = game(guess)

    print(f"You got it! The word was {secret_word}. It took {tries} guesses.")
