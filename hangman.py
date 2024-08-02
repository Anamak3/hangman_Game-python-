import random

import hangman_word_ist

chosen_world=random.choice(hangman_word_ist.word_list)
lives=6
from hangman_ascii import stages,logo
print(logo)



display=[]
word_length=len(chosen_world)
for _ in range(word_length):
    display +="_"
print(display)
end_game=False

while not end_game:
    guess=input("Guess a letter \n").lower()
    if guess in display:
        print(f"you alraedy gussed this letter {guess}")

    for position in range(word_length):
        letter=chosen_world[position]

        if letter==guess:
            display[position]=letter
    if guess not in chosen_world:
        print(f"you gussed {guess},that's mot in the word. you lose a life.")
        lives -= 1
        if lives==0:
            end_game=True
            print("you lose the game")
    print(f"{''.join(display)}")
    if "_" not in display:
        end_game=True
        print("congrats you win")
    #from hangmanascii import stages
    print(stages[lives])