import builtins
from .sequences import Sequence

def open(path):
    """Opens a sequence file and returns a processed :py:class:`.Sequence`.

    :param str path: the location of the sequence file.
    :rtype: ``Sequence``"""
    
    with builtins.open(path) as f:
        string = " ".join([
         line for line in f.read().splitlines() if line.strip()
        ]).replace(" ", "")
        return Sequence(string)
