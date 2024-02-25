from .phrase import Phrase
import random
import sys

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
        self.active_phrase = "Default"
        self.guesses = []
    
    def start(self):
        self.welcome()

    def get_random_phrase(self):
        random_index = random.randrange(0,5)
        self.active_phrase = self.phrases[random_index]
        return self.active_phrase
        
    def welcome(self):
        self.active_phrase = self.get_random_phrase()
        self.missed = 0
        print("\n/******* Welcome to Phrasehunter! ************/\n")
        print("\n Here's your phrase to guess: \n")
        print(self.active_phrase.display())
        print("\n")
        self.get_guess()

    def get_guess(self):
        # Flag to indicate whether user inputs incorrect content (int, multi-character, etc).
        input_error = False

        # Check if the last guessed solve the puzzle
        if self.active_phrase.check_complete() == True:
            print("You won, great job!")
            self.game_over()

        # Ask for user guess 
        user_guess = input("What letter would you like to guess? ")

        if user_guess in self.guesses:
            print("\n/** Error: You guessed this already! **/\n")
            self.get_guess()


        # INPUT ERROR HANDLING
        # If user enters more than one letter
        if len(user_guess) > 1:
            print("\n/** Error: One character only, please! **/\n")
            input_error = True
        
        # If user enters a number
        if user_guess.isdigit() == True:
            print("\n/** Error: Enter letters only, please! **/\n")  
            input_error = True
        
        # If user enters nothing
        if user_guess == "":
            print("\n /** Enter a guess, please! **/ \n")
            input_error = True

        # If user enters an empty space
        if user_guess == " ":
            print("\n /** Enter letters only, please! **/ \n")
            input_error = True
    
        # If guess is wrong AND there is no input error, increment error cunter
        if self.active_phrase.check_letter(user_guess) == False and input_error == False:
            self.guesses.append(user_guess)
            self.missed += 1
            print("\nWhoops, you have " + str(self.missed) + " incorrect guesses.\n")
        else:
            # If guess is correct, just add guessed letter to list
            self.guesses.append(user_guess)
        
        # If user gets 5 wrong, they lose
        if self.missed >= 5:
            print("\nSorry, that's 5 errors. You lose.\n")
            self.game_over()
        # otherwise, keep playing
        else:
            self.get_guess()

    def game_over(self):
        # Ask user if they want to play again
        play_again = input("Would you like to play again? Y/N ").lower()
        # If they do, restart the game
        if play_again == "y":
            self.start()
        # IF not, quit the game
        elif play_again == "n":
            print("\nOkay, thanks for playing, see you next time!\n")
            sys.exit()
        else:
            print("Sorry, I don't understand that.")