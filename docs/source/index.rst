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

Table of Contents
-----------------

.. toctree ::
  installing
  overview
  api
  contributing
  changelog
