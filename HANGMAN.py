import random


print('H A N G M A N')
menu_game = input('Type "play" to play the game, "exit" to quit: ')
print("")
while menu_game == "play":
    word_list = ['python', 'java', 'kotlin', 'javascript']
    word_game = random.choice(word_list)
    len_word = len(word_game)
    hidden_word = "-" * len_word
    guess_letter = set()
    game_letter = set()
    lives = 8
    while lives != 0:
        print(hidden_word)
        letter = input('Input a letter: ')
        if len(letter) == 1:
            if letter.isalpha() and letter.islower():
                if letter in game_letter:
                    print("You already typed this letter\n")
                    continue
                game_letter.add(letter)
                if letter in word_game and letter not in guess_letter:
                    guess_letter.add(letter)
                    hidden_word = ""
                    for j in word_game:
                        if j in guess_letter:
                            hidden_word += j
                        else:
                            hidden_word += "-"
                    if "-" not in hidden_word:
                        print(f"You guessed the word {hidden_word}!")
                        print("You survived!")
                        break
                    print("\n")
                else:
                    lives -= 1
                    print("No such letter in the word")
                    if lives == 0:
                        print("You are hanged!")
                        break
                    print("")
            else:
                print("It is not an ASCII lowercase letter\n")
        else:
            print("You should input a single letter\n")
    menu_game = input('Type "play" to play the game, "exit" to quit: ')
