import re
class BioSequence:

    def __init__(self, sequence):
        if not isinstance(sequence, str):
            raise TypeError("Sequence must be str, not '%s'" % str(sequence))
        self._sequence = sequence


    def __repr__(self):
        return "<BioSequence (%i bases)>" % len(self._sequence)


    def sequence(self):
        return self._sequence



class DnaSequence(BioSequence):

    def __init__(self, sequence, *args, **kwargs):
        BioSequence.__init__(self, sequence, *args, **kwargs)
        pattern = re.compile("^[GCAT]+$")
        if not pattern.match(sequence):
            bad_base = sequence[re.search(r'[^AGCT]', sequence).start()]
            raise ValueError("'%s' is not a valid DNA base" % bad_base)
