from unittest import TestCase
from unittest.mock import Mock, patch, PropertyMock, MagicMock
from valerius.utilities import *

class FileOpeningTests(TestCase):

    @patch("builtins.open")
    @patch("valerius.utilities.string_to_sequence")
    def test_can_open_file(self, mock_seq, mock_open):
        open_return = MagicMock()
        mock_file = Mock()
        open_return.__enter__.return_value = mock_file
        mock_file.read.return_value = "ABCD\nEF GH\n\n123"
        mock_open.return_value = open_return
        s = open("path/to/file")
        mock_open.assert_called_with("path/to/file")
        mock_seq.assert_called_with("ABCD\nEF GH\n\n123")
        self.assertIs(s, mock_seq.return_value)



class SequenceClassGettingTests(TestCase):

    def test_can_detect_dna(self):
        self.assertIs(get_sequence_class("ACGTCGA"), DnaSequence)


    def test_can_detect_rna(self):
        self.assertIs(get_sequence_class("ACGUCGA"), RnaSequence)


    def test_can_detect_protein(self):
        self.assertIs(get_sequence_class("MFPYTVA"), PeptideSequence)



class StringToSequenceTests(TestCase):

    @patch("valerius.utilities.is_fasta")
    @patch("valerius.utilities.get_sequence_class")
    def test_can_process_text(self, mock_cls, mock_is):
        mock_is.return_value = False
        s = string_to_sequence("ABCD\nEF GH\n\n123")
        mock_is.assert_called_with("ABCD\nEF GH\n\n123")
        mock_cls.return_value.assert_called_with("ABCDEFGH123")
        self.assertIs(s, mock_cls.return_value.return_value)


    @patch("valerius.utilities.is_fasta")
    @patch("valerius.utilities.get_sequence_class")
    def test_can_process_fasta_text(self, mock_cls, mock_is):
        mock_is.return_value = True
        s = string_to_sequence("ABCD\nEF GH\n\n123")
        mock_is.assert_called_with("ABCD\nEF GH\n\n123")
        mock_cls.return_value.assert_called_with("EFGH123")
        self.assertIs(s, mock_cls.return_value.return_value)



class IsFastaTests(TestCase):

    def test_can_find_fasta(self):
        self.assertTrue(is_fasta(">..|..\n..."))


    def test_can_reject_fasta(self):
        self.assertFalse(is_fasta("..|..\n..."))
        self.assertFalse(is_fasta(">..|....."))
        self.assertFalse(is_fasta(">....\n..."))



class FetchingTests(TestCase):

    @patch("requests.get")
    @patch("valerius.utilities.string_to_sequence")
    def test_can_fetch_sequence_from_uniprot(self, mock_seq, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = "1334"
        s = fetch("ABC")
        mock_get.assert_called_with("https://www.uniprot.org/uniprot/ABC.fasta")
        mock_seq.assert_called_with("1334")
        self.assertIs(s, mock_seq.return_value)
