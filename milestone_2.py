import random

word_list = ['plums', 'apples', 'mangoes', 'grapes', 'lemons'] #list of words for individual games
print(word_list)

word = random.choice(word_list) #This randomises choice of word for instance of game
print(word)

guess = input("Please guess a single letter ") #This asks the user to guess a letter for the game.
guess

while len(guess) != 1:
    print("Oops! That is not a valid input")
    guess = input("Please guess a single letter ") 
else:
    print("Good guess!")
    
'''We want to validate that a correct input is inserted.'''