import unittest
import pokemon

class TestPokemon(unittest.TestCase):
    def test_ash(self):
        """Test basic Ash methods

        Test initial position and number of pokemons,
        test again with 1 million successive moves north.

        Returns OK when successful.
        """
        ash = pokemon.Ash()
        self.assertEqual(ash.get_position(), (0,0))
        self.assertEqual(ash.get_pokemons(), 1)
        for i in range(0,1000000):
            ash.move("N")
        self.assertEqual(ash.get_position(), (0,1000000))
        self.assertEqual(ash.get_pokemons(), 1000001)   


if __name__ == '__main__':
    unittest.main()