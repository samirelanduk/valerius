"""Structures that contain multiple sequences."""

from .utilities import from_string

class SequenceSet:
    """A collection of :py:class:`.Sequence` objects. You can pass in strings
    instead if you wish, and these will be converted automatically.

    :param \*sequences: The sequences to make up the set."""

    def __init__(self, *sequences):
        sequences = [from_string(s) if isinstance(s, str)
         else s for s in sequences]
        self._sequences = tuple(sequences)


    def __repr__(self):
        return "<SequenceSet ({} sequence{})>".format(
         len(self._sequences), "" if len(self._sequences) == 1 else "s"
        )


    def __getitem__(self, index):
        return self._sequences[index]


    @property
    def sequences(self):
        """Returns the :py:class:`.Sequence` objects contained within.

        :rtype: ``tuple``"""

        return self._sequences
