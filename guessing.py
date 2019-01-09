import random
number=random.randint(1,100)
guesses = [0]
print("I've picked a random number from 1 to 100. Guess the number!")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
while True:
    print("I've picked a random number from 1 to 100. Guess the number!")
    
    guess=int(input("Your guess? "))
    if guess > 100 or guess < 1:
        print("OUT OF BONDS!")
        continue
    
    if guess==number:
        print(f"YOU WON! NUMBER OF GUESSES {len(guesses)}") #len() counts our placeholder, so we count the number of
        break                                               # guesses before appending new one
        
    guesses.append(guess)    
     # when testing the first guess, guesses[-2]==0, which evaluates to False
    # and brings us down to the second section
    if guesses[-2]:
        if abs(number-guess)<abs(number-guesses[-2]):
            print("WARMER!")
        else:
            print("COLDER!")
    else:
        if abs(number-guess)>10:
            print("COLD!")
        else:
            print("WARM!")