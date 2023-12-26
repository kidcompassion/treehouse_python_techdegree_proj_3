# Import your Game class


from phrasehunter.Game import Game
from phrasehunter.Phrase import Phrase




# Create your Dunder Main statement.
if __name__=="__main__":
    game = Game()
    phrase = Phrase(game.get_random_phrase())