from secret import SecretWord
from board import Board

class Game:
    """Run an entire game. 

    Initialization defines the player who pickers secret word and one or more guessers.
    play
       - picker picks the secret word from the dictionary held by all players
       - guessers guess in turn looking at the state of the board until the game is done
       - each guesser continues as long as they guess currect letters
       - returns final board
    winner returns the player who picked the last letter.

    >>> from wordset import Dictionary
    >>> from player import Player, DummyPlayer
    >>> p = Player(Dictionary("assets/lincoln.txt"))
    >>> game = Game(DummyPlayer("pick"), [ DummyPlayer("guess") ] )
    >>> board = game.play(False)
    >>> board.word()
    ['s', 'c', 'o', 'r', 'e']
    >>> len(board.guesses())
    6
    """
    def __init__(self, picker, guessers):
        # BEGIN
        self.picker = picker
        self.guessers = guessers
        self.winner = -1
        "*** REPLACE THIS LINE ***"
        # END

    def play(self, verbose=True):
        # BEGIN
        board = Board(SecretWord(self.picker.pick_word()))
        while not board.done():
            if len(self.guessers)>1:
                flag = True
            else:
                flag = False
            for guesser in range(len(self.guessers)):
                self.winner = guesser
                guess_word = self.guessers[guesser].guess(board)
                if guess_word:
                    board.guess(guess_word)
                else:
                    return board
                if verbose:
                    if flag:
                        print(self.guessers[guesser].name,'guesses', guess_word)
                    board.display()
                    if board.done() and flag:
                        print('winner is', self.guessers[guesser].name)
                        break
                while guess_word in board.hits() and not board.done():
                    guess_word = self.guessers[guesser].guess(board)
                    if guess_word:
                        board.guess(guess_word)
                    else:
                        return board
                    if verbose:
                        if flag:
                            print(self.guessers[guesser].name,'guesses', guess_word)
                        board.display()
                        if board.done() and flag:
                            print('winner is', self.guessers[guesser].name)
    
        return board
        "*** REPLACE THIS LINE ***"
        # END

    def winner(self):
        # BEGIN
        return self.guessers[self.winner]
        "*** REPLACE THIS LINE ***"
        # END



