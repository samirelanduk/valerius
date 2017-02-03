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



class NucleotideSequence(BioSequence):

    def __init__(self, *args, **kwargs):
        BioSequence.__init__(self, *args, **kwargs)


    def gc_content(self):
        gc_bases = self.sequence().count("G") + self.sequence().count("C")
        return gc_bases / len(self.sequence())



class DnaSequence(NucleotideSequence):

    def __init__(self, sequence, *args, **kwargs):
        NucleotideSequence.__init__(self, sequence, *args, **kwargs)
        pattern = re.compile(r"^[GCAT]+$")
        if not pattern.match(sequence):
            bad_base = sequence[re.search(r"[^AGCT]", sequence).start()]
            raise ValueError("'%s' is not a valid DNA base" % bad_base)



class RnaSequence(NucleotideSequence):

    def __init__(self, sequence, *args, **kwargs):
        NucleotideSequence.__init__(self, sequence, *args, **kwargs)
        pattern = re.compile(r"^[GCAU]+$")
        if not pattern.match(sequence):
            bad_base = sequence[re.search(r"[^AGCU]", sequence).start()]
            raise ValueError("'%s' is not a valid RNA base" % bad_base)



class PeptideSequence(BioSequence):

    def __init__(self, sequence, *args, **kwargs):
        BioSequence.__init__(self, sequence, *args, **kwargs)
        pattern = re.compile("^[GALMFWKQESPVICYHRNDT]+$")
        if not pattern.match(sequence):
            bad_peptide = sequence[
             re.search(r"[^GALMFWKQESPVICYHRNDT]", sequence).start()
            ]
            raise ValueError("'%s' is not a valid peptide residue" % bad_peptide)
