from unittest import TestCase
from unittest.mock import patch
from valerius.sequence import BioSequence, DnaSequence

class DnaSequenceCreationTests(TestCase):

    def test_can_create_dna_sequence(self):
        sequence = DnaSequence("GCATCGTATACAGCAGTACGT")
        self.assertIsInstance(sequence, BioSequence)


    @patch("valerius.sequence.BioSequence.__init__")
    def test_dna_sequence_uses_biosequence_initialisation(self, mock):
        sequence = DnaSequence("GCATCGTATACAGCAGTACGT")
        self.assertTrue(mock.called)


    def test_can_only_use_valid_bases(self):
        with self.assertRaises(ValueError):
            DnaSequence("GCATCGTATACAGCAGTACGW")


    def test_invalid_base_reports_which_base_is_wrong(self):
        with self.assertRaises(ValueError) as context:
            DnaSequence("GCATCGTATACAGCAGTACGW")
        self.assertIn("'W'", str(context.exception))
        with self.assertRaises(ValueError) as context:
            DnaSequence("GCATCGTATZACAGCAGTACGW")
        self.assertIn("'Z'", str(context.exception))
