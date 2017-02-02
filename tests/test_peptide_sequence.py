from unittest import TestCase
from unittest.mock import patch
from valerius.sequence import BioSequence, PeptideSequence

class PeptideSequenceCreationTests(TestCase):

    def test_can_create_peptide_sequence(self):
        sequence = PeptideSequence("MGDVLEQFFILTGLLV")
        self.assertIsInstance(sequence, BioSequence)


    @patch("valerius.sequence.BioSequence.__init__")
    def test_peptide_sequence_uses_biosequence_initialisation(self, mock):
        sequence = PeptideSequence("MGDVLEQFFILTGLLV")
        self.assertTrue(mock.called)
