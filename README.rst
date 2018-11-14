|travis| |coveralls| |pypi|

.. |travis| image:: https://api.travis-ci.org/samirelanduk/valerius.svg?branch=0.2
  :target: https://travis-ci.org/samirelanduk/valerius/

.. |coveralls| image:: https://coveralls.io/repos/github/samirelanduk/valerius/badge.svg?branch=0.2
  :target: https://coveralls.io/github/samirelanduk/valerius/

.. |pypi| image:: https://img.shields.io/pypi/pyversions/valerius.svg
  :target: https://pypi.org/project/valerius/

valerius
========

valerius is a simple Bioinformatics toolset for processing Biological
sequences.

Example
-------

  >>> import valerius
  >>> sequence = valerius.from_string("TGACAATATATATATATATATAATGCTAGC")
  >>> sequence.type
  'DNA'
  >>> sequence.gc_content
  0.2



Installing
----------

pip
~~~

valerius can be installed using pip:

``$ pip3 install valerius``

valerius is written for Python 3, and does not support Python 2.

If you get permission errors, try using ``sudo``:

``$ sudo pip3 install valerius``


Development
~~~~~~~~~~~

The repository for valerius, containing the most recent iteration, can be
found `here <http://github.com/samirelanduk/valerius/>`_. To clone the
valerius repository directly from there, use:

``$ git clone git://github.com/samirelanduk/valerius.git``


Requirements
~~~~~~~~~~~~

valerius requires `requests <https://docs.python-requests.org/>`_.


Overview
--------

From String
~~~~~~~~~~~

A sequence can be made from a string using:

    >>> import valerius
    >>> sequence1 = valerius.from_string("MALWMRLLPL")
    >>> sequence2 = valerius.from_string("ggttgaactactcat")

valerius will automatically detect which sequence type it is, and will return a
``PeptideSequence`` for example, or ``RnaSequence`` as
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


Changelog
---------

Release 0.2.0
~~~~~~~~~~~~~

`14 November 2018`

* You can now fetch sequences from servers.
* Added sequence type detection.
* Residue code generation from sequence now possible.
* Added FASTA parsing.


Release 0.1.0
~~~~~~~~~~~~~

`5 February 2017`

* Added basic nucleotide and peptide sequence classes.
