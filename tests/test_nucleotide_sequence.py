from unittest import TestCase
from unittest.mock import patch
from valerius.sequence import BioSequence, NucleotideSequence

class NucleotideSequenceCreationTests(TestCase):

    def test_can_create_nucelotide_sequence(self):
        sequence = NucleotideSequence("GCATCGTATACAGCAGTACGT")
        self.assertIsInstance(sequence, BioSequence)


    @patch("valerius.sequence.BioSequence.__init__")
    def test_dna_sequence_uses_biosequence_initialisation(self, mock):
        sequence = NucleotideSequence("GCATCGTATACAGCAGTACGT")
        self.assertTrue(mock.called)


    def test_dna_sequence_repr(self):
        sequence = NucleotideSequence("GCATCGTATACAGCAGTACGT")
        self.assertEqual(str(sequence), "<NucleotideSequence (21 bases)>")



class GcContentTests(TestCase):

    def test_all_gc_is_1(self):
        sequence = NucleotideSequence("GGGGG")
        self.assertEqual(sequence.gc_content(), 1)
        sequence = NucleotideSequence("CCCCC")
        self.assertEqual(sequence.gc_content(), 1)
        sequence = NucleotideSequence("GCGCG")
        self.assertEqual(sequence.gc_content(), 1)


    def test_no_gc_is_0(self):
        sequence = NucleotideSequence("ATATAT")
        self.assertEqual(sequence.gc_content(), 0)


    def test_mixed_gc_content(self):
        sequence = NucleotideSequence("GA")
        self.assertEqual(sequence.gc_content(), 0.5)
        sequence = NucleotideSequence("GATT")
        self.assertEqual(sequence.gc_content(), 0.25)
        sequence = NucleotideSequence("GATTCCGCCGGG")
        self.assertEqual(sequence.gc_content(), 0.75)
