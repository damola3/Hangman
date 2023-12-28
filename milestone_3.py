import random

word_list = ['plums', 'apples', 'mangoes', 'grapes', 'lemons'] #list of words for individual gamesh

word = random.choice(word_list) #This randomises choice of word for instance of gamebhg
guess = input("Please guess a single letter ") #This asks the user to guess a letter for the game.
guess

def check_guess():
    global guess
    lguess = guess.lower()
    while lguess not in word:    
        print("Sorry, {} is not in the word. Try again.".format(lguess))
        guess = input("Please guess a single letter ")
        lguess = guess.lower()
    else:
        print("Good guess! {} is in the word.".format(lguess))

def ask_for_input():
    global guess
    while guess.isalpha() == True:
        break
    else:
        while guess.isalpha() == False:
            print("Invalid letter. Please, enter a single alphabetical character.")
            guess = input("Please guess a single letter ")

ask_for_input()
check_guess()