"""Structures that contain multiple sequences."""

class SequenceSet:
    """A collection of :py:class:`.Sequence` objects."""

    def __init__(self, *sequences):
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
