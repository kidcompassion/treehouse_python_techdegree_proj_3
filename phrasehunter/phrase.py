# Create your Phrase class logic here.



class Phrase:

    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def display(self, guesses):
        # Create a dictionary so we can assign an index to each letter
        displayed_phrase = {}
        counter_phrase = 0
        ## Do this with true and false instead of indexes
        # if tru, show letter, if false, show underscore
        for letter in self.phrase:
            if letter == " ":
                displayed_phrase[counter_phrase] = { " ": True}
                counter_phrase += 1
            else:
                displayed_phrase[counter_phrase] = { letter: False }
                counter_phrase += 1

         #check letter should go here
                        
        return displayed_phrase


    def check_letter(self):
        # loop through each list and if the letter matches, switch it to True
        #set letter visibility to true
        #phrase_dict = self.display(0)
        print(self)
        # if guess exists in phrase
        #



    def check_complete():
        pass
    
