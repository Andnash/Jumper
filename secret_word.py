import random
#from director import Director

class Secret_word:
    """ Secret_word is the class that holds the available words to be guessed, has the functions to pick one of those words, and show the letters of 
    that word as underscores if applicable."""
     
    def __init__(self):
        self._wordbank = ['aardvark', 'buttress', 'clandestine', 'discard', 'entertainment', 'censored', 'galvanize', 'hypothetical', 'iteration', 
        'jovial', 'kindergarten', 'lavish', 'miscellaneous', 'namesake', 'opulent', 'plausible', 'quintessential', 'ramification', 'sword', 'triangle', 
        'usurp', 'validate', 'whistle', 'xanthic', 'yesterday', 'zestful']
       
        self._chosen_word = ''


    def _word_picker(self):
        self._chosen_word = random.choice[self._wordbank]
        print(self._chosen_word)



    
