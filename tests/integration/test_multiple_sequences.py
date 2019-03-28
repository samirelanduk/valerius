from unittest import TestCase
import valerius

class PairwiseAlignmentTests(TestCase):

    def test_dot_matrix(self):
        seq1, seq2 = valerius.open("tests/integration/files/anhydrase.fasta")
        matrix = seq1.dot_matrix(seq2)
        self.assertEqual(matrix[0][0], 1)
        self.assertEqual(matrix[1][1], 1)
        self.assertEqual(matrix[2][2], 0)
        self.assertEqual(matrix[2][3], 1)
        matrix.show()
