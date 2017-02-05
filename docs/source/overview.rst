Overview
--------

Biological Sequences
~~~~~~~~~~~~~~~~~~~~

All sequences are ultimately instances of :py:class:`.BioSequence`.

Nucleotide Sequences
~~~~~~~~~~~~~~~~~~~~

Nucleotide sequences - :py:class:`.NucleotideSequence` - hold genetic
information.

Generally, you would use one of its subclasses, :py:class:`.DnaSequence` or
:py:class:`.RnaSequence`. In any case, all nucleotides have a GC content
measure:

  >>> from valerius.sequence import DnaSequence
  >>> sequence = DnaSequence("TGACAATATATATATATATATAATGCTAGC")
  >>> sequence.gc_content()
  0.2

Peptide Sequences
~~~~~~~~~~~~~~~~~

Peptide sequences - :py:class:`.PeptideSequence` - are for chains of amino acid
residues such as proteins.
