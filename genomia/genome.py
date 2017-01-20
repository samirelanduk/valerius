class Genome:

    def __init__(self, sequence):
        if not isinstance(sequence, str):
            raise TypeError("Sequence must be str, not '%s'" % str(sequence))
        chars_used = set(sequence)
        for char in chars_used:
            if char not in ("A", "T", "G", "C"):
                raise ValueError("%s is not a valid base" % char)
        self._sequence = sequence


    def __repr__(self):
        return "<Genome (%i bases)>" % len(self._sequence)


    def sequence(self):
        return self._sequence
