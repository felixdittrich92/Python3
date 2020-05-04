# eigene Listenklasse erstellen
# für eigene Listen/Sequenzen/etc. : https://docs.python.org/3/library/collections.abc.html

from collections.abc import MutableSequence

class MyOwnList(MutableSequence):
    def __init__(self, values=None):
        super().__init__() # erbt alles von Elternklasse
        if values:
            self._values = values
        else:
            self._values = []

    def __str__(self):
        return str(self._values)

    def __len__(self):
        return len(self._values)

    def __getitem__(self, idx):
        return self._values[idx]

    def __setitem__(self, idx, val):
        self._values[idx] = val

    def __delitem__(self, idx):
        del self._values[idx] # löschen - del

    def insert(self, idx, val):
        self._values.insert(idx, val)

    def append(self, val):
        self._values.append(val)

my_list = MyOwnList([1, 2, 3]) # __init__
print(my_list) # __str__
print(len(my_list)) # __len__
print(my_list[0]) # __getitem__
my_list[0] = 'hello' # __setitem__
print(my_list) # __str__
del my_list[1] # __del__
print(my_list) # __str__