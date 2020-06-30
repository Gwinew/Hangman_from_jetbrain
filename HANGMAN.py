import random


print('H A N G M A N\n')
word_list = ['python', 'java', 'kotlin', 'javascript']
word_game = random.choice(word_list)
len_word = len(word_game)
hidden_word = "-" * len_word
guess_letter = set()
lives = 8
while lives != 0:
    print(hidden_word)
    letter = input('Input a letter: ')
    if letter in word_game and letter not in guess_letter:
        guess_letter.add(letter)
        hidden_word = ""
        for j in word_game:
            if j in guess_letter:
                hidden_word += j
            else:
                hidden_word += "-"
        print("\n")
        if "-" not in hidden_word:
            print(f'{hidden_word}\nYou guessed the word!\nYou survived!')
            break
    else:
        lives -= 1
        if letter in guess_letter:
            print("No improvements\n")
        else:
            print("No such letter in the word\n")
        if lives == 0:
            print("You are hanged!")
            break
