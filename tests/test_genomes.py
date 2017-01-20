from unittest import TestCase
from genomia.genome import Genome

class GenomeCreationTests(TestCase):

    def test_can_create_genome(self):
        genome = Genome("GCATCGTATACAGCAGTACGT")
        self.assertEqual(genome._sequence, "GCATCGTATACAGCAGTACGT")


    def test_need_sequence(self):
        with self.assertRaises(TypeError):
            Genome()


    def test_sequence_must_be_str(self):
        with self.assertRaises(TypeError):
            Genome(1001)


    def test_only_valid_bases_allowed(self):
        with self.assertRaises(ValueError):
            Genome("GCATCGTATACAGCAGTACGTP")
