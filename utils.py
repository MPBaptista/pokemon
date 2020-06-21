import re

def get_input():
    sequence = str(input("\nIntroduz a sequência de movimentos desejada(N/S/E/O):\n--> "))
    return sequence

def validade_sequence(sequence):
    sequence_list = []
    flag = True
    for element in sequence:
        if re.match("[NSEO]", element):
            sequence_list.append(element)
        else:
            print("Sequência inválida")
            flag = False
            break
    return (flag, sequence_list)