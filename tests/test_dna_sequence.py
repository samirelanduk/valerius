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
