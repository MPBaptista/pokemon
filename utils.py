import re

def read_input():
    """
    Moves ash in argument direction
    
    Args:
        direction (str): Str of direction to move in.
    """
    sequence = str(input("\nIntroduz a sequência de movimentos desejada(N/S/E/O):\n--> "))
    return sequence

def validate_sequence(sequence):
    """
    Checks if sequence of moves is valid.
    
    Args:
        sequence (str): string of direction to move in.
    
    Returns:
        valid_flag, sequence_list (tuple): tuple of boolean if string is valid and the sequence of moves.
    """
    sequence_list = []
    valid_flag = True
    for element in sequence:
        if re.match("[NSEO]", element):
            sequence_list.append(element)
        else:
            valid_flag = False
            break
    return (valid_flag, sequence_list)
