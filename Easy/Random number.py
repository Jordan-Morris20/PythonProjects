import random

print('Enter upper bound')
upper_bound=input()
upper_bound=int(upper_bound)
secret = random.randint(0,upper_bound)
i=0
n=5

while i < n:
    print('Enter your guess')
    guess = input()
    guess=int(guess) 
    if secret == guess:
        print('Yay, correct!')
        break
    else:
        print('Your guess was off by',abs(secret-guess))