from unittest import TestCase
from unittest.mock import Mock, patch, PropertyMock, MagicMock
from valerius.sequences import NucleotideSequence

class GcContentTests(TestCase):

    def test_can_get_gc_content(self):
        s = NucleotideSequence("ABC")
        self.assertEqual(s.gc_content, 1 / 3)


    def test_can_get_gc_content_no_gc(self):
        s = NucleotideSequence("ABD")
        self.assertEqual(s.gc_content, 0)


    def test_can_get_gc_content_no_sequence(self):
        s = NucleotideSequence("")
        self.assertEqual(s.gc_content, 0)
