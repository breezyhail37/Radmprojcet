import random
import nltk
nltk.download('words')
from nltk.corpus import words


words = ()

hangman_art = {
    0: ("", "", ""),
    1: ("o", "", ""),
    2: ("o", "|", ""),
    3: ("o", "/|", ""),
    4: ("o", "/|\\", ""),
    5: ("o", "/|\\", "/"),
    6: ("o", "/|\\", "/\\"),
}

def display_man(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print("The answer was:", answer)

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one letter.")
            continue

        if guess in guessed_letters:
            print("You have already guessed this letter.")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            print("Incorrect guess.")
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("Congratulations! You guessed the word.")
            is_running = False

        if wrong_guesses >= 6:
            display_man(wrong_guesses)
            display_answer(answer)
            print("Game over! Better luck next time.")
            is_running = False

if __name__ == "__main__":
    main()
