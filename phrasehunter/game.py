# Create your Game class logic in here.
import random
import sys
from .phrase import Phrase

#init 
# get phrase (Game)
# assign default booleans to phrase (phrase)
#get user input (game)
# check if it matches phrase (phrase)
#update phrase (phrase)
#retrigger the get user input (Game)


#handle when someone repeats the same letter
# handle when smeone puts in a number
# handle if someone submits an empty string


class Game:

    def __init__(self):
        self.missed = 5
        self.phrases = ["Ahoy matey", "Up and away", "Swab the decks", "That ship has sailed", "Batten down the hatches"]
        # this generates the entire Phrase object and assigns it to Game property
        self.active_phrase = Phrase(self.get_random_phrase())
        self.guesses = []
        
    
    
    def start(self):
        self.welcome()
        

    def get_random_phrase(self):
        # Generate a random index to retrieve from the list of phrases
        randomizer = random.randrange(0, len(self.phrases))
        return self.phrases[randomizer]
        


    def welcome(self):
        welcome_msg = "==============================\n"
        welcome_msg += "  Welcome to Phrase Hunter\n"
        welcome_msg += "==============================\n"
        print(welcome_msg)
        # Set all booleans for initial load
        self.active_phrase.initial_display()
        self.get_guess()
        
        




    def get_guess(self):
        
        user_guess = input("Enter a letter to guess: ")
        if user_guess.isalpha() == False:
            print("This game accepts letters only. Please try again.")
            self.get_guess() #Keep asking for more guesses
        elif len(user_guess) > 1:
            print("This guess is not valid. Please guess one character at a time.")
            self.get_guess() #Keep asking for more guesses
        
        else:
            self.guesses.append(user_guess)
            total_guesses = self.guesses
           
            
            self.active_phrase.display(user_guess)
            # Check the correct guess flag to see whether to increment the error counter
            if self.active_phrase.check_complete(total_guesses) == True:
                print("You win! Great job!")
                self.game_over()
            if self.active_phrase.correct_guess != True:
                # if user has lives remaining
                if self.missed > 1:
                    self.missed = self.missed - 1
                    print(f"Sorry, incorrect guess! You have {self.missed} of 5 lives remaining.")
                # If user is out of lives
                else:
                    print("Sorry, you lose")
                    self.game_over()
            
            self.get_guess() #Keep asking for more guesses
            


    def error_handling(user_input):
        
        pass  

    def game_over(self):
        sys.exit()
