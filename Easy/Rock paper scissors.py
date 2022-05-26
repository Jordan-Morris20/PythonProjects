from random import random
import random

games = int(input('How many games do you want to play?'))
i=0
while i < games:
    computer = random.choice(['rock','paper','scissors'])
    pick = input('Choose rock, paper or scissors \n')
    if computer == pick:
        print('opponent chose',computer)
        print('Tie!')
    elif computer == 'rock' and pick == 'paper':
        print('opponent chose',computer)
        print('You win')
    elif computer == 'paper' and pick == 'scissors':
        print('opponent chose',computer)
        print('You win')
    elif computer == 'scissors' and pick == 'rock':
        print('opponent chose',computer)
        print('You win')        
    else:
        print('opponent chose',computer)
        print('You loose')
    i+=1