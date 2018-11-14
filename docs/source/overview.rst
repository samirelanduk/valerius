Overview
--------

From String
~~~~~~~~~~~

A sequence can be made from a string using:

    >>> import valerius
    >>> sequence1 = valerius.from_string("MALWMRLLPL")
    >>> sequence2 = valerius.from_string("ggttgaactactcat")

valerius will automatically detect which sequence type it is, and will return a
:py:class:`.PeptideSequence` for example, or :py:class:`.RnaSequence` as
required.

Basic properties can be queried:

    >>> "LLP" in sequence1
    True
    >>> sequence1.type
    'peptide'
    >>> sequence.length
    10
    >>> sequence2.frequencies
    Counter({'T': 5, 'A': 4, 'G': 3, 'C': 3})
    >>> sequence1.codes
    ['MET', 'ALA', 'LEU', 'TRP', 'MET', 'ARG', 'LEU', 'LEU', 'PRO', 'LEU']
    >>> sequence2.gc_content
    0.4

Opening
~~~~~~~

You can open a file...

    >>> sequence = valerius.open("my_sequence.fasta")
    >>> sequence
    <DnaSequence (length: 163)>

...or fetch them...

    >>> sequence = valerius.fetch("P01308")
    <PeptideSequence (length: 110)>
