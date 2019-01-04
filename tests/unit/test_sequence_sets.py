from unittest import TestCase
from unittest.mock import Mock, patch, PropertyMock, MagicMock
from valerius.sets import SequenceSet

class SequenceSetTest(TestCase):

    def setUp(self):
        self.seq1, self.seq2, self.seq3 = Mock(), Mock(), Mock()
        self.sequences = [self.seq1, self.seq2, self.seq3]



class SequenceSetCreationTests(SequenceSetTest):

    def test_can_create_sequence_set(self):
        s = SequenceSet(*self.sequences)
        self.assertEqual(s._sequences, tuple(self.sequences))



class SequenceSetRepr(SequenceSetTest):

    def test_can_get_sequence_set_repr(self):
        s = SequenceSet(*self.sequences)
        self.assertEqual(repr(s), "<SequenceSet (3 sequences)>")


    def test_can_get_sequence_set_repr_one_sequence(self):
        s = SequenceSet(self.sequences[0])
        self.assertEqual(repr(s), "<SequenceSet (1 sequence)>")



class SequenceSetIndexingTests(SequenceSetTest):

    def test_can_get_sequence_by_index(self):
        s = SequenceSet(*self.sequences)
        self.assertEqual(s[0], self.seq1)
        self.assertEqual(s[-1], self.seq3)



class SequenceSetSequenceProperty(SequenceSetTest):

    def test_can_get_sequences(self):
        s = SequenceSet(*self.sequences)
        self.assertEqual(s.sequences, s._sequences)
