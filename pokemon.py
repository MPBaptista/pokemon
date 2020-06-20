
class Ash():
    """
    Create initial Ash instance.
    """

    def __init__(self):
        """
        Create ash at default position (0,0)
        """
        self.position = [0,0]
        self.pokemons = 0

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
    def move_N(self):
        """ 
        Move Ash North (Norte)
        """
        self.position[1] += 1
    def move_S(self):
        """ 
        Move Ash South (Sul)
        """
        self.position[1] -= 1
    def move_E(self):
        """ 
        Move Ash East (Este)
        """
        self.position[0] += 1
    def move_O(self):
        """ 
        Move Ash West (Oeste)
        """
        self.position[0] -= 1

class WorldMap():
    """
    Create initial map instance.
    """
    def __init__(self):
        self.world_map = []
    def checkForPokemon(self, position):
        if position not in self.world_map:
            self.world_map.append(position)
            return True
        else:
            return False
    

def main():
    ash = Ash()
    world_map = WorldMap()
    print("Bem vindo Ash")
    while True:
        sequence = (str(input("Introduz a sequência de movimentos desejada(N/S/E/O separados por vírgulas): "))).split(",")
        for element in sequence:
            if element in ["N", "S", "E", "O"]:
                sequence_list.append(element)
            else:
                print("Sequência inválida")
        
        flag = str(input("Deseja Continuar? (s/n) "))
        if flag == "s":
            continue
        elif flag == "n":
            break

if __name__ == "__main__":
    main()
