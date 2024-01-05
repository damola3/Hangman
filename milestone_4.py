import random

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word = random.choice(word_list)
        self.word_list = word_list #List of words to be tested in-game
        self.num_lives = num_lives #Number of lives per game
        self.word_guessed = [] #List of letters of the word, with '_' for each letter not guessed
        for i in self.word:
            self.word_guessed.append(i)
        self.num_letters = len(self.word) #Number of unique letters not yet guessed
        self.list_of_guesses = [] #list of guesses already tried

    def check_guess(self, guess):
        lguess = guess.lower()
        if lguess in self.word:
            for letter in self.word:
                if lguess == letter.lower():
                    self.word_guessed[self.word.index(letter)] = letter
                    print("Good guess! {} is in the word.".format(lguess))
            self.num_letters -=1
        else:
            self.num_lives -= 1
            print("Sorry, {} is not in the word.".format(lguess))
            print("You have {} lives left.".format(self.num_lives))
    
    def ask_for_input(self):
        while True:
            guess = input("Please guess a single letter ") #This asks the user to guess a letter for the game.
            if guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
                guess = input("Please guess a single letter ")

            elif guess in self.list_of_guesses:
                print("You've already tried that letter!")
            
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

word_list = ['plums', 'apples', 'mangoes', 'grapes', 'lemons'] 
game=Hangman(word_list)
game.ask_for_input()