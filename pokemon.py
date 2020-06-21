import time
import sys
import utils
import re
import argparse

class Ash():

    def __init__(self):
        """Creates ash instance at default position (0,0), initialize explored map and pokemons."""
        self.position = (0,0)
        self.explored_map = set()
        self.explored_map.add(self.position)

    def get_position(self):
        """Returns current Ash position as tuple"""
        return self.position

    def get_pokemons(self):
        """Gets number of pokemons in Ash's Pokedex"""
        return len(self.explored_map)

    def move(self,direction):
        """
        Moves ash in argument direction
        
        Args:
            direction (str): string of direction to move in.
        """
        if direction == "N":
            self.position = (self.position[0], self.position[1] + 1)
        if direction == "S":
            self.position = (self.position[0], self.position[1] - 1)
        if direction == "E":
            self.position = (self.position[0] + 1, self.position[1])
        if direction == "O":
            self.position = (self.position[0] - 1, self.position[1])
        self.explored_map.add(self.get_position())


def main():
    # Parse program flags
    parser = argparse.ArgumentParser(description="Ash goes looking for pokemons in bidimensional field. Each position around him has one single pokemon.")
    parser.add_argument("-b", "--benchmark", action="store_true", help="benchmark time")
    args = parser.parse_args()

    ash = Ash()
    print("Bem-vindo Ash!")
    while True:
        sequence = utils.read_input()
        validated_sequence = utils.validate_sequence(sequence)

        start = time.process_time()
        if validated_sequence[0]:
            for direction in validated_sequence[1]:
                ash.move(direction)
        else:
            print("Sequência inválida")
            break
        end = time.process_time()

        print(ash.get_position())
        print(ash.get_pokemons())
        if args.benchmark:
            print("Tempo de execução: " + str(end-start) + " segundos")
            
        continue_flag = str(input("\nContinuar(s/n): "))
        if re.match("[s]", continue_flag) and len(continue_flag) == 1:
            pass
        elif re.match("[n]", continue_flag) and len(continue_flag) == 1:
            print("\nAdeus Ash!")
            break
        else:
            print("Comando inválido")
            break

if __name__ == "__main__":
    main()

