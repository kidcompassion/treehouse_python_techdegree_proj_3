from phrase import Phrase
import random

# Create your Game class logic in here.
class Game():

    def __init__(self):
        self.missed = 0
        self.phrases = [
            Phrase("All aboard"),
            Phrase("Swab the decks"),
            Phrase("Batten Down the Hatches"),
            Phrase("Ahoy Matey"),
            Phrase("Hello Sailor")
        ]
        self.active_phrase = self.get_random_phrase()
        self.guesses = 0
    
    def start(self):
        print(self.phrases)

    def get_random_phrase(self):
        random_index = random.randrange(0,4)
        self.active_phrase = self.phrases[random_index]
        return self.active_phrase
        
    def welcome(self):
        
        
        print("Welcome\n")
        print(self.active_phrase.display())
        self.get_guess()

    def get_guess(self):
        self.guesses = input("What letter would you like to guess?")
        self.active_phrase.check_letter(self.guesses)
        self.get_guess()

    def game_over():
        pass


game = Game()
game.welcome()