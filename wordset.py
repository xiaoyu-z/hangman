from utils import lowercase, key_of_max
import string
from collections import OrderedDict    # Variant of dict that you might want to learn about

#
# WordSet class
#
class WordSet:
    """Set of unique words, all in lower case and of positive length.

    >>> WordSet("one two, Two. tHree").words()
    ['one', 'three', 'two']
    >>> WordSet(["one","two","Two", ""]).words()
    ['one', 'two']
    >>> 'two' in WordSet(["one","two","Two"])
    True
    """
    def __init__(self, text):
        """Form a WordSet from a string of words or collection of words.
        """
        # BEGIN Question 2
        "*** REPLACE THIS LINE ***"
        self.word_set = []
        if type(text) == str:
            for i in text.split(' '):
                if i.find('\n')>0:
                    for k in i.split('\n'):
                        new_word = str.lower(''.join([j for j in k if str.isalpha(j)]))
                        if new_word not in self.word_set and new_word:
                            self.word_set.append(new_word.strip())

                else:
                    new_word = str.lower(''.join([k for k in i if str.isalpha(k)]))
                    if new_word not in self.word_set and new_word:
                        self.word_set.append(new_word.strip())
        if type(text) == list:
            for i in text:
                new_word = str.lower(''.join([k for k in i if str.isalpha(k)]))
                if new_word not in self.word_set and new_word:
                    self.word_set.append(new_word.strip())
                
        # END Question 2

    def words(self):
        """Return sorted list of words in WordSet.

        >>> WordSet("Hi. Hey you. How, the heck, are you?").words()
        ['are', 'heck', 'hey', 'hi', 'how', 'the', 'you']
        """
        # BEGIN Question 2
        "*** REPLACE THIS LINE ***"
        self.word_set.sort()
        return self.word_set
        # END Question 2

    def __contains__(self, word):
        # BEGIN Question 2
        if word in self.word_set:
            return True
        return False
        "*** REPLACE THIS LINE ***"
        # END Question 2


#
# Dictionary class
#
class Dictionary(WordSet):
    """Construct a dictionary from all the words in a text file.
    Subclass of WordSet with a file based initializer.

    >>> from wordset import Dictionary
    >>> Dictionary('assets/lincoln.txt').words()[55]
    'government'
    """
    def __init__(self, filename):
        with open(filename) as fp:
            text = fp.read()
            WordSet.__init__(self, text)

#
# WordMunch class
#
class WordMunch(WordSet):
    """Perform analytics on a set of unique words.

    Subclass of WordSet that provides analytics on the words.

    >>> w = WordMunch("one two, Two. tHree")
    >>> w.words()
    ['one', 'three', 'two']
    >>> w.frequency()['o']
    2
    >>> key_of_max(w.frequency())
    'e'
    """
    def filter(self, ffun):
        """Filter set to include only those that satisfy the filter function predicate."""
        # BEGIN
        new_word_set = []
        for i in self.words():
            if ffun(i):
                new_word_set.append(i)
        self.word_set  = new_word_set
        "*** REPLACE THIS LINE ***"
        # END

    def frequency(self):
        """Return and ordered dictionary of the frequency of each letter in word set."""
        # BEGIN
        frequency = {}
        for i in self.words():
            for k in i:
                frequency[k] = 0
        for i in self.words():
            for k in i:
                frequency[k] += 1
        return frequency
        "*** REPLACE THIS LINE ***"
        # END
