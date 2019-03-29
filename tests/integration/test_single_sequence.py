from unittest import TestCase
import valerius

class SequenceTests(TestCase):

    def test_raw_sequence_making(self):
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
        self.assertEqual(sequence.type, "unknown")
        self.assertEqual(sequence.label, "")
        self.assertEqual(sequence.frequencies, {
         "E": 7, "L": 7, "K": 6, "P": 3, "X": 2, "G": 2, "F": 2, "A": 2,
         "Q": 2, "M": 1, "I": 1, "Y": 1, "D": 1, "N": 1, "S": 1, "T": 1
        })


    def test_sequence_from_string(self):
        sequence = valerius.from_string("MKXPEELKGIFEKYAAKEGDPNQLSKEELKLLLQTEF")
        self.assertEqual(sequence.type, "peptide")
        sequence = valerius.from_string("ACTAGAATAGCCAGAACCGTTTCTCTGAGCTT")
        self.assertEqual(sequence.type, "DNA")
        self.assertEqual(sequence.gc_content, 0.4375)
        sequence = valerius.from_string("ACUAGAAUAGCCAGAACCGUUUCUCUGAGGCUU")
        self.assertEqual(sequence.type, "RNA")



class SequenceOpeningTests(TestCase):

    def test_opening_single_sequence(self):
        sequence = valerius.open("tests/integration/files/sequence-line.txt")
        self.assertEqual(
         sequence, "CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC"
        )
        self.assertEqual(sequence.codes[:5], ["DC", "DC", "DT", "DG", "DC"])

        sequence = valerius.open("tests/integration/files/sequence-lines.txt")
        self.assertEqual(len(sequence), 300)
        self.assertEqual(sequence[:20], "MGDVLEQFFILTGLLVCLAC")
        self.assertEqual(sequence[-20:], "IPAWAFYSGAFQRLLLTHYV")
        self.assertEqual(sequence.codes[:4], ["MET", "GLY", "ASP", "VAL"])

        sequence = valerius.open("tests/integration/files/insulin.fasta")
        self.assertEqual(len(sequence), 98)
        self.assertEqual(sequence[:20], "MALWMRLLPLLALLALWGPD")
        self.assertEqual(sequence[-20:], "IVEQCCTSICSLYQLENYCN")
        self.assertEqual(
         sequence.label,
         "tr|A6XGL2|A6XGL2_HUMAN Insulin OS=Homo sapiens OX=9606 GN=INS PE=1 SV=1"
        )


    def test_opening_multiple_sequences(self):
        sequences = valerius.open("tests/integration/files/sequences-lines.txt")
        self.assertEqual(len(sequences), 2)
        self.assertEqual(sequences[0][:20], "MGDVLEQFFILTGLLVCLAC")
        self.assertEqual(sequences[0][-20:], "VVKMTQLILKHMESRQKGLI")
        self.assertEqual(sequences[1][:20], "LNISSGIALFPWPLYSMYSA")
        self.assertEqual(sequences[1][-20:], "IPAWAFYSGAFQRLLLTHYV")

        sequences = valerius.open("tests/integration/files/anhydrase.fasta")
        self.assertEqual(len(sequences), 2)
        self.assertEqual(sequences[0][:20], "MASPDWGYDDKNGPEQWSKL")
        self.assertEqual(sequences[0][-20:], "MQHNNRPTQPLKGRTVRASF")
        self.assertEqual(sequences[1][:20], "MAHSDWGYDSPNGPZEWVKL")
        self.assertEqual(sequences[1][-20:], "IQHNNRPPQPLKGRTVRAFF")
        self.assertEqual(
         sequences[0].label,
         "sp|P00915|CAH1_HUMAN Carbonic anhydrase 1 OS=Homo sapiens OX=9606 GN=CA1 PE=1 SV=2"
        )
        self.assertEqual(
         sequences[1].label,
         "sp|P00917|CAH1_HORSE Carbonic anhydrase 1 OS=Equus caballus OX=9796 GN=CA1 PE=1 SV=3"
        )
