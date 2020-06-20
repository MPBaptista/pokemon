import time
import sys
import utils
import re

class Ash():
    """
    Create initial Ash instance.
    """

    def __init__(self):
        """
        Create ash at default position (0,0), initialize explored map and pokemons.
        """
        self.position = [0,0]
        self.explored_map = set()
        self.explored_map.add((0,0))

    def get_position_tuple(self):
        """ 
        Return current Ash position as tuple
        """
        return (self.position[0], self.position[1])
    def get_pokemons(self):
        """
        Get number of pokemons in Ash's Pokedex
        """
        return len(self.explored_map)
    def move(self,direction):
        """
        Move ash in argument direction
        """
        if direction == "N":
            self.position[1] += 1
        if direction == "S":
            self.position[1] -= 1
        if direction == "E":
            self.position[0] += 1
        if direction == "O":
            self.position[0] -= 1
        self.explored_map.add(self.get_position_tuple())


def main():
    ash = Ash()
    print("Bem-vindo Ash!")
    while True:
        sequence = utils.get_input()
        validated_sequence = utils.validade_sequence(sequence)

        start = time.process_time()
        if validated_sequence[0]:
            for direction in validated_sequence[1]:
                ash.move(direction)
        else:
            break

        end = time.process_time()
        print(ash.get_pokemons())
        print("time: " + str(end-start))
            
        flag = str(input("\nDeseja Continuar? (s/n) "))
        if re.match("[s]", flag):
            pass
        elif re.match("[n]", flag):
            print("\nAdeus Ash!")
            break
        else:
            print("Comando inválido")
            break

if __name__ == "__main__":
    main()

