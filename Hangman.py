import random
import time

#* Initial pleasentries
print('Welcome to hangman')
name = input('Enter your name')
time.sleep(2)

#  Define the global variables for the other functions
def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["january","border","image","film","promise","kids","lungs","doll","rhyme","damage","plants"]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_'*length
    already_guessed = []
    play_game = ""
    
def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input('This is the word '+ display + ' Enter your guess')
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip())>=2:
        print('Invalid guess')
        hangman()