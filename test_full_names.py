import unittest
from full_names import get_f_n
class NamesTestCase(unittest.TestCase):
    """Tests for names.py"""
    def test_first_last(self):
        """Tests names like janis joplin"""
        full_name = get_f_n('janis', 'joplin')
        self.assertEqual(full_name, 'Janis Joplin')

    def test_middle(self):
        """Tests names like david lee roth"""
        full_name = get_f_n('david', 'roth', 'lee')
        self.assertEqual(full_name, 'David Lee Roth')

unittest.main()