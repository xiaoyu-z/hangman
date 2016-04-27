"""Player classes for hangman game."""

from wordset import WordMunch
from utils import *
import random

class Player:
    """Player base class.  Defines initializer and interface.

    >>> from wordset import Dictionary
    >>> p = Player(Dictionary('assets/lincoln.txt'))
    >>> Player.all_words[2]
    'add'
    """
    all_words = None
    def __init__(self, dictionary):
        """Inialize class with a dictionary."""
        # BEGIN
        Player.all_words = dictionary.words()
        #print(self.all_words)
        "*** REPLACE THIS LINE ***"
        # END
    
    def guess(self, board):
        """Return a character a a guess."""
        return None

    def pick_word(self):
        """Return a word that is to be guessed."""
        return None

class DummyPlayer(Player):
    """Simple deterministic player for testing."""
    
    def __init__(self, name):
        self.name = name
        self.calls = -1

    def guess(self, board):
        """Return a character a a guess."""
        self.calls += 1
        return "cfeors"[self.calls]

    def pick_word(self):
        """Return a word that is to be guessed."""
        return 'score'    


class HumanPlayer(Player):
    """HumanPlayer is initialized with a name and implements the player interface 
    such that:
    - guess requests a guess from a person, via the input device
    - pick_word requests a secret word and verifies that it is in the dictionary
    
    """
    def __init__(self, name):
        self.name = name

    def guess(self, board):
        """Guess a character."""

        print(self.name, ", please enter your next guess.")
        guess = input()
        while (len(guess) != 1) or (guess in board.guesses()):
            print('Please enter a single character not yet guessed')
            guess = input()
        return guess

    def pick_word(self):
        """Return a secret word from the dictionary."""

        print(self.name,", pick your secret word.")
        word = input()
        while not word in Player.all_words:
            print(word, " is not in the dictionary. Another:")
            word = input()
        return word

class ComputerPlayer(Player):
    """Perform as a player - picking a word or guessing a character
    
    >>> from wordset import WordSet    # Basic test including total character frequency
    >>> from board import Board
    >>> p = Player(WordSet(['one','two','three']))   # Player superclass with the dictionary
    >>> c = ComputerPlayer()
    >>> b = Board('three')
    >>> c.guess(b)
    'e'
    """
    def __init__(self, name='Computer'):
        # BEGIN
        #Player.__init__(self)
        self.name = name
        self.index = 0
        self.wordmunch = WordMunch(Player.all_words)
        "*** REPLACE THIS LINE ***"
        # END

    def guess(self, board, verbose=False):
        """Guess a character to play based on the current board.
        verbose option allows useful and fun displays.
        """
        # BEGIN
        Board = board
        def filter_f(word):
            if len(word) == len(Board):
                flag = True
                for i in board.hits():
                    if i not in word:
                        flag = False
                        break
                return flag
            
            return False
                
        self.wordmunch.filter(filter_f)
        frequency = self.wordmunch.frequency()
        frequency = sorted(frequency.items(), key = lambda word:word[1],reverse = True)
        #print(frequency)
        if verbose:
            print('verbose is True')
        #print(frequency)
        self.index = 0
        #print(frequency)
        while frequency[self.index][0] in board.guesses():
            self.index += 1
            try: frequency[self.index][0]
            except: return
        
        #board.guess(alpha_list[self.index])
        return frequency[self.index][0]
        
        "*** REPLACE THIS LINE ***"
        # END

    def pick_word(self):
        """Pick a random word from the dictionary."""
        # BEGIN
        return random.sample(Player.all_words, 1)[0]
        "*** REPLACE THIS LINE ***"
        # END
