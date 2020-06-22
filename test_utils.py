import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_parse_input(self):
        """Test utils input parser.
        
        Test input parser with valid and invalid sequences.

        Returns OK when successful.
        """
        self.assertEqual(utils.parse_input("E"), (True, ["E"]))
        self.assertEqual(utils.parse_input("NESO"), (True, ["N","E","S","O"]))
        self.assertEqual(utils.parse_input("EQ"), (False, ["E"]))
        self.assertEqual(utils.parse_input("QE"), (False, []))
        self.assertEqual(utils.parse_input("1"), (False, []))

if __name__ == '__main__':
    unittest.main()