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


    def test_can_only_use_valid_residues(self):
        with self.assertRaises(ValueError):
            PeptideSequence("MGDVLEQFFILTGLLVX")


    def test_invalid_peptide_reports_which_peptide_is_wrong(self):
        with self.assertRaises(ValueError) as context:
            PeptideSequence("MGDVLEQFFILTGLLVX")
        self.assertIn("'X'", str(context.exception))
        with self.assertRaises(ValueError) as context:
            PeptideSequence("MGDVLEJQFFILTGLLVX")
        self.assertIn("'J'", str(context.exception))


    def test_peptide_sequence_repr(self):
        sequence = PeptideSequence("MGDVLEQFFILTGLLV")
        self.assertEqual(str(sequence), "<PeptideSequence (16 bases)>")
