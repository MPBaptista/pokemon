# Pokemon

### Introduction
Ash goes looking for pokemons in bi-dimensional field. Each position around him has one single pokemon. 

## Requirements
To run this program you need to have Python 3.6 installed (or the most 
recently available).

## Installation
### Clone
The first step is to clone the repository into your desired location. 
- Clone this repo to your local machine as follows `git clone https://github.com/MPBaptista/pokemon.git`

## Usage
### Run
Run python file (use local Python version accordingly to requirements).
```shell
python3 pokemon.py
```
or run and display time benchmark.
```shell
python3 pokemon.py -b
```
### Unit Tests
#### For pokemon.py methods.
1. Tests get_position() in initial position;
2. Tests get_pokemons() in initial position;
3. Tests move() with 1 million successive moves;
4. Tests get_position() after moves;
5. Tests get_pokemon() after moves;
```shell
python3 -m unittest --v test_pokemon.py 
```
#### For utils.py methods.
1. Tests parse_input() with string "E";
2. Tests parse_input() with string "NESO";
3. Tests parse_input() with string "EQ";
4. Tests parse_input() with string "QE";
5. Tests parse_input() with string "1";
```shell
python3 -m unittest --v test_utils.py 
```
## Example

    python3 pokemon.py -b

    Bem-vindo Ash!

    Introduz a sequência de movimentos desejada(N/S/E/O):
    --> NNEESSO
    Total de pokemons apanhados: 8
    Tempo de execução: 0.0006053420001990162 segundos

    Continuar(s/n): n

    Adeus Ash!


## Notes
In regards to the definition of the bi-dimensional field a set proved to be the best way. Python set allows the addition of a new value, a numpy array has to create a new array for each new value, so the set proves to be vastly faster and simpler. 

Comparatively to a list a set still proves its advantages, being that the set only allows adding unique values the complexity of adding a value is only O(1), to add a new value to a list the list has to be checked for the value ```if x not in list: add``` raising the complexity to O(N).

## Limits/Pitfalls
1. Due to limitations of all POSIX compilant command-lines the max input the program will behave correctly to is 4095 moves, to bypass this simply input successive move sequences of up to 4095 moves each.

## Author
* **Miguel Baptista**

## License
[GPLv3](https://www.gnu.org/licenses/gpl-3.0.txt)