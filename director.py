from game.terminal_service import TerminalService
from game.secret_word import Secret_word
from game.jumper import Jumper


class Director:
    
    def __init__(self):
        self.jumper = Jumper()
        self._is_playing = True
        self._terminal_service = TerminalService()
        self.mistake_lvl = 0

    def start_game(self):
        #Starts the game by running the main game loop.
        
        while self._is_playing != False:
            Secret_word()
            TerminalService()
            self._get_inputs()
            self._do_outputs()
            Jumper()
            

    def _get_inputs(self):

        self.letter_guess = self._terminal_service.read_text('Guess a letter [a-z]: ')
        # letter_guess is the player choosing a letter as their guess
        
        print(self.letter_guess)
        return self.letter_guess
    

    def check_guessed_letter(self):


        """ the check_guessed_letter function is supposedsto take in the guessed letter, check within the secret word for matching letters based on their position,
        and if it finds one that matches, to replace the _ with the guessed/correct letter.
        
        It should be looking for the 'i' in question and beginning from the zeroth position, check forward up to the length of the _chosen_word).

        If there is not a letter that matches the guess, it should add one to the mistake_lvl, which should alter what version of the jumper image is printed out.
        """


        unguessed = ['_'] * len(self.chosen_word)
        # unguessed is the _ spaces that the player still needs to guess to uncover the secret word. 

        for i in range(0,len(self._chosen_word)):
            check = self._chosen_word[i]
            if self.letter_guess == check:
                # letter_guess is the player choosing a letter as their guess

                unguessed[i] = self.letter_guess
                print(unguessed)

                return unguessed
                
                
        else:
            self.mistake_lvl += 0

    def _do_outputs(self):
        while Secret_word == ['_']:
            print(Secret_word)

        else: 
            self._is_playing = False
