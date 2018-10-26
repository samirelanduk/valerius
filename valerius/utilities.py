import builtins
import re
from .sequences import Sequence

def open(path):
    """Opens a sequence file and returns a processed :py:class:`.Sequence`.

    If the file is a FASTA file this will be detected and parsed accordingly.

    :param str path: the location of the sequence file.
    :rtype: ``Sequence``"""

    with builtins.open(path) as f:
        string = f.read()
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
