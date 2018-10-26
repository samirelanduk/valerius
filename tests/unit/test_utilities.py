from unittest import TestCase
from unittest.mock import Mock, patch, PropertyMock, MagicMock
from valerius.utilities import *

class FileOpeningTests(TestCase):

    @patch("builtins.open")
    @patch("valerius.utilities.is_fasta")
    @patch("valerius.utilities.Sequence")
    def test_can_open_file(self, mock_seq, mock_is, mock_open):
        open_return = MagicMock()
        mock_file = Mock()
        open_return.__enter__.return_value = mock_file
        mock_file.read.return_value = "ABCD\nEF GH\n\n123"
        mock_open.return_value = open_return
        mock_is.return_value = False
        s = open("path/to/file")
        mock_open.assert_called_with("path/to/file")
        mock_seq.assert_called_with("ABCDEFGH123")
        self.assertIs(s, mock_seq.return_value)


    @patch("builtins.open")
    @patch("valerius.utilities.is_fasta")
    @patch("valerius.utilities.Sequence")
    def test_can_open_fasta_file(self, mock_seq, mock_is, mock_open):
        open_return = MagicMock()
        mock_file = Mock()
        open_return.__enter__.return_value = mock_file
        mock_file.read.return_value = "ABCD\nEF GH\n\n123"
        mock_open.return_value = open_return
        mock_is.return_value = True
        s = open("path/to/file")
        mock_open.assert_called_with("path/to/file")
        mock_seq.assert_called_with("EFGH123")
        self.assertIs(s, mock_seq.return_value)
