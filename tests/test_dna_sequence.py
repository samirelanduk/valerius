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


    def test_dna_sequence_repr(self):
        sequence = DnaSequence("GCATCGTATACAGCAGTACGT")
        self.assertEqual(str(sequence), "<DnaSequence (21 bases)>")



class GcContentTests(TestCase):

    def test_all_gc_is_1(self):
        sequence = DnaSequence("GGGGG")
        self.assertEqual(sequence.gc_content(), 1)
        sequence = DnaSequence("CCCCC")
        self.assertEqual(sequence.gc_content(), 1)
        sequence = DnaSequence("GCGCG")
        self.assertEqual(sequence.gc_content(), 1)


    def test_no_gc_is_0(self):
        sequence = DnaSequence("ATATAT")
        self.assertEqual(sequence.gc_content(), 0)


    def test_mixed_gc_content(self):
        sequence = DnaSequence("GA")
        self.assertEqual(sequence.gc_content(), 0.5)
        sequence = DnaSequence("GATT")
        self.assertEqual(sequence.gc_content(), 0.25)
        sequence = DnaSequence("GATTCCGCCGGG")
        self.assertEqual(sequence.gc_content(), 0.75)
