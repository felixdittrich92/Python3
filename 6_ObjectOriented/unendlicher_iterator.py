# unendlicher Iterator beginnt wenn "zuende" von vorne zu iterrieren
# itertools: https://docs.python.org/3/library/itertools.html

import itertools

class NameIterator:
    def __init__(self, names):
        self.names = names
        self.num_names = len(self.names)
        self.current_n = 0

    def __iter__(self):
        self.current_n = 0
        return self # returnt das iterierbare Objekt
    
    def __next__(self):
        if self.current_n < self.num_names:
            current_result = self.names[self.current_n]
            self.current_n += 1
            return current_result
        else:
            self.current_n = 0
            current_result = self.names[self.current_n]
            self.current_n += 1
            return current_result

names = ['Hans', 'Franz', 'Schranz']

my_iterator = NameIterator(names)

for i in range(7):
    print(next(my_iterator))

print("---------------itertools------------------")
# einfacher mit itertools
my_iterator2 = itertools.cycle(names)

for i in range(7):
    print(next(my_iterator))