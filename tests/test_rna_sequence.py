from unittest import TestCase
from unittest.mock import patch
from valerius.sequence import NucleotideSequence, RnaSequence

class RnaSequenceCreationTests(TestCase):

    def test_can_create_rna_sequence(self):
        sequence = RnaSequence("GCAUCGUAUACAGCAGUACGU")
        self.assertIsInstance(sequence, NucleotideSequence)


    @patch("valerius.sequence.NucleotideSequence.__init__")
    def test_rna_sequence_uses_nucleotide_sequence_initialisation(self, mock):
        sequence = RnaSequence("GCAUCGUAUACAGCAGUACGU")
        self.assertTrue(mock.called)


    def test_can_only_use_valid_bases(self):
        with self.assertRaises(ValueError):
            RnaSequence("GCAUCGUAUACAGCAGUACGT")


    def test_invalid_base_reports_which_base_is_wrong(self):
        with self.assertRaises(ValueError) as context:
            RnaSequence("GCAUCGUAUACAGCAGUACGT")
        self.assertIn("'T'", str(context.exception))
        with self.assertRaises(ValueError) as context:
            RnaSequence("GCAUCGUAUZACAGCAGUACGT")
        self.assertIn("'Z'", str(context.exception))


    def test_rna_sequence_repr(self):
        sequence = RnaSequence("GCAUCGUAUACAGCAGUACGU")
        self.assertEqual(str(sequence), "<RnaSequence (21 bases)>")
