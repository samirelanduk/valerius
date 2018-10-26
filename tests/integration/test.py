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
