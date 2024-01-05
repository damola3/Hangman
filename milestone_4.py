import random

class Hangman:
    '''
    Introduces the game Hangman as an entire class with its own methods
        Attributes:
            word_list (list): List of words to be tested in-game
            word (str): A random choice of word from word_list
            num_lives (int): Number of lives per game
            word_guessed (list): List of letters of the word, with '_' for each letter not guessed
            num_letters (int): #Number of unique letters not yet guessed
            list_of_guesses (list): #list of guesses already tried
            '''
    def __init__(self, word_list = list, num_lives = 5 or int):
        self.word = random.choice(word_list)
        self.word_list = word_list 
        self.num_lives = num_lives 
        self.word_guessed = self.init_word(self.word)
        self.num_letters = len(self.word) 
        self.list_of_guesses = []

    def check_guess(self, guess):
        '''This checks to see if the guess is correct and changes game variables accordingly.
        
        Args:
            guess (str): Single letter guess
        '''
        lguess = guess.lower()
        if lguess in self.word.lower():
            for letter in self.word.lower():
                if lguess == letter.lower():
                    self.word_guessed[self.word.index(letter)] = letter
                    print("Good guess! {} is in the word.".format(lguess))
            self.num_letters -=1
        else:
            self.num_lives -= 1
            print("Sorry, {} is not in the word.".format(lguess))
            print("You have {} lives left.".format(self.num_lives))
    
    def ask_for_input(self):
        '''This asks the user for their input, validates it and then passes the input through the game.
        Input:
            Letter guess
        '''        
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
    @staticmethod
    def init_word(word):
        '''This sets the 'word_guessed' variable to a list compromising of each letter per entry.
        
        Args:
            word (str): Word to be guessed

        Returns:
            word (list):
        '''        
        guessed = []
        for i in word:
            guessed.append('_')
        return guessed

word_list = ['plums', 'apples', 'mangoes', 'grapes', 'lemons'] 
game=Hangman(word_list)
game.ask_for_input()