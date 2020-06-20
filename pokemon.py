import time

class Ash():
    """
    Create initial Ash instance.
    """

    def __init__(self):
        """
        Create ash at default position (0,0)
        """
        self.position = [0,0]
        self.pokemons = 1

    def get_position(self):
        """ 
        Return current Ash position
        """
        return self.position
    def get_position_tuple(self):
        """ 
        Return current Ash position
        """
        return (self.position[0], self.position[1])
    def get_pokemons(self):
        """
        Get number of pokemons in Ash's Pokedex
        """
        return self.pokemons
    def add_pokemon(self):
        """
        Add new pokemon to Ash's Pokedex
        """
        self.pokemons += 1
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
        return (self.position[0], self.position[1])
    def __str__(self):
        return 'Ash está em ' + str(self.get_position_tuple()) + ' e tem ' + str(self.get_pokemons()) + ' pokemons.'

class WorldMap():
    """
    Create initial map instance.
    """
    def __init__(self):
        self.world_map = [(0,0)]
    def checkForPokemon(self, position):
        if position not in self.world_map:
            self.world_map.append(position)
            return True
        else:
            return False
    def __str__(self):
        return 'Casas exploradas: ' + str(self.world_map)

def main():
    ash = Ash()
    world_map = WorldMap()
    print("Bem-vindo Ash\n")
    while True:
        sequence = str(input("Introduz a sequência de movimentos desejada(N/S/E/O): "))
        sequence_list = []
        for element in sequence:
            if element in ["N", "S", "E", "O"]:
                sequence_list.append(element)
            else:
                print("Sequência inválida")
                break
        start = time.process_time()
        for direction in sequence_list:
            if world_map.checkForPokemon(ash.move(direction)):
                ash.add_pokemon()
            else:
                pass
        end = time.process_time()
        print(ash.get_pokemons())
        #print(end-start)
            
        flag = str(input("\nDeseja Continuar? (s/n) "))
        if flag == "s":
            continue
        elif flag == "n":
            print("\nAdeus Ash")
            break
        else:
            print("Comando inválido\n")
if __name__ == "__main__":
    main()

