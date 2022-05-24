import random
import time

#* Initial pleasentries
print('Welcome to hangman')
name = input('Enter your name \n')
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
    
 #  Main game function    
def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input('This is the word '+ display + ' Enter your guess \n')
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip())>=2:
        print('Invalid guess')
        time.sleep(2)
        hangman()
    elif guess in word:
        already_guessed.extend(guess)
        index = word.find(guess)
        word = word[:index] + '_' + word[index +1:]
        display = display[:index] + guess + display[index+1:]
        print(display + '\n')
    elif guess in already_guessed:
        print('Try another letter \n')
    else:
        count+=1
        if count == 1:
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print('Wrong guess, ',str(limit-count),' guesses remaining.')
        elif count == 2:
            print("   _____ \n"
                  "  |     |\n"
                  "  |     O\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print('Wrong guess, ',str(limit-count),' guesses remaining.')
        elif count == 3:
            print("   _____ \n"
                  "  |     |\n"
                  "  |     O\n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print('Wrong guess, ',str(limit-count),' guesses remaining.')
        elif count == 4:
            print("   _____ \n"
                  "  |     |\n"
                  "  |     O\n"
                  "  |    /|\ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print('Wrong guess, ',str(limit-count),' guesses remaining.')
        elif count == 5:
            print("   _____ \n"
                  "  |     |\n"
                  "  |     O\n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print('Game over, you have been hanged!')
            print('The word was ', already_guessed, word)
    
    if word == '_':
        print('Yay! You have guessed the word. Well done, ' ,name,'!')
        exit()
    elif count != limit:
        hangman()
        
main()

hangman()