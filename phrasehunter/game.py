import random
import sys
from .phrase import Phrase

class Game:

    def __init__(self):
        self.missed = 5
        self.phrases = ["Ahoy matey", "Up and away", "Swab the decks", "That ship has sailed", "Batten down the hatches"]
        # this generates the entire Phrase object and assigns it to Game property
        self.active_phrase = Phrase(self.get_random_phrase())
        self.guesses = []
        self.new_game = True
        self.start()
    
    
    def start(self):
        self.welcome()
        

    def get_random_phrase(self):
        # Generate a random index to retrieve from the list of phrases
        randomizer = random.randrange(0, len(self.phrases))
        return self.phrases[randomizer]
        

    def welcome(self):
        welcome_msg =  "\n"
        welcome_msg += "==============================\n"
        welcome_msg += "  Welcome to Phrase Hunter\n"
        welcome_msg += "==============================\n"
        print(welcome_msg)
        # Set all booleans for initial load
        self.active_phrase.initial_display()
        self.get_guess()
        

    def get_guess(self):
        user_guess = input("Enter a letter to guess: ").upper()
        # Error handling

        # Is the input a letter? If not, give an error
        if user_guess.isalpha() == False:
            print("\nThis game accepts letters only. Please try again.\n ")
            self.get_guess() # Keep asking for more guesses
        # Is the input longer than 1 character? If so, give an error
        elif len(user_guess) > 1:
            print("\nThis guess is not valid. Please guess one character at a time. \n")
            self.get_guess() # Keep asking for more guesses
        else:
            # If the input is valid, add it to the list of guessed characters
            self.guesses.append(user_guess)
            #total_guesses = self.guesses
            self.active_phrase.display(user_guess)
           
           
            if self.active_phrase.check_complete(self.guesses) == True:
                print("\nYou win! Great job! \n")
                self.play_again()
            # Check whether guess is wrong, but hasn't already been guessed
            if (self.active_phrase.correct_guess != True) and (self.active_phrase.already_guessed == False):
                # if user has lives remaining
                if self.missed > 1:
                    self.missed = self.missed - 1
                    print(f"\nSorry, incorrect guess! You have {self.missed} of 5 lives remaining.\n")
                # If user is out of lives
                else:
                    print("\nSorry, you lose\n")
                    self.play_again()
            # Check whether guess is wrong, but HAS already been guessed (this shouldn't cost them a life)
            if (self.active_phrase.correct_guess != True) and (self.active_phrase.already_guessed == True):
                print("\nUh oh, you already guessed that - try again! \n")        
            
            self.get_guess() #Keep asking for more guesses
            

    def play_again(self):
        restart = input("Would you like to play again? (Y/N) ").lower()
        if restart == "y":
            # Instantiate a new game
            self.__init__()
        elif restart == "n":
            # Leave game
            self.game_over()
        else:
            # If entry is not valid, run the question again
            print("/n That entry is invalid /n")
            self.play_again()


    def game_over(self):
        print("/n Thanks for playing! /n")
        sys.exit()
