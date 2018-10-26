from unittest import TestCase
from unittest.mock import Mock, patch, PropertyMock, MagicMock
from valerius.sequences import Sequence

class SequenceCreationTests(TestCase):

    def test_can_create_sequence(self):
        s = Sequence("ABC")
        self.assertEqual(s._string, "ABC")



class SequenceReprTests(TestCase):

    def test_sequence_repr(self):
        s = Sequence("ABC")
        self.assertEqual(repr(s), "<Sequence (length: 3)>")



class SequenceStrTests(TestCase):

    def test_sequence_short_str(self):
        s = Sequence("ABC")
        self.assertEqual(str(s), "ABC")


    def test_sequence_long_str(self):
        s = Sequence("ABC" * 100)
        self.assertEqual(str(s), "ABCABCABCA...(280 omitted)...CABCABCABC")



class SequenceLenTests(TestCase):

    def test_sequence_len(self):
        s = Sequence("ABC")
        self.assertEqual(len(s), 3)



class SequenceEqualityTests(TestCase):

    def test_equality_with_sequence(self):
        s = Sequence("ABC")
        other = Mock(_string="ABC")
        self.assertEqual(s, other)
        other._string = "BCD"
        self.assertNotEqual(s, other)


    def test_equality_with_string(self):
        s = Sequence("ABC")
        self.assertEqual(s, "ABC")
        self.assertNotEqual(s, "BCD")



class SequenceIterationTests(TestCase):

    def test_can_iterate_over_sequence(self):
        s = Sequence("ABC")
        chars = [c for c in s]
        self.assertEqual(chars, ["A", "B", "C"])



class SequenceContainerTests(TestCase):

    def test_sequences_are_containers(self):
        s = Sequence("ABC")
        self.assertIn("A", s)
        self.assertIn("BC", s)
        self.assertNotIn("D", s)



class SequenceIndexingTests(TestCase):

    def test_can_get_substrings(self):
        s = Sequence("ABC")
        sub = s[0]
        self.assertIsInstance(sub, Sequence)
        self.assertEqual(sub._string, "A")



class SequenceSettingTests(TestCase):

    def test_can_set_substrings(self):
        s = Sequence("ABC")
        s[1] = "P"
        self.assertEqual(s._string, "APC")


    def test_can_only_set_one_string_at_a_time(self):
        s = Sequence("ABC")
        with self.assertRaises(ValueError):
            s[1] = "PP"



class SequenceLengthTests(TestCase):

    @patch("valerius.sequences.Sequence.__len__")
    def test_sequence_length(self, mock_len):
        mock_len.return_value = 200
        s = Sequence("ABC")
        self.assertIs(s.length, 200)



class SequenceStringTests(TestCase):

    def test_can_get_string(self):
        s = Sequence("ABC")
        self.assertIs(s.string, s._string)
