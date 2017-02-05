"""Classes for the various kinds of Biological sequence."""

import re

class BioSequence:
    """The base class for all Biological sequences.

    :param str sequence: The sequence the object shall represent."""

    def __init__(self, sequence):
        if not isinstance(sequence, str):
            raise TypeError("Sequence must be str, not '%s'" % str(sequence))
        self._sequence = sequence


    def __repr__(self):
        return "<%s (%i bases)>" % (self.__class__.__name__, len(self._sequence))


    def sequence(self):
        """Returns the sequence as a string."""

        return self._sequence



class NucleotideSequence(BioSequence):
    """Base class: :py:class:`BioSequence`

    Represents nucleotide chains of any kind.

    :param str sequence: The sequence the object shall represent."""

    def __init__(self, *args, **kwargs):
        BioSequence.__init__(self, *args, **kwargs)


    def gc_content(self):
        """The proportion of bases which are guanine or cytosine."""

        gc_bases = self.sequence().count("G") + self.sequence().count("C")
        return gc_bases / len(self.sequence())



class DnaSequence(NucleotideSequence):
    """Base class: :py:class:`NucleotideSequence`

    Represents DNA sequences of any kind.

    :param str sequence: The sequence the object shall represent. The only\
    acceptable bases are G, C, A and T."""

    def __init__(self, sequence, *args, **kwargs):
        NucleotideSequence.__init__(self, sequence, *args, **kwargs)
        pattern = re.compile(r"^[GCAT]+$")
        if not pattern.match(sequence):
            bad_base = sequence[re.search(r"[^AGCT]", sequence).start()]
            raise ValueError("'%s' is not a valid DNA base" % bad_base)



class RnaSequence(NucleotideSequence):
    """Base class: :py:class:`NucleotideSequence`

    Represents RNA sequences of any kind.

    :param str sequence: The sequence the object shall represent. The only\
    acceptable bases are G, C, A and U."""

    def __init__(self, sequence, *args, **kwargs):
        NucleotideSequence.__init__(self, sequence, *args, **kwargs)
        pattern = re.compile(r"^[GCAU]+$")
        if not pattern.match(sequence):
            bad_base = sequence[re.search(r"[^AGCU]", sequence).start()]
            raise ValueError("'%s' is not a valid RNA base" % bad_base)



class PeptideSequence(BioSequence):
    """Base class: :py:class:`BioSequence`

    Represents amino acid sequences.

    :param str sequence: The sequence the object shall represent. The only\
    acceptable residues are the twenty canonical amino acids."""

    def __init__(self, sequence, *args, **kwargs):
        BioSequence.__init__(self, sequence, *args, **kwargs)
        pattern = re.compile("^[GALMFWKQESPVICYHRNDT]+$")
        if not pattern.match(sequence):
            bad_peptide = sequence[
             re.search(r"[^GALMFWKQESPVICYHRNDT]", sequence).start()
            ]
            raise ValueError("'%s' is not a valid peptide residue" % bad_peptide)
