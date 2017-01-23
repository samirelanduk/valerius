from unittest import TestCase
from valerius.genome import Genome

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


    def test_genome_repr(self):
        genome = Genome("GCATCGTATACAGCAGTACGT")
        self.assertEqual(str(genome), "<Genome (21 bases)>")



class GenomePropertyTests(TestCase):

    def test_basic_properties(self):
        genome = Genome("GCATCGTATACAGCAGTACGT")
        self.assertIs(genome.sequence(), genome._sequence)
