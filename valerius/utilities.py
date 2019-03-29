"""Utility functions for reading in data."""

import builtins
import re
import requests
from .sequences import Sequence, DnaSequence, RnaSequence, PeptideSequence

def open(path):
    """Opens a sequence file and returns a processed :py:class:`.Sequence`.

    If the file is a FASTA file this will be detected and parsed accordingly.

    :param str path: the location of the sequence file.
    :rtype: ``Sequence``"""

    with builtins.open(path) as f:
        blocks = split_string(f.read())
        sequences = [from_string(block) for block in blocks]
        return sequences[0] if len(sequences) == 1 else sequences


def split_string(string):
    """Takes a raw string and splits it into individual raw sequences.

    :param str string: the string to split.
    :rtype: ``list``"""

    string = string.replace("\n>", "\n\n>")
    while "\n\n\n" in string:
        string = string.replace("\n\n\n", "\n\n")
    return string.split("\n\n")


def get_sequence_class(string):
    """Looks at a string sequence and tries to guess what kind of sequence it is
    before returning the appropriate class.

    :param str string: the string sequence to inspect.
    :rtype: ``class``"""

    if re.compile(r"^[GCATgcat]+$").match(string):
        return DnaSequence
    elif re.compile(r"^[GCAUgcau]+$").match(string):
        return RnaSequence
    else:
        return PeptideSequence


def from_string(string):
    """Takes a filestring and turns it into a :py:class:`.Sequence`, parsing
    from FASTA if required.

    :param str string: the string to convert.
    :rtype: ``Sequence``"""

    lines = string.splitlines()
    label = lines.pop(0)[1:] if is_fasta(string) else ""
    string = " ".join([
     line for line in lines if line.strip()
    ]).replace(" ", "")
    return get_sequence_class(string)(string, label=label)


def is_fasta(filestring):
    """Checks whether a filestring is FASTA formatted.

    :param str filestring: the filestring to check.
    :rtype: ``bool``"""

    return re.match(r"^>(.+?)\n", filestring)


def fetch(accession, db="uniprot"):
    """Fetches a sequence from UNIPROT by accession code.

    :param str accession: the UNIPROT accession ID.
    :param str db: an alternative database, such as NCBI.
    :rtype: ``Sequence``"""

    url = {
     "uniprot": "https://www.uniprot.org/uniprot/{}.fasta",
     "ncbi": "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
     "efetch.fcgi?db=nucleotide&id={}&rettype=fasta"
    }
    response = requests.get(url[db].format(accession))
    if response.status_code == 200:
        return from_string(response.text)
