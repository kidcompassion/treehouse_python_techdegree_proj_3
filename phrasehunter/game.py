# Create your Game class logic in here.
import random
from .phrase import Phrase

#init 
# get phrase (Game)
# assign default booleans to phrase (phrase)
#get user input (game)
# check if it matches phrase (phrase)
#update phrase (phrase)
#retrigger the get user input (Game)



class Game:

    def __init__(self):
        self.missed = 0
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
        if len(user_guess) >1:
            print("This guess is not valid. Please guess one character at a time.")
        else:
            self.guesses.append(user_guess)
            #self.active_phrase.check_complete(0)
            self.active_phrase.display(user_guess)
            # Check the correct guess flag to see whether to increment the error counter
            if self.active_phrase.correct_guess != True:
                self.missed +=1
                print(self.missed)
            self.get_guess() #Keep asking for more guesses
            

        
            
        

        

    

    def game_over(self):
        pass

