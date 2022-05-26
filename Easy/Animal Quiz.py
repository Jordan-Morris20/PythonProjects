def check(guess, answer):
    global counter
    if guess.lower() == answer.lower():
        counter += 1
        print("Correct")
    else:
        print("Wrong answer")
    
counter = 0    
guess1 = input("Which bear lives at the North Pole? ")
answer1 = "Polar Bear"
guess2 = input("Which is the fastest land animal? ")
answer2 = "Cheetah"
guess3 = input("Which is the larget animal? ")
answer3 = "Blue Whale"

check(guess1, answer1)
check(guess2, answer2)
check(guess3, answer3)
print("Your score was ", counter, " out of 3")