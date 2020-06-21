# Pokemon

### Introduction
Ash goes looking for pokemons in bi-dimensional field. Each position around him has one single pokemon. 

## Requirements
To run this program you need to have Python 3.6 installed (or the most 
recently available).

## Installation
### Clone
The first step is to clone the repository into your desired location. 
- Clone this repo to your local machine using `https://github.com/MPBaptista/pokemon.git`

## Usage
### Run
Run python file (use local Python version accordingly to requirements).
```shell
python3 pokemon.py
```
Run and display time benchmark.
```shell
python3 pokemon.py -b
```
### Unit Tests
Test Ash mehods.
```shell
python3 -m unittest --v test_pokemon.py 
```
Test utils methods.
```shell
python3 -m unittest --v test_utils.py 
```
## Example

    python3 pokemon.py -b

    Bem-vindo Ash!

    Introduz a sequência de movimentos desejada(N/S/E/O):
    --> N
    2
    Tempo de execução: 2.0524999999993465e-05 segundos

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