# Create your Phrase class logic here.
class Phrase():
    def __init__(self, phrase):
        self.phrase = phrase.lower()
        self.hidden_phrase = []
        #self.display()


    def display(self):
        for x in self.phrase:
            if x != " ":
                self.hidden_phrase.append("_")
            else:
                self.hidden_phrase.append(" ")

        return self.hidden_phrase
       
     # pass user guess
    def check_letter(self, user_guess):
        #self.display()
        wrong_guess = False
        if user_guess in self.phrase:  
            # get its index
            # https://stackoverflow.com/questions/176918/how-to-find-the-index-for-a-given-item-in-a-list
            indexes = [i for i, letter in enumerate(self.phrase) if letter == user_guess]
            for index in indexes:
                self.hidden_phrase[index] = user_guess
            print(self.hidden_phrase)
            self.check_complete()
            return True
        else:
            # Bubble up the error so Game can track missed guesses
            return False
            
            
            # increment wrong guess
            

            

            

    def check_complete(self):
        print(self.phrase)
        if self.phrase == "".join(self.hidden_phrase):
            print("complete")


