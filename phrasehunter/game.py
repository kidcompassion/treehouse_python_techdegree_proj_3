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
        input_error = False

        if self.active_phrase.check_complete() == True:
            print("You won, great job!")
            self.game_over()
             
        user_guess = input("What letter would you like to guess? ")

        if len(user_guess) > 1:
            print("\n/** Error: One character only, please! **/\n")
            input_error = True
            #user_guess

        if user_guess.isdigit() == True:
            print("\n/** Error: Enter letters only, please! **/\n")  
            input_error = True
            #user_guess 
        
        if user_guess == "":
            print("\n /** Enter a guess, please! **/ \n")
            input_error = True
            #user_guess

        if user_guess == " ":
            print("\n /** Enter letters only, please! **/ \n")
            input_error = True
            #user_guess     
    

        if self.active_phrase.check_letter(user_guess) == False and input_error == False:
            self.guesses.append(user_guess)
            self.missed += 1
            print("\nWhoops, you have " + str(self.missed) + " incorrect guesses.\n")
        else:
            self.guesses.append(user_guess)
        
        if self.missed >= 5:
            print("\nSorry, that's 5 errors. You lose.\n")
            self.game_over()
        else:
            self.get_guess()

        

    def game_over(self):
        #print("game_over")
        play_again = input("Would you like to play again? Y/N ").lower()
        if play_again == "y":
            self.start()
        elif play_again == "n":
            print("\nOkay, thanks for playing, see you next time!\n")
            sys.exit()
        else:
            print("Sorry, I don't understand that.")
            


