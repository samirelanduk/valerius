import re
class BioSequence:

    def __init__(self, sequence):
        if not isinstance(sequence, str):
            raise TypeError("Sequence must be str, not '%s'" % str(sequence))
        self._sequence = sequence


    def __repr__(self):
        return "<%s (%i bases)>" % (self.__class__.__name__, len(self._sequence))


    def sequence(self):
        return self._sequence



class DnaSequence(BioSequence):

    def __init__(self, sequence, *args, **kwargs):
        BioSequence.__init__(self, sequence, *args, **kwargs)
        pattern = re.compile("^[GCAT]+$")
        if not pattern.match(sequence):
            bad_base = sequence[re.search(r'[^AGCT]', sequence).start()]
            raise ValueError("'%s' is not a valid DNA base" % bad_base)


    def gc_content(self):
        return len(
         [base for base in self.sequence() if base == "G" or base == "C"]
        ) / len(self.sequence())



class PeptideSequence(BioSequence):

    def __init__(self, sequence, *args, **kwargs):
        BioSequence.__init__(self, sequence, *args, **kwargs)
        pattern = re.compile("^[GALMFWKQESPVICYHRNDT]+$")
        if not pattern.match(sequence):
            bad_peptide = sequence[
             re.search(r'[^GALMFWKQESPVICYHRNDT]', sequence).start()
            ]
            raise ValueError("'%s' is not a valid peptide residue" % bad_peptide)
