from flask import Blueprint

api = Blueprint('aistuff', __name__)

@api.route('/ai')
def index():
    return 'Hello ai'

"""
#MarkovChain

import random
import typing as t
from pathlib import Path

def read_names(file='names.txt') -> t.List[str]:
    filepath = Path(__file__).parent.joinpath(file)
    with open(filepath) as f:
        names = f.readlines()

    def k(n):
        s = n.split('\t')
        if len(s) > 1:
            return s[1]
        return n

    #names = map(k, names)
    names = filter(len, names)
    names = map(lambda n: n.strip(), names)
    names = filter(lambda n: n.isalpha(), names)
    names = list(names)
    names = set(names)

    #with open(filepath, 'w') as f:
    #    for name in names:
    #       f.write(name + '\n')

    return names


data = [''.join(chr(random.randint(ord('a'), ord('z'))) for a in range(5)) for j in range(1000)]


class Markov:

    def __init__(self, data: t.List[str]):
        self.data = data
        self.map: t.Dict[str, int] = None
        self.start: t.Dict[str, int] = None

    def get_word(self, length: int,  beginning: str = None) -> str:
        if beginning is not None:
            word = beginning
            i = len(beginning)-1
        else:
            word = self.get_starting_char()
            i = 0

        while i < length-1:
            word += self.get_next(word[i])
            i += 1
        return word

    def calculate(self) -> t.Dict[str, int]:
        # Get starting characters
        self.start = self.count_starting()
        chars = {char: 0 for char in self.get_unique_chars()}
        for char in chars:
            chars[char] = self.count_preceding(char)
        self.map = chars
        return chars

    def count_preceding(self, symbol: str) -> t.Dict[str, int]:
        counts = {}
        for word in self.data:
            word_size = len(word)
            for i, char in enumerate(word):
                if char == symbol:
                    preceding_index = i + 1
                    if preceding_index < word_size:
                        preceding_char = word[preceding_index]
                        counts[preceding_char] = counts.get(preceding_char, 0) + 1
        return counts

    def count_starting(self) -> t.Dict[str, int]:
        counts = {}
        for word in self.data:
            symbol = word[0]
            counts[symbol] = counts.get(symbol, 0) + 1
        return counts

    def get(self, chain: t.Dict[str, int], n: float = .1):
        reversed = {v: k for k, v in chain.items()}
        reversed_list = sorted(reversed.keys())[::-1]

        i = 0
        while i < len(chain) and random.random() < n:
            i += 1
            n /= 2

        i = min(i, len(chain)-1)
        most_frequent_symbol = reversed[reversed_list[i]]
        return most_frequent_symbol

    def get_next(self, symbol: str) -> str:
        return self.get(self.map[symbol])

    def get_starting_char(self) -> str:
        return self.get(self.start)

    def get_unique_chars(self) -> t.List[str]:
        chars = {symbol for symbol in ''.join(self.data)}
        return chars

if __name__ == '__main__':
    data = read_names()
    markov = Markov(data)
    a = markov.calculate()
    k = markov.get_word(7, 'api')
    print(k)

"""