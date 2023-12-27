# Create your Phrase class logic here.



class Phrase:

    def __init__(self, phrase):
        self.phrase = phrase.lower()
        self.initial_phrase = self.initial_display()

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
        for x in phrase:
            if guess in x:
                x[guess] = True
        return phrase


    
    def check_complete(self):
        print("check complete")
    
