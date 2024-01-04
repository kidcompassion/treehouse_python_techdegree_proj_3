# Create your Phrase class logic here.



class Phrase:

    def __init__(self, phrase):
        self.phrase = phrase.lower()
        self.initial_phrase = self.initial_display()
        self.correct_guess = False
        #Put all characters contained in a string into a set
        self.phrase_set_of_characters = set(self.phrase) 
        # remove the spaces from the set
        self.phrase_set_of_characters.remove(" ")
        
        #print(self.phrase_set_of_characters)

    def initial_display(self):
        # The first time we load the app, set up all the booleans on letters
        displayed_phrase = []
        for letter in self.phrase:
            if letter == " ":
                displayed_phrase.append({" ": True})
                
            else:
                displayed_phrase.append( { letter: False })
        return displayed_phrase
      

    def display(self, guesses):
        
        # This will hold the phrase once we filter for correct values
        flattened_phrase = ""            
        post_guess = self.check_letter(self.initial_phrase, guesses)
        
        # for each dictionary in the list
        for x in post_guess:
            #Check if it's existence is set to True
            if True in x.values():
                # If it is, add the letter into the flattened phrase
                for key in x:
                    flattened_phrase += key
            # If it's set to false, leave it as an underscore.
            else:
                flattened_phrase += "_"

        print(flattened_phrase)
        
            

       

    def check_letter(self, phrase, guess):
        # Reset the correct guess flag to be False until it gets switched to true
        self.correct_guess = False
        
        for x in phrase:
            # If the guess is in the word, set its value to true    
            if guess in x:
                x[guess] = True
                self.correct_guess = True

        return phrase
        #if all values are set to true (or none are false), the person wins


    
    def check_complete(self, total_user_guesses):
        # Remove spaces from the original phrase and turn it into a set of letters
        original_phrase = set(self.phrase.replace(" ", ""))
        # turn the list of user guesses into a set
        guessed_letters =set(total_user_guesses)
        # remove any guessed letters from original set
        remaining_letters = original_phrase.difference(guessed_letters)
        # When no letters remain, phrase has been guessed
        if bool(remaining_letters) == False:
            return True


       # get all guessed
       
       # chosen_characters = []
       #
       # for x in word:
       #     for y,z in x.items():
       #         chosen_characters.append(z)
       # 
       # if False not in chosen_characters:
       #     return True