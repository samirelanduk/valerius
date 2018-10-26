import builtins
import re
import requests
from .sequences import Sequence

def open(path):
    """Opens a sequence file and returns a processed :py:class:`.Sequence`.

    If the file is a FASTA file this will be detected and parsed accordingly.

    :param str path: the location of the sequence file.
    :rtype: ``Sequence``"""

    with builtins.open(path) as f:
        return string_to_sequence(f.read())



def string_to_sequence(string):
    """Takes a filestring and turns it into a :py:class:`.Sequence`, parsing
    from FASTA if required.

    :param str string: the string to convert.
    :rtype: ``Sequence``"""

    lines = string.splitlines()[1:] if is_fasta(string) else string.splitlines()
    string = " ".join([
     line for line in lines if line.strip()
    ]).replace(" ", "")
    return Sequence(string)


def is_fasta(filestring):
    """Checks whether a filestring is FASTA formatted.

    :param str filestring: the filestring to check.
    :rtype: ``bool``"""

    return re.match(r"^>(.+?)\|(.+)\n", filestring)


def fetch(accession):
    """Fetches a sequence from UNIPROT by accession code.

    :param str accession: the UNIPROT accession ID.
    :rtype: ``Sequence``"""
    
    response = requests.get(
     "https://www.uniprot.org/uniprot/{}.fasta".format(accession)
    )
    if response.status_code == 200:
        return string_to_sequence(response.text)
