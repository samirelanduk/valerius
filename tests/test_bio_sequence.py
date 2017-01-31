from unittest import TestCase
from valerius.sequence import BioSequence

class BioSequencereationTests(TestCase):

    def test_can_create_biosequence(self):
        sequence = BioSequence("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.assertEqual(sequence._sequence, "ABCDEFGHIJKLMNOPQRSTUVWXYZ")


    def test_need_sequence(self):
        with self.assertRaises(TypeError):
            BioSequence()


    def test_biosequence_must_be_str(self):
        with self.assertRaises(TypeError):
            BioSequence(1001)


    def test_sequence_repr(self):
        sequence = BioSequence("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.assertEqual(str(sequence), "<BioSequence (26 bases)>")



class BioSequencePropertyTests(TestCase):

    def test_basic_properties(self):
        sequence = BioSequence("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.assertIs(sequence.sequence(), sequence._sequence)