# Create your Game class logic in here.
import random



class Game:




    def __init__(self):
        self.missed = 0
        self.phrases = ["Ahoy matey", "Up and away", "Swab the decks", "The ship has sailed", "The train has left the station"]
        self.active_phrase = None
        self.guesses = []


    def start():
        pass

    def get_random_phrase(self):
        # Generate a random index to retrieve from the list of phrases
        randomizer = random.randrange(0, len(self.phrases))
        return self.phrases[randomizer]


    def welcome():
        pass


    def get_guess():
        pass


    def game_over():
        pass

