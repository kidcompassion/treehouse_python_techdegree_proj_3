# Create your Phrase class logic here.
class Phrase():
    def __init__(self, phrase):
        self.phrase = phrase.lower()
        self.hidden_phrase = []
        
    def display(self):
        # Hidden phrase will hold the hidden phrase (____ ____), and update with each guess
        self.hidden_phrase = []
        # Generate the hidden version of the phrase, and render spaces appropriately
        for x in self.phrase:
            if x != " ":
                self.hidden_phrase.append("_")
            else:
                self.hidden_phrase.append(" ")
        
        return "".join(self.hidden_phrase)
       
    
    def check_letter(self, user_guess):
        # If user guess is correct...
        if user_guess in self.phrase: 

            # If guess is in string, get every instance of its index
            # https://stackoverflow.com/questions/176918/how-to-find-the-index-for-a-given-item-in-a-list
            
            # ... find the index for any appearance of the guess
            indexes = [i for i, letter in enumerate(self.phrase) if letter == user_guess]
            # ...for each index, show the actual letter
            for index in indexes:
                self.hidden_phrase[index] = user_guess
            # Flatten the hidden phrase into a string and print it
            print("".join(self.hidden_phrase))
            # Check whether the word is totally revealed
            self.check_complete()
            # Return True so the Game class knows it was a valid guess
            return True
        else:
            # Bubble up the error so Game can track missed guesses
            return False       

    def check_complete(self):
        # If original phrase and hidden phrase match, then puzzle is complete.
        if self.phrase == "".join(self.hidden_phrase):
            return True


