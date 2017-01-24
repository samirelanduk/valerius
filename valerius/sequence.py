class BioSequence:

    def __init__(self, sequence):
        if not isinstance(sequence, str):
            raise TypeError("Sequence must be str, not '%s'" % str(sequence))
        self._sequence = sequence


    def __repr__(self):
        return "<BioSequence (%i bases)>" % len(self._sequence)


    def sequence(self):
        return self._sequence
