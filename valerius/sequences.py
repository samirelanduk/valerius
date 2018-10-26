"""Classes for the various kinds of Biological sequence."""

from collections import Counter

class Sequence:
    """A string sequence of some kind.

    :param str string: the raw string."""

    def __init__(self, string):
        self._string = string


    def __repr__(self):
        return "<{} (length: {})>".format(
         self.__class__.__name__, len(self._string)
        )


    def __str__(self):
        if len(self._string) < 25:
            return self._string
        else:
            return "{}...({} omitted)...{}".format(
             self._string[:10], len(self._string) - 20, self._string[-10:]
            )


    def __len__(self):
        return len(self._string)


    def __eq__(self, other):
        try:
            return self._string == other._string
        except AttributeError:
            return self._string == other


    def __iter__(self):
        return iter(self._string)


    def __contains__(self, substring):
        return substring in self._string


    def __getitem__(self, index):
        return self.__class__(self._string[index])


    def __setitem__(self, index, char):
        if len(char) != 1:
            raise ValueError("Can only substitute one character at a time")
        self._string = "{}{}{}".format(
         self._string[:index], char, "" if index == -1 else self._string[index + 1:]
        )


    @property
    def length(self):
        """The length of the string.

        :rtype: ``int``"""

        return len(self)


    @property
    def string(self):
        """The sequence's raw string.

        :rtype: ``str``"""

        return self._string


    @property
    def frequencies(self):
        """Returns the frequency of each character in the sequence.

        :rtype: ``Counter``"""
        
        return Counter(self._string)
