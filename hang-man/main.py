# regex lib
import re

lives = 10

print("Welcome to HangMan")

word_to_guess = input("Enter word to guess: ")
print(word_to_guess)

displayed_word = list(re.sub(r"\w", "_", word_to_guess))

print("".join(displayed_word))


while "_" in displayed_word:
    guessed_char = input("Enter character to guess: ")

    if len(guessed_char) != 1:
        print("Only one character at a time!")
        continue

    if guessed_char not in word_to_guess:
        lives -= 1
        print(f"Wrong character! Lives left: {lives}")
        if lives == 0:
            print("You lost! The word was", word_to_guess)
            break
        continue

    pos_to_search = 0
    positions = []
    while True:
        pos_to_search = word_to_guess.find(guessed_char, pos_to_search)

        if pos_to_search == -1:
            break

        positions.append(pos_to_search)

        pos_to_search += 1

    # print(positions)

    for pos in positions:
        displayed_word[pos] = guessed_char

    print("".join(displayed_word))

if lives > 0:
    print("You guessed the word!")
