from unittest import TestCase
from genomia.genome import Genome

class GenomeCreationTests(TestCase):

    def test_can_create_genome(self):
        genome = Genome("GCATCGTATACAGCAGTACGT")
        self.assertEqual(genome._sequence, "GCATCGTATACAGCAGTACGT")
