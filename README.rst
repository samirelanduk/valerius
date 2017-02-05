valerius
========

valerius is a simple Bioinformatics toolset for processing Biological
sequences.

Example
-------

  >>> from valerius.sequence import DnaSequence
  >>> sequence = DnaSequence("TGACAATATATATATATATATAATGCTAGC")
  >>> sequence.gc_content()
  0.2


Installing
----------

pip
~~~

valerius can be installed using pip:

``$ pip install valerius``

valerius is written for Python 3. If the above installation fails, it may be
that your system uses ``pip`` for the Python 2 version - if so, try:

``$ pip3 install valerius``

Requirements
~~~~~~~~~~~~

valerius currently has no dependencies.


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


Changelog
---------

Release 0.1.0
~~~~~~~~~~~~~

`5 February 2017`

* Added basic nucleotide and peptide sequence classes.
