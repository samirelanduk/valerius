from unittest import TestCase
import valerius

class Tests(TestCase):

    def test(self):
        sequence = valerius.Sequence("MKSPEELKGIFEKYAAKEGDPNQLSKEELKLLLQTEFPLL")
        self.assertEqual(len(sequence), 40)
        self.assertEqual(sequence.length, 40)
        self.assertIn("SPEEL", sequence)
        self.assertNotIn("ABCD", sequence)
        self.assertEqual(sequence[0], "M")
        self.assertEqual(sequence[0], valerius.Sequence("M"))
        self.assertEqual(sequence[-7:-4], "QTE")
        sequence[2] = "X"
        sequence[-2] = "X"
        self.assertEqual(sequence[:5], "MKXPE")
        self.assertEqual(sequence[-5:], "EFPXL")
        self.assertEqual(sequence.string, "MKXPEELKGIFEKYAAKEGDPNQLSKEELKLLLQTEFPXL")
        self.assertEqual(sequence.frequencies, {
         "E": 7, "L": 7, "K": 6, "P": 3, "X": 2, "G": 2, "F": 2, "A": 2,
         "Q": 2, "M": 1, "I": 1, "Y": 1, "D": 1, "N": 1, "S": 1, "T": 1
        })


    def test_opening(self):
        sequence = valerius.open("tests/integration/files/sequence-line.txt")
        self.assertEqual(
         sequence, "CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC"
        )

        sequence = valerius.open("tests/integration/files/sequence-lines.txt")
        self.assertEqual(len(sequence), 300)
        self.assertEqual(sequence[:20], "MGDVLEQFFILTGLLVCLAC")
        self.assertEqual(sequence[-20:], "IPAWAFYSGAFQRLLLTHYV")
