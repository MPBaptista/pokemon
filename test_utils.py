import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_validate_sequence(self):
        """Test utils sequence validator.
        
        Test sequence validator with valid and invalid sequences.

        Returns OK when successful.
        """
        self.assertEqual(utils.validate_sequence("E"), (True, ["E"]))
        self.assertEqual(utils.validate_sequence("NESO"), (True, ["N","E","S","O"]))
        self.assertEqual(utils.validate_sequence("EQ"), (False, ["E"]))
        self.assertEqual(utils.validate_sequence("QE"), (False, []))
        self.assertEqual(utils.validate_sequence("1"), (False, []))

if __name__ == '__main__':
    unittest.main()