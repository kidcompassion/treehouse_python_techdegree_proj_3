# Create your Phrase class logic here.



class Phrase:

    def __init__(self, phrase):
        self.phrase = phrase.lower()
        self.initial_phrase = self.initial_display()
        self.correct_guess = None

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
        winner = False
        self.correct_guess = False
        for x in phrase:
            # If the guess is in the word, set its value to true    
            if guess in x:
                x[guess] = True
                self.correct_guess = True
        print(self.correct_guess)                    
        return phrase
    
        #if all values are set to true (or none are false), the person wins


    
    def check_complete(self, fail):
        print(fail)
    
