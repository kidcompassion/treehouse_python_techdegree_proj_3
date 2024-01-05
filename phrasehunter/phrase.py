class Phrase:

    def __init__(self, phrase):
        self.phrase = phrase.upper()
        self.initial_phrase = self.initial_display()
        self.correct_guess = False
        self.already_guessed = False #This flag indicates the letter was already guessed

        # Put all characters contained in a string into a set
        self.phrase_set_of_characters = set(self.phrase) 
        # remove the spaces from the set
        self.phrase_set_of_characters.remove(" ")
    
    def initial_display(self):
        # The first time we load the app, set up all the booleans on letters
        # The visibility state starts as false on everything - when a guess is correct, make it "true"
        
        '''
        This list will hold a unique dictionary for each letter. 
        In each dictionary, the key is one letter, and the value is a T/F flag to indicate visibility.
        Everything starts as false, and we don't see anything.
        Once a letter is correctly guessed, flag gets set to true.
        '''

        displayed_phrase = []

        for letter in self.phrase:
            # Set all spaces to true, since we don't need to guess them
            if letter == " ":
                displayed_phrase.append({" ": True})
            else:
            # default everything to false
                displayed_phrase.append( { letter: False })
        return displayed_phrase
      

    def display(self, guesses):
        
        # This will hold the updated phrase once we filter for correct values
        flattened_phrase = ""            
        
        # This holds the post-guess phrase, showing the the underscores and guessed letters
        post_guess = self.check_letter(self.initial_phrase, guesses)
        
        # for each dictionary/letter in the list/phrase
        for x in post_guess:
            # Check if letter visibility is set to True
            if True in x.values():
                # If it is, add the letter into the flattened phrase for display
                for key in x:
                    flattened_phrase += key
            # If letter visibility is set to false, leave it as an underscore.
            else:
                flattened_phrase += "_"
        # print phrase for display
        print("\n" + flattened_phrase +"\n")
        
            
    def check_letter(self, phrase, guess):
        # Reset the correct guess flag to be False until it gets switched to true
        self.correct_guess = False
        self.already_guessed = False

        # look through phrase to see if guessed letter is there
        for x in phrase:
            # If the guess is there, set its visibility to true
            if guess in x :
                if x[guess] == False:
                    x[guess] = True
                    # Set correct guess flag to be true
                    self.correct_guess = True
                else:
                    self.already_guessed = True
        return phrase

    
    def check_complete(self, total_user_guesses):
        # Remove spaces from the original phrase and turn it into a set of letters
        original_phrase = set(self.phrase.replace(" ", ""))
        # turn the list of user guesses into a set
        guessed_letters = set(total_user_guesses)
        # remove any guessed letters from original set
        remaining_letters = original_phrase.difference(guessed_letters)
        # When no letters remain, phrase has been guessed
        if bool(remaining_letters) == False:
            return True