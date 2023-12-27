# Create your Game class logic in here.
import random
from .phrase import Phrase

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
        self.get_guess()
        
        


    def get_guess(self):
        #print(self.phrase_obj)
        user_guess = input("Enter a letter to guess: ")
        if len(user_guess) >1:
            print("This guess is not valid. Please guess one character at a time.")
        else:
            print(self.active_phrase.display(0))

    

    def game_over(self):
        pass

