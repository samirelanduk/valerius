from unittest import TestCase
import valerius

class SequenceSetTests(TestCase):

    def test_sequence_interaction_tests(self):
        pass


    def test_raw_sequence_sets(self):
        seq1 = valerius.from_string("LPLLALLALWGPDPAAAFVNQHL")
        seq2 = valerius.from_string("LLALLALWGPDPAAASVNQHLLH")
        seq3 = valerius.from_string("LPLLALLALLGPDPAFVN")
        seq_set = valerius.SequenceSet(seq1, seq2, seq3)
        self.assertEqual(seq_set.sequences, (seq1, seq2, seq3))
        self.assertEqual(seq_set[1], seq2)


    def test_sequence_sets_from_list(self):
        pass



class SequenceSetOpeningTests(TestCase):

    def test_can_open_sequences_from_file(self):
        pass
